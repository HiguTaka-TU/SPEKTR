# X線スペクトル生成
![図1](https://user-images.githubusercontent.com/73208280/101884257-bece4d80-3bdb-11eb-9b1a-b8638c27d6c6.png)  
SPEKTR3.0を用いてX線スペクトルを生成します。

## スペクトルを生成
1.以下のリンクよりSPEKTR3.0をダウンロードします。  
https://istar.jhu.edu/downloads/  

2.ダウンロードしたSPEKTR3.0のSpektr Codeのディレクトリにgenerate_spectrum.mを置き、"Spectrum"というディレクトリを作成しておく  
MATLABを起動し、スペクトルを生成  
`$generate_spectrum`    
デフォルトでは10000のスペクトルが生成される  

## スペクトルを正規化  
スペクトルの各ビンの和を１にする  
"Spectrum_norm"というディレクトリを作成し、以下コマンドを実行く   
`$python normalization.py`  
これで正規化されたスペクトルの完成である  

## X線の平均エネルギーを図示する  
`$python mean_energy.py`  
各スペクトルの平均エネルギーをプロットしたmean_energy.png、CSVファイルにまとめたmean_energy.csvが生成される

## CSVファイルにまとめる  
データセットとしてまとめて取り扱うためCSVファイルに保存する  
`$python make_dataset.py`  
生成されたスペクトルを格納したCSVファイルspectrum_norm_{data_size}.csvが生成される  
＊{data_size}にはスペクトルの個数が入る  

