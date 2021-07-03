function [senNueva,numMuesF,inicioN,finN] = diezma(sen,inicio,fin,numMues,numero)
    %inicio -4
    %mod(-4,2)
        aux2=1;
    disp('inicio');
    disp(inicio);
    disp('fin');
    disp(fin);
    disp('nnumero de muestras');
    disp(numMues);
    for j=1: (numMues)
        disp(sen(j))
        aux=mod(inicio+j-1,numero);

        if aux==0
            senNueva(aux2)=sen(j+1);
            aux2=aux2+1;
        end
    end
    aux3=length(senNueva);
    inicioN = -1*(aux3-1)/2;
    finN=(aux3-1)/2;
     
    vector1 = (inicio-1):fin;%generamos un vector con nmustras elementos para graficar   
    vector2 = (inicioN):finN;%generamos un vector con nmustras elementos para graficar   
    
    
    
    subplot(1,2,1), stem(vector1,sen),title('Senal');
        grid on;
        subplot(1,2,2), stem(vector2,senNueva),title('Senal interpolada');
        grid on;
end