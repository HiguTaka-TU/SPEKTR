# X線スペクトル生成
![図1](https://user-images.githubusercontent.com/73208280/101884257-bece4d80-3bdb-11eb-9b1a-b8638c27d6c6.png)  
SPEKTR3.0を用いてX線スペクトルを生成します。

## SPEKTRをダウンロード
1.以下のリンクよりSPEKTR3.0をダウンロードします。  
https://istar.jhu.edu/downloads/  

<<<<<<< HEAD
2.ダウンロードしたSPEKTR3.0のSpektr Codeのディレクトリにgenerate_spectrum.mを置き、MATLABを起動  
あらかじめ"Spectrum"というディレクトリを作成しておき、スペクトルを生成する  
`$generate_spectrum`    
デフォルトでは10000のスペクトルが生成される

3.スペクトルの各ビンの和を１にする  
"Spectrum_norm"というディレクトリを作成し、以下コマンドを実行
`$python normalization.py`
=======
2.ダウンロードしたSPEKTR3.0のSpektr Codeのディレクトリにgenerate_spectrum.mを置き、MATLABを起動  
あらかじめ"Spectrum"というディレクトリを作成しておき、スペクトルを生成する  
`$generate_spectrum`    
デフォルトでは10000のスペクトルが生成される
>>>>>>> 7eb5dcb572e8000d298c41858d00650b1516ddd4
