import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
# =============================================================================
#  mean = [0, 0]
#     cov = [[1, 0], [0, 1]]
#  mean2 = [5, 5]
#     cov2 = [[1, 0], [0, 1]]
# =============================================================================

def generate_data(mean,cov,y,size):
    
    bias = [1 for i in range(size)]
    x = np.random.multivariate_normal(mean, cov,size).T  
    bias = (np.matrix(bias))
    x = np.r_[x,bias]
    x = np.matrix(x)
    if y == 1:
        T = (np.matrix(np.ones(size)))
    elif y == -1:
        T = np.matrix([-1 for i in range(size)])
    #print(x.shape)
    return x, T
    
# =============================================================================
# print(generate_data( [0, 0] , [[1, 0], [0, 1]] ,1,100)[0][:,1].shape)
# =============================================================================

def create_data(mean1,cov1,y1,\
         mean2, cov2,y2,size):

    x1,t1 = generate_data(mean1,cov1,y1,size)
    x2,t2 = generate_data(mean2,cov2,y2,size)
    data = np.c_[x1,x2]  
    #print(data)
    plotdata(x1,x2)
    permu = np.random.permutation(2*size)
    dataShuf = data[:,permu]
    T = np.c_[t1,t2]
    #print(T)
    T = T[:,permu]  
    return dataShuf, T


def plotdata(x1,x2):

    
    plt.scatter(x1[0].tolist(),x1[1].tolist() ,c='r')
    plt.scatter(x2[0].tolist(), x2[1].tolist(), c='b')
    plt.ylabel("some numbers")
    
    
def sigmoid(x):
    return (2/((1+math.exp(-x)))) - 1


def sigmoid_prime(x):
    return (1+sigmoid(x))*(1-sigmoid(x))/2

def zedLoop(x,y):
    firstFlag = 1
    returnMatrix = 0
    for i in range (len(x[0])):
        returnVector = []
        for j in range (len(y)):
            returnVector.append(zed(x[j][i],y[j][i]))
            #returnVector.append(x[j])
        if firstFlag==1:
            returnMatrix = np.matrix(returnVector)
            firstFlag = 0
        else:
            returnMatrix = np.r_[returnMatrix,np.matrix(returnVector)]
    return returnMatrix

def zed(x,y):
    
    return  (math.exp(-(x**2+y**2)/10)-0.5)

def initialize_weights(n, input_dimension, ):
    # =============================================================================
    #     number of nodes in hidden layer - n (not including the bias)   
    #     length of the row of weight vector = length of column of data matrix
    #    W1 is outer layer. W2 are weights of the hidden layer
    #    added bias to outer layer. 
    # =============================================================================
    #W1 = np.matrix(np.random.multivariate_normal(mean, cov,size).T)
    W1 = np.matrix(np.random.normal(0,1,input_dimension))
    for x in range(n-1):
         W1 = np.r_[W1,np.matrix(np.random.normal(0,1,input_dimension))]
         #W1 = np.r_[W1,np.matrix(np.random.normal(0,1,n+1))]
         #if you want bias in second layer
    W2 = np.matrix(np.random.normal(0,1,n+1))

    return W1, W2


def forward_pass(data,W1,W2,size):
    bias = [1 for i in range(size)]
    bias = (np.matrix(bias))
    sigmoid_f = np.vectorize(sigmoid)
    sigmoid_prime_f = np.vectorize(sigmoid_prime)
    H_star = W1*data
    H_star = np.r_[H_star,bias]
    H = sigmoid_f(H_star)
    
    # remove this comment if you want bias in second layer
    O_star = W2*H
    O = sigmoid_f(O_star)



    sigmoid_prime_O_star= (sigmoid_prime_f(O_star))
    sigmoid_prime_H_star= (sigmoid_prime_f(H_star))
    return H_star,H,O_star,O,sigmoid_prime_O_star,sigmoid_prime_H_star,H
    
    
    
def backpropagation(H_star,H,O_star,O,T,sigmoid_prime_O_star,sigmoid_prime_H_star,W1,W2,HiddenLayerNodes):

    delta_O = np.multiply((O-T),(sigmoid_prime_O_star))
    placeHolder = (np.transpose(W2)*delta_O)
    delta_H = np.multiply(placeHolder,sigmoid_prime_H_star)
    delta_H = np.array(delta_H)

    delta_H = np.delete(delta_H, HiddenLayerNodes,axis = 0)

    return delta_O,delta_H
    
    
    
    
def batch_learning(data, T, W1, W2):
    sigmoid_f = np.vectorize(sigmoid)
    sigmoid_prime_f = np.vectorize(sigmoid_prime)

def weight_update(delta_O,delta_H,X,H,etha):
    delta_W1 = -np.matrix(delta_H)*np.matrix(np.transpose(X))
    delta_W2 = -delta_O*np.transpose(H)
    return delta_W1,delta_W2
    

def iteration(X,T,W1,W2,etha,HiddenLayerNodes,size,xx,yy):
    delta = 0
    O = 0
    for x in range(1,10):
        for _ in range(1,40):
                
            H_star,H,O_star,O,sigmoid_prime_O_star,sigmoid_prime_H_star,H = forward_pass(X,W1,W2,size)
            delta_O,delta_H = backpropagation(H_star,H,O_star,O ,T,sigmoid_prime_O_star,sigmoid_prime_H_star,W1,W2,HiddenLayerNodes)
            delta_W1,delta_W2 =  weight_update(delta_O,delta_H,X,H,etha)
            W1 = W1 + delta_W1*etha
            W2 = W2 + delta_W2*etha
            delta = delta_W1
        #print(W1[0])
        print(delta)
        zz = np.reshape(O,(21,21))
        mashPlot(xx,yy,np.array(zz))
    return O

def mashPlot(X, Y, Z):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        # Plot the surface.
        surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        # Customize the z axis.
        ax.set_zlim(-1.01, 1.01)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        # Add a color bar which maps values to colors.
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()

def main():

    x = np.arange(-5,5.5,0.5)
    y = np.arange(-5,5.5,0.5)
    xx,yy =np.meshgrid(x,y, sparse=False)
    z2 = (np.exp(-(xx**2+yy**2)/10)-0.5)
    T = np.reshape(z2,(1,(21*21)))
    bias = [1 for i in range(21*21)]
    bias = (np.matrix(bias))
    Patterns = np.r_[np.reshape((xx),(1,(21*21))),np.reshape(yy,(1,(21*21)))] 
    Patterns = np.r_[Patterns,(bias)]
    etha = 0.005
    size = 21*21
    input_dimension = 3
    data = Patterns
    HiddenLayerNodes = 3
    #it seems you need more 20 to get a good circle
    W1, W2 = initialize_weights(HiddenLayerNodes,input_dimension )

    O = np.matrix(iteration(data,T,W1,W2,etha,HiddenLayerNodes,size,xx,yy))


    
    """
    print("space\n")
    print(zz[0])
    print("space\n")
    print(z2[0])
    """
    plt.show()
    print("O\n")
    print(O)
    print("T\n")
    print(T)
    
    #plt.contourf(xx,yy,np.array(zz))
    #plt.contourf(xx,yy,z2)
    
    #plt.ylabel("y value")
    #plt.xlabel("x value")
    #plt.title("")
    #plt.show()
    return
main()    
    