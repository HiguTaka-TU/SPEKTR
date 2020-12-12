import numpy as np
import matplotlib.pyplot as plt
import csv

data_size=1

#データの書き込みを行う
def write_csv(csv_name,data,mode): #mode= 'w' or 'a'
	with open(csv_name,mode) as f:
		writer=csv.writer(f)
		writer.writerow(data)

#mean_energyは空の配列 mean_energy=[]
def mean_energy(file_name,mean_energy):
	mean=0
	data=np.loadtxt(file_name,skiprows=1)
	for i in range(data.shape[0]):
		mean+=1000 * (data[i][0]+data[i][1])/2 * data[i][2]
	mean_energy.append(mean)

	write_csv('mean_energy.csv',mean_energy,'a')

	return mean_energy

#平均エネルギーのプロット
def mean_energy_fig(mean_energy):
	x=np.arange(1,data_size+1)

	fig=plt.figure()
	
	plt.scatter(x,mean_energy,s=10,marker='^',label='80-140kV')
	
	plt.xlabel('Spectrum Number')
	plt.ylabel('Mean Energy')
	
	plt.title('Mean Energy')
	plt.legend(loc='upper left')
	filename='mean_energy.png'
	plt.savefig(filename)
	plt.close()

if __name__=="__main__":
	for i in range(data_size):
		i=i+1
		
		file_name='Spectrum_norm/spectrum_norm%d.txt' % i
		
		mean=[]
		mean_energy(file_name,mean)
	
		mean_energy_fig(mean)
