# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 00:39:30 2018

@author: mukund
"""

import matplotlib.pyplot as plt
import numpy as np
import math
import pickle

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
    permu = np.random.permutation(2*size)
    dataShuf = data[:,permu]
    T = np.c_[t1,t2]
    #print(T)
    T = T[:,permu]
    with open('dataShuf.pickle', 'wb') as f:
        pickle.dump(dataShuf, f) 
    with open('T.pickle', 'wb') as f:
        pickle.dump(T, f)
    with open('x1.pickle', 'wb') as f:
        pickle.dump(x1, f) 
    with open('x2.pickle', 'wb') as f:
        pickle.dump(x2, f)    
    #return dataShuf, T
    return

def create_new_data(mean1,cov1,y1,\
         mean2, cov2,y2,size):

    x1,t1 = generate_data(mean1,cov1,y1,size)
    x2,t2 = generate_data(mean2,cov2,y2,size)
    data = np.c_[x1,x2]  
    #print(data)
    permu = np.random.permutation(2*size)
    dataShuf = data[:,permu]
    T = np.c_[t1,t2]
    #print(T)
    T = T[:,permu]
    with open('dataShuftest.pickle', 'wb') as f:
        pickle.dump(dataShuf, f) 
    with open('Ttest.pickle', 'wb') as f:
        pickle.dump(T, f)
    with open('x1test.pickle', 'wb') as f:
        pickle.dump(x1, f) 
    with open('x2test.pickle', 'wb') as f:
        pickle.dump(x2, f)    
    #return dataShuf, T
    return


def plotdata():
    x1 = 0
    x2 = 0
    x1test = 0
    x2test = 0
    with open('x1.pickle', 'rb') as f:
        x1 = (pickle.load(f))  
    with open('x2.pickle', 'rb') as f:
        x2 = (pickle.load(f)) 
    with open('x1test.pickle', 'rb') as f:
        x1test = (pickle.load(f))  
    with open('x2test.pickle', 'rb') as f:
        x2test = (pickle.load(f)) 
    
    plt.scatter(x1[0].tolist(),x1[1].tolist() ,c='r')

    plt.scatter(x2[0].tolist(), x2[1].tolist(), c='b')
    plt.scatter(x1test[0].tolist(),x1test[1].tolist() ,c='g')

    plt.scatter(x2test[0].tolist(), x2test[1].tolist(), c='y')
    plt.ylabel("some numbers")
    
    
def sigmoid(x):
    return 2/(1+np.log(1+math.exp(-x))) - 1


def sigmoid_prime(x):
    return (1+sigmoid(x))*(1-sigmoid(x))/2


def initialize_weights(n, input_dimension, ):
    # =============================================================================
    #     number of nodes in hidden layer - n (not including the bias)   
    #     length of the row of weight vector = length of column of data matrix
    #    W1 is outer layer. W2 are weights of the hidden layer
    #    added bias to outer layer. 
    # =============================================================================
    #W1 = np.matrix(np.random.multivariate_normal(mean, cov,size).T)
    W1 = np.matrix(np.random.normal(0,1,n))
    for x in range(input_dimension-1):
         W1 = np.r_[W1,np.matrix(np.random.normal(0,1,n))]
         #W1 = np.r_[W1,np.matrix(np.random.normal(0,1,n+1))]
         #if you want bias in second layer
        
   
    W2 = np.matrix(np.random.normal(0,1,n))
    return np.transpose(W1), W2


def forward_pass(data,W1,W2,size):
    bias = [1 for i in range(size*2)]
    bias = (np.matrix(bias))
    sigmoid_f = np.vectorize(sigmoid)
    sigmoid_prime_f = np.vectorize(sigmoid_prime)
    H_star = W1*data
    H = sigmoid_f(H_star)
    #H = np.r_[H,bias]
    # remove this comment if you want bias in second layer
    O_star = W2*H
    O = sigmoid_f(O_star)



    sigmoid_prime_O_star= (sigmoid_prime_f(O_star))
    sigmoid_prime_H_star= (sigmoid_prime_f(H_star))
    return H_star,H,O_star,O,sigmoid_prime_O_star,sigmoid_prime_H_star,H
    
    
    
def backpropagation(H_star,H,O_star,O,T,sigmoid_prime_O_star,sigmoid_prime_H_star,W1,W2):

    delta_O = np.multiply((O-T),(sigmoid_prime_O_star))
    placeHolder = (np.transpose(W2)*delta_O)
    delta_H = np.multiply(placeHolder,sigmoid_prime_H_star)
    return delta_O,delta_H
    
    
    
def step(x):
    return 1 * (x > 0)
def batch_learning(data, T, W1, W2):
    sigmoid_f = np.vectorize(sigmoid)
    sigmoid_prime_f = np.vectorize(sigmoid_prime)

def weight_update(delta_O,delta_H,X,H,etha):
    delta_W1 = -delta_H*np.transpose(X)
    delta_W2 = -delta_O*np.transpose(H)
    return delta_W1,delta_W2
    

def iteration(X,T,W1,W2,size,etha,datatest,Ttest):
    O = 0
    step_f = np.vectorize(step)
    old = ((step_f(W1*datatest)-(step_f(Ttest))!=0).sum()/100)
    old2 = ((step_f(W1*X)-(step_f(T))!=0).sum()/200)
    for x in range(1,10):
        for y in range(1,10):
                
            H_star,H,O_star,O,sigmoid_prime_O_star,sigmoid_prime_H_star,H = forward_pass(X,W1,W2,size)
            delta_O,delta_H = backpropagation(H_star,H,O_star,O ,T,sigmoid_prime_O_star,sigmoid_prime_H_star,W1,W2)
            delta_W1,delta_W2 =  weight_update(delta_O,delta_H,X,H,etha)
            W1 = W1 + delta_W1*etha
            W2 = W2 + delta_W2*etha
            plt.plot([((x*10)+y)-1,((x*10)+y)],[old,((step_f(W1*datatest)-(step_f(Ttest))!=0).sum()/100)],c="r")
            old = ((step_f(W1*datatest)-(step_f(Ttest))!=0).sum()/100)
            plt.plot([((x*10)+y)-1,((x*10)+y)],[old2,((step_f(W1*X)-(step_f(T))!=0).sum()/200)],c="b")
            old2 = ((step_f(W1*X)-(step_f(T))!=0).sum()/200)

        #print(O)
    #print(O)
    return W1,O

def main():
    mean1 = [0, 0]
    cov1 = [[1, 0], [0, 1]]
    mean2 = [2,2]
    cov2 = [[1, 0], [0, 1]]
    etha = 0.01
    #the real size is size*2
    size = 100
    y1 = 1
    y2 = -1
    HiddenLayerNodes = 10
    data = 0
    T = 0
    #create_data(mean1,cov1,y1,\
         #mean2, cov2,y2,size) 
    #create_new_data(mean1,cov1,y1,\
         #mean2, cov2,y2,size) 

    Ttest = 0
    datatest = 0
    with open('T.pickle', 'rb') as f:
        T = np.matrix(pickle.load(f))  
    with open('dataShuf.pickle', 'rb') as f:
        data = np.matrix(pickle.load(f)) 
    with open('Ttest.pickle', 'rb') as f:
        Ttest = np.matrix(pickle.load(f))  
    with open('dataShuftest.pickle', 'rb') as f:
        datatest = np.matrix(pickle.load(f)) 
    #plotdata()
    W1, W2 = initialize_weights(HiddenLayerNodes,3)
    print("T")
    print(T)

    W1, O = iteration(data,T,W1,W2,size,etha,datatest,Ttest)
    #print("Target")
    #print(((T-O)>0.7).sum()/size*2/100)
    for x in range(W1.shape[0]):
        W01 = W1.item((x, 0))
        W02 = W1.item((x, 1))
        W00 = W1.item((x, 2))
        #a = W01
        #b = W02
        #c = W00
        #y = (-c-ax)/b x = 0 ->  y = -c/b
        #x = -c/a if y = 0 

        #plt.plot([0,-W00/W02],[-W00/W01,0])
    plt.show()
    return
    


main()    
    
    
    