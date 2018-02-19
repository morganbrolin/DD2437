
import matplotlib.pyplot as plt
import numpy as np
import math


def read_animals():
	#returns a list with list 
	# returns a list of animals with attributes
	f = open('animals.dat','r') 
	animal_list = []
	animal = []
	for _ in range(32):
		animal = []
		for _ in range(84):
			attribute = f.read(1)
			animal.append(int(attribute))
			f.read(1)
		animal_list.append(animal)
	return animal_list
def read_animals_names():
	#returns a list with animal names
	f = open('animalnames.dat','r') 
	animal_list = []
	for _ in range(32):
		animal_list.append(f.readline())

	return animal_list
def similiarity(animal,W):
	d = None
	index = None
	for i in range(len(W)):
		dist = float((animal - W[i])*np.transpose(animal - W[i]))
		if i == 0:
			d = dist
			index = 0
		elif (dist) > d:
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
			#print((animal - W[i]))
			#print(dist,"dist")
			#print(np.transpose(animal-W[i]),"transpose")
			if i == 0:
				d = dist
				index = i
			elif (dist) > d:
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
		#print(index)

		if neighbourhood == 0 :
			W[(index)] = W[(index)] + step*(animal-W[(index)])


		for i in range(neighbourhood):
			ind = i + index - neighbourhood/2
			ind = int(ind)
			if ind < 0:
				pass
			elif ind > len(W[0]):
				pass
			else:
				W[(ind)] = W[(ind)] + step*(animal-W[(ind)])
				pass



	return W
def epoch_iteration(iterations,animal_list,W,neighbourhood,step,original_neighbourhood):
	for _ in range(iterations):
		W = sequencial_iteration(animal_list,W,int(neighbourhood-2),step)
		print(neighbourhood)
		neighbourhood = neighbourhood - (original_neighbourhood/iterations)
	return W
def main():
	neighbourhood = 52
	step = 0.2
	iterations = 20
	nodes = 100
	animal_list = np.matrix(read_animals())
	W = initialize_weights(nodes,84)
	W = epoch_iteration(iterations,animal_list,W,neighbourhood,step,neighbourhood)
	out = output(animal_list,W)
	out_list = []
	names_list = read_animals_names()
	for x in range(nodes):
		list_in_list = []
		for y in out:
			if y ==[]:
				break
			if y[0]==x:
					list_in_list.append(names_list[y[1]-1])
		out_list.append(list_in_list)



	read_animals_names()
	print(out_list)


main()