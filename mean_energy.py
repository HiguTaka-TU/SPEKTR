import numpy as np
import matplotlib.pyplot as plt

#mean_energyは空の配列 mean_energy=[]
def mean_energy(file_name,mean_energy):
	mean=0
	data=np.loadtxt(file_name,skiprows=1)
	print(data)
	for i in range(data.shape[0]):
		mean+=1000 * (data[i][0]+data[i][1])/2 * data[i][2]
	mean_energy.append(mean)


	write_csv('mean_energy.csv',mean_energy,'a')

#平均エネルギーのプロット
def mean_energy_fig():
	x=np.arange(1,10000+1)

	fig=plt.figure()
	
	plt.scatter(x,MeanEnergy,s=10,marker='^',label='81-140kV')
	
	plt.xlabel('Spectrum Number')
	plt.ylabel('Mean Energy')
	
	plt.title('Mean Energy')
	plt.legend(loc='upper left')
	filename='mean_energy.png'
	plt.savefig(filename)
	plt.close()
