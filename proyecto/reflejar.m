function [] = reflejar(sen,inicio,fin,numMuest)
    vector1 = (inicio-1):fin;%generamos un vector con nmustras elementos para graficar   
    inicioNuevo=(-1*fin)+1;
    finNuevo=1+(-1*inicio);
    
    disp('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa');
    disp(int2str(inicioNuevo-1));
    disp(int2str(finNuevo));
    disp('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa');
    
    for j=1:(numMuest)
        %disp(sen(j+1));
        aux=numMuest-j+2;
        disp(aux);
        senNueva(j)=sen(aux);
    end
    senNueva= [0,senNueva,0];
    disp(senNueva);
  
    vector2 = (inicioNuevo-1):finNuevo;%generamos un vector con nmustras elementos para graficar
    
    disp('------------------');
    disp(senNueva);
    disp(vector2);
    disp('------------------');
    
    function [sen1Cero, sen2Cero, inicio, fin, numMues] = acompleta(sen1, sen2, inicio1, inicio2, fin1, fin2, numMues1, numMues2)
    
    subplot(1,2,1), stem(vector1,sen),title('Senal');
        grid on;
        subplot(1,2,2), stem(vector2,senNueva),title('Senal desplazada');
        grid on;
        