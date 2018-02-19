
import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

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

def read_votes():
	#returns a list with list 
	# returns a list of animals with attributes
	f = open('votes.dat','r') 
	data = f.readline().split(',')
	animal_list = []
	animal = []
	for i in range(349):
		animal = []
		for j in range(31):

			animal.append(float(data[i*j]))
		animal_list.append(animal)
	return animal_list

def read_mpparty():
	#returns a list with list 
	# returns a list of animals with attributes
	f = open('mpparty.dat','r') 
	animal_list = []
	for line in f:
		data = line.split('\n')
		animal_list.append(int(data[0]))
	return animal_list

def read_sex():
	#returns a list with list 
	# returns a list of animals with attributes
	f = open('mpsex.dat','r') 
	animal_list = []
	for line in f:
		data = line.split('\n')
		animal_list.append(int(data[0]))
	return animal_list

def read_district():
	#returns a list with list 
	# returns a list of animals with attributes
	f = open('mpdistrict.dat','r') 
	animal_list = []
	for line in f:
		data = line.split('\n')
		animal_list.append(int(data[0]))
	return animal_list

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
	#100 nodes and each node have 31 attributes each attribute has a weight
    W = np.matrix(np.random.uniform(0,1,input_dimension))
    for x in range(nodes-1):
         W = np.r_[W,np.matrix(np.random.uniform(0,1,input_dimension))]
    return W

def sequencial_iteration(animal_list,W,neighbourhood,step):
	for animal in animal_list:

		index = similiarity(animal,W)
		index_i= int(str(index)[0])
		index_j = 0
		if len(str(index)) != 1:
			index_j = int(str(index)[1])
		if neighbourhood == 0 :
			W[(index)] = W[(index)] + step*(animal-W[(index)])

		else:
			for i in range(neighbourhood*2+1):
				for j in range(neighbourhood*2+1):
					ind_i = i + index_i - neighbourhood
					ind_j = j + index_j - neighbourhood 
					ind = int((ind_i*10)+ind_j)
					if ind_i < 0:
						pass
					elif ind_i > (9):
						pass
					elif ind_j > (9):
						pass
					elif ind_j < 0:
						pass
					else:
						W[(ind)] = W[(ind)] + step*(animal-W[(ind)])
						pass



	return W
def epoch_iteration(iterations,animal_list,W,neighbourhood,step,original_neighbourhood):
	for _ in range(iterations):
		W = sequencial_iteration(animal_list,W,int(neighbourhood-2),step)
		neighbourhood = neighbourhood - (original_neighbourhood/iterations)
	return W
def plot_all_data(out):
	plt.ylabel("Y")
	plt.xlabel("X")
	plt.title("All the data")
	megasum = []
	for i in range(10):
		sumr = []
		for j in range(10):
			summa = 0
			sumr.append(summa)
		megasum.append(sumr)
	for i in range(10):
		sumr = []
		for j in range(10):
			summa = 0
			for x in range (349):
				if ((i*10)+j) == out[x][0]:
					megasum[i][j] = megasum[i][j]+1


	x = np.arange(1,11,1)
	y = np.arange(1,11,1)
	xx,yy =np.meshgrid(x,y, sparse=False)
	zz = np.reshape(np.matrix(megasum),(10,10))
	plt.contourf(xx,yy,np.array(zz))
	plt.show()
def plot_data_party(out,party,party_list,label_list):
	megasum = []
	plt.ylabel("Y")
	plt.xlabel("X")
	plt.title(label_list[party])
	for i in range(10):
		sumr = []
		for j in range(10):
			summa = 0
			sumr.append(summa)
		megasum.append(sumr)
	for i in range(10):
		sumr = []
		for j in range(10):
			summa = 0
			for x in range (349):
				if ((i*10)+j) == out[x][0]:
					if party_list[((x))] == party:
						megasum[i][j] = megasum[i][j]+1


	x = np.arange(1,11,1)
	y = np.arange(1,11,1)
	xx,yy =np.meshgrid(x,y, sparse=False)
	zz = np.reshape(np.matrix(megasum),(10,10))
	plt.contourf(xx,yy,np.array(zz))
	plt.show()

def main():
	neighbourhood = 2
	step = 0.2
	iterations = 20
	nodes = 100
	animal_list = np.matrix(read_votes())
	party_list = read_mpparty()
	sex_list = read_sex()
	district_list = read_district()
	W = initialize_weights(nodes,31)
	W = epoch_iteration(iterations,animal_list,W,neighbourhood,step,neighbourhood)
	out = output(animal_list,W)

	plot_all_data(out)
	label_list = ['no party','m', 'fp', 's','v', 'mp','kd','c']
	for party in range(8):
		plot_data_party(out,party,party_list,label_list)
	label_list = ['m','f']
	for sex in range(2):
		plot_data_party(out,sex,sex_list,label_list)
	label_list = ["None","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29"]
	for district in range(29):
		plot_data_party(out,district+1,district_list,label_list)





	#np.meshPlot(xx,yy,np.array(zz))
	


main()