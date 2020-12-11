ii=1;
for k =1:1:10000;%kV 60 types
    kV=randi([80 140]);
    %formatSpec='./spectrum/spectrum%dkV-%d%%-%.2f-%.2f.text';
    formatSpec='./spectrum10000/spectrum%d.text';
    ripple=randi([0 100]); 
    mmAl=rand*9.5+0.5;
    fp=spektrSpectrum(kV,[mmAl,ripple],'TASMICS',0);
    mmCu=rand*0.5;
    fp=spektrBeers(fp,[29 mmCu]);
    M=max(fp);
    fp=fp/M;
    %filename=sprintf(formatSpec,kV,ripple,mmAl,mmCu);
    filename=sprintf(formatSpec,ii);
    file_spectrum=fopen(filename,'w');
    fprintf(file_spectrum,'1\n')
    for j =1:1:150;
        e=fp(j,1);%element
        s=0.001*(j-1);%start
        l=0.001*j;%last
        fprintf(file_spectrum,'%1.3f %1.3f %f\n',s,l,e);
    end %fprintfend   
    plot(fp,'k')
    hold on
    fclose(file_spectrum);

    file_data=fopen('data.txt','a');
    fprintf(file_data,'%3d,%3d,%2.3f,%1.3f\n',kV,ripple,mmAl,mmCu);
    fclose(file_data);
    
    %fprintf(file,'%f\n',fp);
    %type spectrum1.txt
    ii=ii+1;
end %kV end
