
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
	z_list = []
	for i in range(10):
		sumr = []
		for j in range(10):
			summa = 0
			sumr.append(summa)
		z_list.append(sumr)
	for i in range(10):
		for j in range(10):
			summa = 0
			for person in range (349):
				if ((i*10)+j) == out[person][0]:
					z_list[i][j] = z_list[i][j]+1


	x = np.arange(1,11,1)
	y = np.arange(1,11,1)
	xx,yy =np.meshgrid(x,y, sparse=False)
	zz = np.reshape(np.matrix(z_list),(10,10))
	cs = plt.contourf(xx,yy,np.array(zz))
	cbar = plt.colorbar(cs)
def plot_data_party(out,party,party_list,label_list):
	plt.subplot(330+party+2)
	z_list = []
	plt.ylabel("Y")
	plt.xlabel("X")
	plt.title(label_list[party])
	for i in range(10):
		sumr = []
		for j in range(10):
			summa = 0
			sumr.append(summa)
		z_list.append(sumr)
	for i in range(10):
		for j in range(10):
			summa = 0
			for person in range (349):
				if ((i*10)+j) == out[person][0]:
					if party_list[((person))] == party:
						z_list[i][j] = z_list[i][j]+1


	x = np.arange(1,11,1)
	y = np.arange(1,11,1)
	xx,yy =np.meshgrid(x,y, sparse=False)
	zz = np.reshape(np.matrix(z_list),(10,10))
	cs = plt.contourf(xx,yy,np.array(zz))
	cbar = plt.colorbar(cs)


def plot_data_gender(out,gender,gender_list,label_list):
	plt.subplot(310+gender+2)
	z_list = []
	plt.ylabel("Y")
	plt.xlabel("X")
	plt.title(label_list[gender])
	for i in range(10):
		sumr = []
		for j in range(10):
			summa = 0
			sumr.append(summa)
		z_list.append(sumr)
	for i in range(10):
		for j in range(10):
			summa = 0
			for person in range (349):
				if ((i*10)+j) == out[person][0]:
					if gender_list[((person))] == gender:
						z_list[i][j] = z_list[i][j]+1


	x = np.arange(1,11,1)
	y = np.arange(1,11,1)
	xx,yy =np.meshgrid(x,y, sparse=False)
	zz = np.reshape(np.matrix(z_list),(10,10))
	cs = plt.contourf(xx,yy,np.array(zz))
	cbar = plt.colorbar(cs)
	
def plot_data_district(out,district,district_list,label_list):
	plt.subplot(6,5,0+district+2)
	z_list = []
	plt.ylabel("Y")
	plt.xlabel("X")
	plt.title(label_list[district])
	for i in range(10):
		sumr = []
		for j in range(10):
			summa = 0
			sumr.append(summa)
		z_list.append(sumr)
	for i in range(10):
		for j in range(10):
			summa = 0
			for x in range (349):
				if ((i*10)+j) == out[x][0]:
					if district_list[((x))] == district+1:
						z_list[i][j] = z_list[i][j]+1


	x = np.arange(1,11,1)
	y = np.arange(1,11,1)
	xx,yy =np.meshgrid(x,y, sparse=False)
	zz = np.reshape(np.matrix(z_list),(10,10))
	cs = plt.contourf(xx,yy,np.array(zz))
	cbar = plt.colorbar(cs)
	

def main():
	neighbourhood = 2
	step = 0.05
	iterations = 100
	nodes = 100
	animal_list = np.matrix(read_votes())
	party_list = read_mpparty()
	sex_list = read_sex()
	district_list = read_district()
	W = initialize_weights(nodes,31)
	W = epoch_iteration(iterations,animal_list,W,neighbourhood,step,neighbourhood)
	out = output(animal_list,W)
	plt.subplot(331)
	plot_all_data(out)
	label_list = ['no party','Moderaterna', 'Folkpartiet', 'Socialdemokraterna','Vänsterpartiet', 'Miljöpartiet','Kristemokraterna','Centern']
	for party in range(8):
		plot_data_party(out,party,party_list,label_list)

	label_list = ['Male','Female']
	plt.show()

	plt.subplot(311)
	plot_all_data(out)
	for sex in range(2):
		plot_data_gender(out,sex,sex_list,label_list)
	plt.show()
	plt.subplot(651)
	plot_all_data(out)
	
	label_list = ["District 1","District 2","District 3","District 4","District 5","District 6","District 7","District 8","District 9","District 10","District 11","District 12","District 13","District 14","District 15","District 16","District 17","District 18","District 19","District 20","District 21","District 22","District 23","District 24","District 25","District 26","District 27","District 28","District 29"]
	for district in range(29):
		plot_data_district(out,district,district_list,label_list)
	plt.show()





	#np.meshPlot(xx,yy,np.array(zz))
	


main()