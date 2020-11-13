# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import csv

import SPEKTR

#スペクトルの合計値を計算
def calc_spectrum_sum(spectrum):
	sum_spectrum=np.sum(spectrum[:,2])

	return sum_spectrum

#正規化したスペクトルを返す
def specturm_normalization(spectrum,sum_spectrum):
	spectrum[:,2]=spectrum[:,2]/sum_spectrum
	return spectrum

#正規化したスペクトルをファイルに書き込み	
def write_spectrum(file_name,spectrum_norm):
	with open(file_name,'w') as f:
		f.write("1\n")
		for j in range(len(spectrum_norm)):
			f.write("{:.3f} {:.3f} {:.6f}\n".format(spectrum_norm[j][0],spectrum_norm[j][1],spectrum_norm[j][2]))

#csvファイルに格納されたスペクトルを正規化する
def spectrum_normalization_from_csv(data):
	spectrum=np.array(data)
	
	sum_spectrum=np.sum(spectrum,axis=1)

	spectrum_norm=np.empty_like(spectrum)

	for i in range(spectrum_norm.shape[0]):
		spectrum_norm[i,:]=spectrum[i,:]/sum_spectrum[i]

	np.savetxt('spectrum_normalization.csv',spectrum_normalization,fmt='%.6f')

def main():
	file_name='/mnt/nfs_S65/Takayuki/package_TotalDensityEstimation/SPEKTRspectrum/SPEKTRspectrum7500/spectrum1.text'
	
	spectrum=SPEKTR.load_spectrum_txt(file_name)
	
	sum_spectrum=calc_spectrum_sum(spectrum)
	
	spectrum_norm=specturm_normalization(spectrum,sum_spectrum)

	file_name='1.txt'

	write_spectrum(file_name,spectrum_norm)

if __name__=="__main__":
	main()
