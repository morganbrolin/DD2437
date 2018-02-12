# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 00:39:30 2018

@author: mukund
"""

import matplotlib.pyplot as plt
import numpy as np
import math

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
    W1 = np.matrix(np.random.normal(0,1,input_dimension+1))
    for x in range(n-1):
         W1 = np.r_[W1,np.matrix(np.random.normal(0,1,input_dimension+1))]
         #W1 = np.r_[W1,np.matrix(np.random.normal(0,1,n+1))]
         #if you want bias in second layer
    W2 = np.matrix(np.random.normal(0,1,input_dimension))
    for x in range(n):
        W2 = np.r_[W2,np.matrix(np.random.normal(0,1,input_dimension))]
    return W1, W2


def forward_pass(data,W1,W2):


    sigmoid_f = np.vectorize(sigmoid)
    sigmoid_prime_f = np.vectorize(sigmoid_prime)
    bias = [1 for i in range(1)]
    bias = (np.matrix(bias))
    H_star = W1*data
    H_star = np.r_[H_star,bias]
    H = sigmoid_f(H_star)
    #H = np.r_[H,bias]
    # remove this comment if you want bias in second layer
    O_star = np.transpose(W2)*H
    O = sigmoid_f(O_star)



    sigmoid_prime_O_star= (sigmoid_prime_f(O_star))
    sigmoid_prime_H_star= (sigmoid_prime_f(H_star))
    return H_star,H,O_star,O,sigmoid_prime_O_star,sigmoid_prime_H_star,H
    
    
    
def backpropagation(H_star,H,O_star,O,T,sigmoid_prime_O_star,sigmoid_prime_H_star,W1,W2):

    delta_O = np.multiply((O-T),(sigmoid_prime_O_star))
    placeHolder = W2*delta_O
    delta_H = np.multiply(placeHolder,sigmoid_prime_H_star)
    delta_H = np.delete(delta_H, 3,axis = 0)
    return delta_O,delta_H
    
    
    
    
def batch_learning(data, T, W1, W2):
    sigmoid_f = np.vectorize(sigmoid)
    sigmoid_prime_f = np.vectorize(sigmoid_prime)

def weight_update(delta_O,delta_H,X,H,etha):
    delta_W1 = -delta_H*np.transpose(X)
    delta_W2 = -delta_O*np.transpose(H)
    return delta_W1,delta_W2
    

def iteration(X,T,W1,W2,etha):       
    H_star,H,O_star,O,sigmoid_prime_O_star,sigmoid_prime_H_star,H = forward_pass(X,W1,W2)
    delta_O,delta_H = backpropagation(H_star,H,O_star,O ,T,sigmoid_prime_O_star,sigmoid_prime_H_star,W1,W2)
    delta_W1,delta_W2 =  weight_update(delta_O,delta_H,X,H,etha)
    W1 = W1 + delta_W1*etha
    W2 = W2 + np.transpose(delta_W2*etha)
    return O,W1,W2

def main():
    mean1 = [0, 0]
    cov1 = [[1, 0], [0, 1]]
    mean2 = [2, 2]
    cov2 = [[1, 0], [0, 1]]
    etha = 0.01
    input_dimension = 8
    HiddenLayerNodes = 3
    numberOfIterations = 1000
    W1, W2 = initialize_weights(HiddenLayerNodes,input_dimension )
    X1 = [1,-1,-1,-1,-1,-1,-1,-1]
    X2 = [-1,1,-1,-1,-1,-1,-1,-1]
    X3 = [-1,-1,1,-1,-1,-1,-1,-1]
    X4 = [-1,-1,-1,1,-1,-1,-1,-1]
    X5 = [-1,-1,-1,-1,1,-1,-1,-1]
    X6 = [-1,-1,-1,-1,-1,1,-1,-1]
    X7 = [-1,-1,-1,-1,-1,-1,1,-1]
    X8 = [-1,-1,-1,-1,-1,-1,-1,1]
    dataList = [X1,X2,X3,X4,X5,X6,X7,X8]
    #last one is bias
    O = 0
    latestX = 0
    oldesum = 1
    e = 0.4
    esum = 0
    for itera in range(numberOfIterations):
        esum=0
        for X in dataList:
            T = np.transpose(np.matrix(X))
            data = np.transpose(np.matrix(X+[1]))
            
            e = (O-T).sum()/16
            esum = esum +e
            latestX = X
        O,W1,W2 = iteration(data,T,W1,W2,etha)
        plt.plot([itera-1,itera],[oldesum,esum/8],c="b")
        oldesum = esum/8

    

    print(e)
    print(O)
    print(latestX)
    plt.show()
    return
    


main()    
    
    
    