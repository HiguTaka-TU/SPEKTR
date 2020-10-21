import numpy as np
import matplotlib.pyplot as plt
import csv

def SPEKTR_fig(rawpath):
	lineCount=0
	x=[]
	fig = plt.figure()
	for line in open(rawpath,"r"):
		lineCount += 1
		if lineCount ==1:
			continue
		data=line.split()
		x.append(data[2])
	plt.plot(x,color="blue")
	lineCount=0

	x=[] #reset

	plt.title('spectrum')
	#plt.legend(loc='lower right')
	#plt.xlabel('')
	#plt.ylabel('')
	filename='./spectrum.png'
	plt.savefig(filename)
	plt.close()


def NearestSpectrum_fig(rawpath):
	lineCount=0
	x=[]
	fig=plt.figure()
	for line in open(rawpath,"r"):
		lineCount += 1
		if lineCount ==1:
			continue
		data=line.split()
		x.append(data[2])
	if i==1:
		plt.plot(x,color="blue",label="No.1")
	if i==2:
		plt.plot(x,color="red",label="No.2")
	if i==3:
		plt.plot(x,color="green",label="No.3")
	lineCount=0

	x=[]
	plt.title('spectrum')
	plt.legend(loc='upper right')
	#plt.xlabel('')
	#plt.ylabel('')
	plt.savefig()
	filename='nearlySpectrum'
	plt.savefig(filename)
	plt.close()
#rawpath="/mnt/nfs_S65/Takayuki/package_TotalDensityEstimation/SPEKTRspectrum/SPEKTRspectrum7500/spectrum1.text"
#NearestSpectrum_fig(rawpath)
