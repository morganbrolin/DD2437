# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 00:39:30 2018

@author: mukund
"""

import matplotlib.pyplot as plt
import numpy as np

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
    return (1+sigmoid(x))(1-sigmoid(x))/2


def initialize_weights(n, size, mean, cov, ):
    # =============================================================================
    #     number of nodes in hidden layer - n (not including the bias)   
    #     length of the row of weight vector = length of column of data matrix
    #    W1 is outer layer. W2 are weights of the hidden layer
    #    added bias to outer layer. 
    # =============================================================================
    W1 = np.matrix(np.random.multivariate_normal(mean, cov,size).T)
    W2 = np.matrix(np.random.normal(0,1,n))
    return W1, W2


def forward_pass():
    return
    
    
    
def backpropagation():
    
    return
    
    
    
    
def batch_learning(data, T, W1, W2):
    sigmoid_f = np.vectorize(sigmoid)
    sigmoid_prime_f = np.vectorize(sigmoid_prime)
    


def main():
    
    return
    


main()    
    
    
    
