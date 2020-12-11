# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import csv

#データの読み込みを行う
def load_data_csv_space(file_name):
	data=np.loadtxt(file_name,delimiter=' ')
	
	return data

def load_data_csv_comma(file_name):
	data=np.loadtxt(file_name,delimiter=',')
	
	return data
	
def load_spectrum_txt(file_name):
	data=np.loadtxt(file_name,skiprows=1)
	
	return data

#データの書き込みを行う
def write_csv_a(csv_name,data):
	with open(csv_name,'a') as f:
		writer=csv.writer(f)
		writer.writerow(data)
		
def write_csv_w(csv_name,data):
	with open(csv_name,'w') as f:
		writer=csv.writer(f)
		writer.writerow(data)

#２つのスペクトルの比較を行い、図に表示
def SPEKTR_compare_fig(spectrum1,specturm2):
	label1_name='Cu_mm'
	label2_name='Al_mm'
	save_name='./spectrum_compare.png'
	
	fig = plt.figure()
	
	plt.plot(spectrum1[:,2],color="orange",label=label1_name,linewidth=1)
	plt.plot(spectrum2[:,2],color="blue",label=label2_name,linewidth=1)
	
	plt.title('spectrum')
	plt.legend(loc='upper right')
	#plt.xlabel('')
	#plt.ylabel('')
	plt.savefig(save_name)
	
	plt.close()


#スペクトルを図に表示し、保存
def spectrum_fig(spectrum):
	kV=140
	save_name='./spectrum_%dkV.png' % kV
	label_name='%dkV' % kV

	spectrum=np.array(spectrum)
	
	fig = plt.figure()
	
	x=np.arange(0.5,150,1)
	
	plt.plot(x,spectrum[i,:],marker='^',alpha=0.5,linewidth=0.5,color='blue',markersize=3,label=label_name)
	
	plt.legend(loc='upper right')
	plt.savefig(filename)
	
	plt.close()

#テキストファイルからスペクトルの割合を抜き出す
def extract_spectrum_txt(input_file):
	#初期化
	line_count=0
	fraction=[]
	for line in open(input_file,"r"):
		line_count += 1 
		if line_count ==1: #一行目は無視
			continue
		data=line.split()
		fraction.append(data[2]) #スペクトルの割合を追加

	return fraction


#mean_energyは空の配列 mean_energy=[]
def mean_energy(file_name,mean_energy):
	for i in range(1,10000):
		Mean=0
		data=np.loadtxt(file_name,skiprows=1)
		for i in range(data.shape[0]):
			Mean+=1000 * (data[i][0]+data[i][1])/2 * data[i][2]
		mean_energy.append(Mean)

#平均エネルギーの比較
def mean_energy_compare():
	fig=plt.figure()
	x1=np.arange(0.1,10.1,0.1)
	x2=np.arange(0.1,5.1,0.1)
	
	
	plt.scatter(x1,f1,marker='^',color='b',label='Al0-10mm')
	plt.scatter(x2,f2,marker='^',color='orange',label='Cu0-5mm')
	
	plt.xlabel('filter thickness')
	plt.ylabel('Mean Energy')
	filename='MeanEnergy.png'
	plt.legend(loc='upper right')
	plt.savefig(filename)


#平均エネルギーのプロット
def mean_energy_fig():
	x=np.arange(1,10000,1)

	fig=plt.figure()
	
	
	plt.scatter(x,MeanEnergy,s=10,marker='^',label='81-140kV')
	
	plt.xlabel('spectrum Number')
	plt.ylabel('MeanEnergy')
	
	plt.title('MeanEnergy')
	plt.legend(loc='upper left')
	filename='MeanEnergy.png'
	plt.savefig(filename)
	plt.close()

if __name__=="__main__":
	for i in range(10000):
		i = i+1
		path_in='../../SPEKTR3.0/SpektrCode/spectrum10000/spectrum%d.text' % i
		fraction=extract_spectrum_txt(path_in)	
		
		path_out='10000.csv'
		write_csv_a(path_out,fraction)
		print(i)
