function[sen,numMues,inicio,fin] = convolucion(sen1,numMues1,inicio1,fin1,sen2,numMues2,inicio2,fin2)
    [sen11,sen22,inicio,fin,numMues]=acompleta(sen1,sen2,inicio1,inicio2,fin1,fin2,numMues1,numMues2);
    disp('aaaaaaaaaaa Senales recibidas aaaaaaaaaaaaaa');
    disp(sen2);
    disp(sen1);
    disp('aaaaaaaaaaa Despues de acompletar aaaaaaaaaaaaaaa');
    disp(sen11);
    disp(sen22);
    disp(conv(sen11,sen22))
    disp('ssssssssssssssssssssssssss');
    
    vector1 = (inicio1-1):fin1;%generamos un vector con nmustras elementos para graficar   
    vector2 = (inicio2-1):fin2;%generamos un vector con nmustras elementos para graficar   
    sen=conv(sen11,sen22);
    
    inicioNuevo=inicio+inicio;
    finNuevo=fin+fin;
    
    numMuesNuevo=numMues+numMues-1;
    
        
    tam=size(sen);
    vector3 = inicioNuevo:finNuevo;%generamos un vector con nmustras elementos para graficar   
    
    disp('------------------------------');
    disp(finNuevo);
    disp(size(sen));
    disp('------------------------------');
    disp(sen);
    disp(vector3);
    disp('-------------------------------');
    disp(size(sen));
    disp(size(vector3));
    
    aux1=size(sen);
    aux2=size(vector3);
    if aux1(2)~=aux2(2)
         vector3 = inicioNuevo:finNuevo+1;%generamos un vector con nmustras elementos para graficar   
    end
    disp('-------------------------------');
    
    subplot(1,3,1), stem(vector1,sen1),title('Senal');
        grid on;
        subplot(1,3,2), stem(vector2,sen2),title('Senal 2');
        grid on;
        subplot(1,3,3), stem(vector3,sen),title('convolucion');
        grid on;