import numpy as np
import matplotlib.pyplot as plt
import csv

def SPEKTR_Normalization():
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

SPEKTR_Normalization()
