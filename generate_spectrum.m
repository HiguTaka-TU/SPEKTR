ii=1;
for k =1:1:10000; %10000種類のスペクトルを生成
    kV=randi([80 140]); %80kV~140kV
    
    formatSpec='./spectrum100000/spectrum%d.text'; % file name
    
    ripple=randi([0 100]); %ripple 0~100%
    
    mmAl=rand*9.5+0.5; % Al 0.5~10 mm
    fp=spektrSpectrum(kV,[mmAl,ripple],'TASMICS',0); %スペクトルを生成
    
    mmCu=rand*0.5; % Cu 0~0.5 mm
    fp=spektrBeers(fp,[29 mmCu]); % Cuフィルタを付加

    M=max(fp); % 最大値を取得
    fp=fp/M; % 最大値を1に正規化
    
    filename=sprintf(formatSpec,ii); 
    file_spectrum=fopen(filename,'w');
    fprintf(file_spectrum,'1\n'); % ファイルの1行目に"1"を入力

    for j =1:1:150; %最大150keVまで
        e=fp(j,1);% 割合
        s=0.001*(j-1);% 区間の初め
        l=0.001*j;% 区間の終わり

        fprintf(file_spectrum,'%1.3f %1.3f %f\n',s,l,e);
    end %fprintfend   

    fclose(file_spectrum);

    %kV,ripple,Al,Cu filter の情報を保存しておく
    file_data=fopen('data.txt','a'); 
    fprintf(file_data,'%3d,%3d,%2.3f,%1.3f\n',kV,ripple,mmAl,mmCu);
    fclose(file_data);
    
    ii=ii+1;
end %kV end
