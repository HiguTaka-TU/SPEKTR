# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

#ファイルからスペクトルを読み込み
def load_spectrum_txt(file_name):
	spectrum=np.loadtxt(file_name,skiprows=1)
	
	return spectrum

#スペクトルの合計値を計算
def calc_spectrum_sum(spectrum):
	sum_spectrum=np.sum(spectrum[:,2])

	return sum_spectrum

#正規化したスペクトルを返す
def specturm_normalization(spectrum,sum_spectrum):
	spectrum[:,2]=spectrum[:,2]/sum_spectrum
	
	return spectrum_norm

#正規化したスペクトルをファイルに書き込み	
def write_spectrum(file_name,spectrum_norm):
	with open(file_name,'w') as f:
		f.write("1\n")
		for j in range(len(spectrum_norm)):
			f.write("{:.3f} {:.3f} {:.6f}\n".format(spectrum_norm[j][0],spectrum_norm[j][1],spectrum_norm[j][2]))


def main():
	for i in range(10000):
		input_name='./Spectrum/spectrum%d.text' % i
	
		spectrum=load_spectrum_txt(input_name)
	
		sum_spectrum=calc_spectrum_sum(spectrum)
	
		spectrum_norm=specturm_normalization(spectrum,sum_spectrum)

		output_name='./Specturm_norm/spectrum_norm%d.txt'

		write_spectrum(output_name,spectrum_norm)

if __name__=="__main__":
	main()
