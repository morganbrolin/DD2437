import matplotlib.pyplot as plt
from random import *
import numpy as np

#mean = [0, 0]
#	cov = [[1, 0], [0, 1]]
#mean2 = [5, 5]
#	cov2 = [[1, 0], [0, 1]]

def generate_data(mean,cov,y,size):
	
	bias = [1 for i in range(size)]
	x = np.random.multivariate_normal(mean, cov,size).T  
	shufX = []
	bias = (np.matrix(bias))
	x = np.r_[x,bias]
	x = np.matrix(x)
	if y == 1:
		T = (np.matrix(np.ones(size)))
	elif y == -1:
		T = np.matrix([-1 for i in range(size)])
	#print(x.shape)
	return x, T
	
#print(generate_data( [0, 0] , [[1, 0], [0, 1]] ,1,100)[0][:,1].shape)


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
	w = np.random.normal(0, 1, len(x1[:,1]))
	T = T[:,permu]

	return dataShuf, T, np.matrix(w)


def plotdata(x1,x2):

	
	plt.scatter(x1[0],x1[1] ,c='r')
	plt.scatter(x2[0], x2[1], c='b')
	plt.ylabel("some numbers")
	

def blearning(data, T, W, eta, iterations):
	for _ in range(iterations):
		Wdelta = -eta*((W*data-T)*np.transpose(data))
		W = W + Wdelta
		#print(Wdelta)
	return W, Wdelta


def seqlearning(data, T, W, eta, iterations):
    for i in range(len(data[1,:])):
        for _ in range(iterations):
            Wdelta = -eta*((W*data[:,i]-T[0,i])*np.transpose(data[:,i]))
            W = W + Wdelta
            
    return W, Wdelta
		
def main():

	dataShuf,T,W = (create_data([0, 0] , [[1, 0], [0, 1]] , 1, [5, 5], [[1, 0], [0, 1]], -1, 100))
	W , Wdelta = blearning(dataShuf, T, W, 0.0003, 30)
	#print(W, Wdelta)
	W = W.tolist()
	print(W)
	plt.plot([0,-W[0][2]/W[0][1]],[-W[0][2]/W[0][0],0])
	plt.show()


main()