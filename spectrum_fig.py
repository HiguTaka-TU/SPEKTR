# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import csv

#ファイルのタイプを選ぶ
#file_type='csv'
file_type='text' #or 'txt'

def spectrum_fig(spectrum,label_name):
	x=np.arange(0.5,150,1)
	
	plt.plot(x,spectrum,marker='^',alpha=0.5,label=label_name,linewidth=0.5,markersize=3)

def fig_setting():
	plt.xlabel('Energy(keV)')
	plt.ylabel('Normalized Intensity')
	
	plt.title('Spectrum')
	plt.legend(loc='upper right')

if __name__=="__main__":
	fig=plt.figure()

	#プロットしたいスペクトルのファイルとラベルの名前を入力（いくつでもOK!）
	file_label={'./Spectrum_norm/spectrum_norm1.text':'True_Spectrum', './Spectrum_norm/spectrum_norm2.text':'Est_Spectrum'}

	for  f,l in file_label.items():
		if file_type=='csv':
			spectrum=np.loadtxt(f,delimiter=',')
		
			spectrum_fig(spectrum,l)

		elif file_type=='text':
			spectrum=np.loadtxt(f,skiprows=1)

			spectrum_fig(spectrum[:,2],l)
	
	fig_setting()
	
	save_name='compare_spectrum.png'

	plt.savefig(save_name)
	plt.close()
