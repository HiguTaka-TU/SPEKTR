import numpy as np
import matplotlib.pyplot as plt
import csv

def SPEKTR_Normalization_text():
	lineCount=0
	sum=0
	data0=np.array([],dtype=np.float) #start
	data1=np.array([],dtype=np.float) #end 
	data2=np.array([],dtype=np.float) #spectrum

	for i in range(1,2):
		rawpath='/mnt/nfs_S65/Takayuki/package_TotalDensityEstimation/SPEKTRspectrum/SPEKTRspectrum7500/spectrum%d.text' % i
		a=np.loadtxt(rawpath,skiprows=1)
		for j in range(0,len(a)):
			sum+=a[j][2]

		for j in range(0,len(a)):
			a[j][2]=a[j][2]/sum

		rawpath_out='./spectrum.text'
		with open(rawpath_out,'w') as f:
			f.write("1\n")
			for j in range(0,len(a)):
				f.write("{:.3f} {:.3f} {:.6f}\n".format(a[j][0],a[j][1],a[j][2]))
		#reset
		sum=0
		lineCount=0
		x=[]

def SPEKTR_Normalization_csv():
	csv1_name = './spectrum7500.csv'
	f1=np.loadtxt(csv1_name,delimiter=',')

	spectrum=np.array(f1)
	
	sum=np.sum(spectrum,axis=1)

	spectrum_normalization=np.empty((7500,150))

	for i in range(0,7500):
		spectrum_normalization[i,:]=spectrum[i,:]/sum[i]

	np.savetxt('spectrum_normalization.csv',spectrum_normalization,fmt='%.6f')
