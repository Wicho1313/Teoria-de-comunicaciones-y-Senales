function [] = desplazar(sen,inicio,fin,numMuest,desplazamiento)
    vector1 = (inicio-1):fin;%generamos un vector con nmustras elementos para graficar   
    inicio = inicio-desplazamiento;
    fin = fin-desplazamiento;
    %for j=0:(numMuest-1)
    %    senNueva(inicio+j)=sen(inicio+j)
    %end
    vector2 = (inicio-1):fin;%generamos un vector con nmustras elementos para graficar
    subplot(1,2,1), stem(vector1,sen),title('Senal');
        grid on;
        subplot(1,2,2), stem(vector2,sen),title('Senal desplazada');
        grid on;
        