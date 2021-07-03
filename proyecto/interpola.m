function [senNueva,numMues,inicioN,finN] = interpola(sen,inicio,fin,numMues,numero)
    %nuevoInicio= inicio *numero;
    muestrasNuevas= numMues*numero-(numero-1);
    aux=1;
    for j=1:(numMues)
        for h = 1:(numero)
         senNueva(aux) =sen(j+1);
         aux=aux+1;
        end
    end
    disp(senNueva);
    inicioN=inicio*numero;
    finN =inicio+muestrasNuevas-1;
    disp(inicioN);
    disp(finN);
    
    %anadimos los ceros
    
    senNueva=[0,senNueva,0];
    finN=finN+1;
    inicioN=inicioN-1;
    
    vector1 = (inicio-1):fin;%generamos un vector con nmustras elementos para graficar   
    vector2 = (inicioN):finN;%generamos un vector con nmustras elementos para graficar   
    
    
    disp('qqqqqqqqqqqqqqqqqqqqqqqqqq');
    disp(sen);
    disp(vector1);
    disp('qqqqqqqqqqqqqqqqqqqqqqqqqq');
    
    disp('eeeeeeeeeeeeeeeeeeeeeeeee');
    disp(senNueva);
    disp(vector2);
    disp('eeeeeeeeeeeeeeeeeeeeeeeee');
   
    
     subplot(1,2,1), stem(vector1,sen),title('Senal');
        grid on;
        subplot(1,2,2), stem(vector2,senNueva),title('Senal interpolada');
        grid on;