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
	
def load_spectrum_txt(file_name,skiprows):
	data=np.loadtxt(file_name,skiprows=skiprows)
	
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
def spectrum_compare_fig(spectrum1,spectrum2,save_name):
	label1_name='BHC'
	label2_name='NO_BHC'
	
	fig = plt.figure()
	
	x=np.arange(0.5,150,1)
	
	plt.plot(spectrum1,marker='^',alpha=0.5,label=label1_name,linewidth=0.5,markersize=3)
	plt.plot(spectrum2,marker='^',alpha=0.5,label=label2_name,linewidth=0.5,markersize=3)
	
	plt.title('spectrum')
	plt.legend(loc='upper right')
	#plt.xlabel('')
	#plt.ylabel('')
	plt.savefig(save_name)
	
	plt.close()


#スペクトルを図に表示し、保存
def spectrum_fig(spectrum,save_name,label_name): 
	spectrum=np.array(spectrum)
	
	fig = plt.figure()
	
	x=np.arange(0.5,150,1)
	plt.plot(x,spectrum,marker='^',alpha=0.5,linewidth=0.5,color='blue',markersize=3,label=label_name)
	
	plt.legend(loc='upper right')
	plt.savefig(save_name)
	
	plt.close()

#テキストファイルからスペクトルの割合を抜き出す
def extract_spectrum_txt(text_name):
	#初期化
	line_count=0
	fraction=[]
	for line in open(text_name,"r"):
		line_count += 1 
		if line_count ==1: #一行目は無視
			continue
		data=line.split()
		fraction.append(data[2]) #スペクトルの割合を追加

	return fraction


#平均エネルギーを計算
def mean_energy(file_name):
	Mean=0
	data=np.loadtxt(file_name,skiprows=1)
	for i in range(data.shape[0]):
		Mean+=1000 * (data[i][0]+data[i][1])/2 * data[i][2]
	
	return Mean

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
def mean_energy_fig(mean_energy):
	data_size=10000
	
	x=np.arange(1,data_size+1,1)

	fig=plt.figure()
	
	plt.scatter(x,mean_energy,s=10,marker='^',label='80-140kV')
	
	plt.xlim([1,data_size])
	
	plt.xlabel('spectrum Number')
	plt.ylabel('mean energy')
	
	plt.title('Mean Energy')
	plt.legend(loc='upper left')
	filename='mean_energy.png'
	plt.savefig(filename)
	plt.close()

if __name__=="__main__":	
	spectrum1=load_data_csv_space('../DNN/predict_value/BHC.txt')
	spectrum2=load_data_csv_comma('../DNN/predict_value/NO_BHC.txt')

	savename='compare_BHC.png'
	spectrum_compare_fig(spectrum1,spectrum2,savename)	

	
	"""
	spectrum=load_data_csv_comma('../DNN/training_data/spectrum/10000.csv')
	spectrum_fig(spectrum[276],'276.png','No.276')	
	"""
	

	"""
	for i in range(10000):
		i=i+1
		filename="/mnt/nfs_S65/Takayuki/package_TotalDensityEstimation/SPEKTRspectrum/spectrum10000_normalization/spectrum%d.text" % i
		
		frac=extract_spectrum_txt(filename)
	
		csv_name='10000.csv'
	
		write_csv_a(csv_name,frac)

	"""


	"""
	#平均エネルギーを計算
	mean_energy=np.loadtxt('./mean_energy_file/dataset/10000.csv',delimiter=',')
	mean_energy_fig(mean_energy)
	"""
	
	"""
	#スペクトルを図示
	spectrum=load_data_csv_space('../DNN/predict_value/QQ_predict.csv')
	spectrum_fig(spectrum,'pred_QQ.png','QQ') 
	
	spectrum=load_data_csv_space('../DNN/predict_value/New_predict.csv')
	spectrum_fig(spectrum,'pred_New.png','New') 
	"""


	"""
	#平均エネルギーを計算して図示、csvファイルにまとめる
	mean=[]
	for i in range(10000):
		i=i+1
		file_name='/mnt/nfs_S65/Takayuki/package_TotalDensityEstimation/SPEKTRspectrum/spectrum10000_normalization/spectrum{0}.text'.format(i)
		Mean=mean_energy(file_name)
		mean.append(Mean)
	mean_energy_fig(mean)
	#np.savetxt('mean_energy.csv',mean,fmt='%.6f')
	"""
