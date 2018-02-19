
import matplotlib.pyplot as plt
import numpy as np
import math


def read_cities():
	#returns a list with list 
	# returns a list of animals with attributes
	f = open('cities.dat','r') 
	cites_list = []
	city = []
	for _ in range(10):
		city = []
		for _ in range(2):
			attribute = f.read(6)
			city.append(float(attribute))
			f.readline(1)
		cites_list.append(city)
		f.readline()
	return cites_list

def similiarity(animal,W):
	d = None
	index = None
	for i in range(len(W)):
		dist = float((animal - W[i])*np.transpose(animal - W[i]))
		if i == 0:
			d = dist
			index = 0
		elif (dist) < d:
			d = dist
			index = i
	return index


def output(animal_list,W):
	list_of_index_values = []
	animal_index = 0
	for animal in animal_list:
		animal_index = animal_index + 1
		d = None
		index = None
		for i in range(len(W)):
			dist = float((animal - W[i])*np.transpose(animal - W[i]))

			if i == 0:
				d = dist
				index = i
			elif (dist) < d:
				d = dist
				index = i
		list_of_index_values.append([index,animal_index])
	return list_of_index_values


def initialize_weights(nodes, input_dimension ):
	#100 nodes and each node have 84 attributes each attribute has a weight
    W = np.matrix(np.random.uniform(0,1,input_dimension))
    for x in range(nodes-1):
         W = np.r_[W,np.matrix(np.random.uniform(0,1,input_dimension))]
    return W

def sequencial_iteration(animal_list,W,neighbourhood,step):
	for animal in animal_list:

		index = similiarity(animal,W)
		#indexes is list index start from 0
		if neighbourhood == 0 :
			W[(index)] = W[(index)] + step*(animal-W[(index)])

		
		else:
			for i in range((neighbourhood*2)+1):
				ind = i + index - neighbourhood 
				ind = int(ind)
				if ind < 0:
					ind = (len(W)+ind)
					W[(ind)] = W[(ind)] + step*(animal-W[(ind)])

					
				elif ind > len(W)-1:
					ind = (ind-len(W))
					W[(ind)] = W[(ind)] + step*(animal-W[(ind)])
				else: 
					W[(ind)] = W[(ind)] + step*(animal-W[(ind)])

					
  


	return W
def epoch_iteration(iterations,animal_list,W,neighbourhood,step,original_neighbourhood):
	for _ in range(iterations):
		print(int(neighbourhood+0.49))
		W = sequencial_iteration(animal_list,W,int(neighbourhood+0.49),step)
		neighbourhood = neighbourhood - (original_neighbourhood/iterations)
		
	return W
def main():
	neighbourhood = 2
	step = 0.2
	iterations = 20
	nodes = 10
	cities = read_cities()
	animal_list = np.matrix(cities)
	W = initialize_weights(nodes,2)
	W = epoch_iteration(iterations,animal_list,W,neighbourhood,step,neighbourhood)
	out = output(animal_list,W)

	print(out)
	order_list = []
	for city in cities:
		plt.scatter(city[0], city[1])
	for i in range(nodes):
		for order in out:
			if i == order[0]:
				order_list.append(order[1])
	print("order",order_list)
	oldestcity = cities[order_list[len(order_list)-1]]
	oldcity = cities[order_list[len(order_list)-1]]
	for i in order_list:
		newcity = cities[i-1]

		plt.plot([newcity[0],oldcity[0]],[newcity[1],oldcity[1]])
		oldcity = newcity
	newcity = oldcity
	oldcity = oldestcity
	plt.plot([newcity[0],oldcity[0]],[newcity[1],oldcity[1]])
	plt.ylabel("Y")
	plt.xlabel("X")
	plt.title("Cyclic Tour")
	plt.show()


main()