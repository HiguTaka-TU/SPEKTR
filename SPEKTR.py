import numpy as np
import matplotlib.pyplot as plt
import csv

def SPEKTR_fig_text(rawpath):
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

def SPEKTR_fig_csv():
	csv_name = './spectrum7500_normalization.csv'

	f1=np.loadtxt(csv_name,delimiter=' ')

	spectrum=np.array(f1)

	fig = plt.figure()
	i=0 
	plt.plot(spectrum[i])
	filename='./spectrum.png'
	plt.savefig(filename)
	plt.close()

def SPEKTR_TEXTtoCSV():
	for i in range(1,100):
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


		with open('spectrum.csv','a') as f:
			writer=csv.writer(f)
			writer.writerow(x)
		
		x=[] #reset





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

def B3FQQNew_Pred_fig():
	lineCount=0
	x=[]
	fig=plt.figure()
	csv1_name = '/mnt/nfs_S65/Takayuki/SpectrumEstimation/CrossEntropy_Zscore/New_estimate/B3F.txt'
	csv2_name = '/mnt/nfs_S65/Takayuki/SpectrumEstimation/CrossEntropy_Zscore/New_estimate/QQ.txt'
	csv3_name = '/mnt/nfs_S65/Takayuki/SpectrumEstimation/CrossEntropy_Zscore/New_estimate/New.txt'

	f1=np.loadtxt(csv1_name,delimiter=' ')
	f2=np.loadtxt(csv2_name,delimiter=' ')
	f3=np.loadtxt(csv3_name,delimiter=' ')

	B3F=np.array(f1)
	QQ=np.array(f2)
	New=np.array(f3)

	plt.plot(B3F,label="B3F")
	plt.plot(QQ,label="QQ")
	plt.plot(New,label="New")
	
	plt.title('spectrum_pred')
	plt.legend(loc='upper right')
	#plt.xlabel('')
	#plt.ylabel('')
	fig.savefig("NewEstimation_check.png")

def MeanEnergy():
	Mean_Energy=[]
	for i in range(1,7501):
		rawpath="/mnt/nfs_S65/Takayuki/package_TotalDensityEstimation/SPEKTRspectrum/SPEKTRspectrum7500_normalization/spectrum_normalization%d.text" % i
		Mean=0
		data=np.loadtxt(rawpath,skiprows=1)
		for i in range(data.shape[0]):
			Mean+=1000 * (data[i][0]+data[i][1])/2 * data[i][2]
		print(Mean)
		Mean_Energy.append(Mean)
	
	with open('MeanEnergy.csv','a') as f:
		writer=csv.writer(f)
		writer.writerow(Mean_Energy)
MeanEnergy()
