import matplotlib.pyplot as plt
from random import *
import numpy as np
import pickle


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

def step(x):
    return 1 * (x > 0)
def create_data(mean1,cov1,y1,\
 		mean2, cov2,y2,size):

	T = 0
	x1 = 0
	with open('T.pickle', 'rb') as f:
		T = np.matrix(pickle.load(f))  
	with open('dataShuf.pickle', 'rb') as f:
		data = np.matrix(pickle.load(f))   
	with open('x1.pickle', 'rb') as f:
	
		x1 = (pickle.load(f))  
	#plotdata()
	w = np.random.normal(0, 1, 3)

	return data, T, np.matrix(w)


def plotdata():
    x1 = 0
    x2 = 0
    with open('x1.pickle', 'rb') as f:
        x1 = (pickle.load(f))  
    with open('x2.pickle', 'rb') as f:
        x2 = (pickle.load(f)) 
        plt.scatter(x1[0].tolist(),x1[1].tolist() ,c='r')

    plt.scatter(x2[0].tolist(), x2[1].tolist(), c='b')
    plt.ylabel("some numbers")

def step_blearning(data, T, W, eta, iterations):
	step_f = np.vectorize(step)
	old = ((step_f(W*data)-(step_f(T))!=0).sum()/200)
	for itera in range(iterations):
		Wdelta = -eta*((step_f(W*data)-T)*np.transpose(data))
		W = W + Wdelta
		#print(Wdelta)
		plt.plot([itera-1,itera],[old,((step_f(W*data)-(step_f(T))!=0).sum()/200)],c="y")
		old = ((step_f(W*data)-(step_f(T))!=0).sum()/200)
	return W, Wdelta

def blearning(data, T, W, eta, iterations):
	step_f = np.vectorize(step)
	old = ((step_f(W*data)-(step_f(T))!=0).sum()/200)
	
	for itera in range(iterations):
		Wdelta = -eta*(((W*data-T))*np.transpose(data))
		W = W + Wdelta
		#print(Wdelta)
		plt.plot([itera-1,itera],[old,((step_f(W*data)-(step_f(T))!=0).sum()/200)],c="g")
		old = ((step_f(W*data)-(step_f(T))!=0).sum()/200)

	return W, Wdelta


def seqlearning(data, T, W, eta, iterations):
    step_f = np.vectorize(step)
    old = ((step_f(W*data)-(step_f(T))!=0).sum()/200)
    
    for itera in range(iterations):
        for i in range(len((data[1,:][0]).tolist()[0])):
            Wdelta = -eta*((W*data[:,i]-T[0,i])*np.transpose(data[:,i]))
            W = W + Wdelta
        plt.plot([itera-1,itera],[old,((step_f(W*data)-(step_f(T))!=0).sum()/200)],c="b")
        old = ((step_f(W*data)-(step_f(T))!=0).sum()/200)
    return W, Wdelta

def seqlearning_step(data, T, W, eta, iterations):
    step_f = np.vectorize(step)
    old = ((step_f(W*data)-(step_f(T))!=0).sum()/200)
    for itera in range(iterations):
        for i in range((len((data[1,:][0]).tolist()[0]))):
            Wdelta = -eta*((step_f(W*data[:,i])-T[0,i])*np.transpose(data[:,i]))
            W = W + Wdelta
        plt.plot([itera-1,itera],[old,((step_f(W*data)-(step_f(T))!=0).sum()/200)],c="r")
        old = ((step_f(W*data)-(step_f(T))!=0).sum()/200)

    return W, Wdelta
		
def main():

	#dataShuf,T,W11 = (create_data([0, 0] , [[1, 0], [0, 1]] , 1, [5, 5], [[1, 0], [0, 1]], -1, 100))
	#dataShuf,T,W22 = (create_data([0, 0] , [[1, 0], [0, 1]] , 1, [5, 5], [[1, 0], [0, 1]], -1, 100))
	dataShuf,T,W33 = (create_data([0, 0] , [[1, 0], [0, 1]] , 1, [5, 5], [[1, 0], [0, 1]], -1, 100))
	dataShuf,T,W44 = (create_data([0, 0] , [[1, 0], [0, 1]] , 1, [5, 5], [[1, 0], [0, 1]], -1, 100))
	#W3 , Wdelta3 = step_blearning(dataShuf, T, W11, 0.0003, 10)
	#W2 , Wdelta2 =  seqlearning_step(dataShuf, T, W22, 0.01, 10)
	W4 , Wdelta4 = blearning(dataShuf, T, W33, 0.0003, 10)
	W1 , Wdelta1 = seqlearning(dataShuf, T, W44, 0.01, 10)


	#print(W*dataShuf)
	W = W1.tolist()
	#plt.plot([0,-W[0][2]/W[0][1]],[-W[0][2]/W[0][0],0])
	plt.show()


main()