import numpy as np
import matplotlib.pyplot as plt
import csv

data_size=10000

#データの書き込みを行う
def write_csv(csv_name,data,mode): #mode= 'w' or 'a'
	with open(csv_name,mode) as f:
		writer=csv.writer(f)
		writer.writerow(data)

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

if __name__=="__main__":
	for i in range(data_size):
		i = i+1
		input_file='./Spectrum_norm/spectrum_norm%d.txt' % i
		fraction=extract_spectrum_txt(input_file)	
		
		output_file='spectrum_norm_%d.csv' % i
		write_csv(output_file,fraction,'a')
