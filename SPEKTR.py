# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import csv

#データの書き込みを行う
def write_csv(csv_name,data,mode): #mode= 'w' or 'a'
	with open(csv_name,mode) as f:
		writer=csv.writer(f)
		writer.writerow(data)

#２つのスペクトルの比較を行い、図に表示
def spectrum_compare_fig(spectrum1,spectrum2,save_name):
	label1_name='Cu_mm'
	label2_name='Al_mm'
	save_name='./spectrum_compare.png'	

	fig = plt.figure()
	
	
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
	kV=140
	save_name='./spectrum_%dkV.png' % kV
	label_name='%dkV' % kV

	spectrum=np.array(spectrum)
	
	fig = plt.figure()
	
	x=np.arange(0.5,150,1)
	plt.plot(x,spectrum[i,:],marker='^',alpha=0.5,linewidth=0.5,color='blue',markersize=3,label=label_name)
	
	plt.legend(loc='upper right')
	plt.savefig(file_name)
	
	plt.close()


if __name__=="__main__":
	"""
	for i in range(10000):
		i = i+1
		path_in='../../SPEKTR3.0/SpektrCode/spectrum10000/spectrum%d.text' % i
		fraction=extract_spectrum_txt(path_in)	
		
		path_out='10000.csv'
		write_csv_a(path_out,fraction)
		print(i)
	"""
