function [sen1Cero, sen2Cero, inicio, fin, numMues] = acompleta(sen1, sen2, inicio1, inicio2, fin1, fin2, numMues1, numMues2)
    %vamos a completar con ceros las senales
    if inicio1>inicio2 
        for j=1 : (inicio1-inicio2)
            sen1 = [0,sen1];
            numMues1=numMues1+1;%anadir num de muestras
            inicio1=inicio1-1;%mover el inicio uno a la izquierda
        end
    end
    if inicio2>inicio1 
        for j=1 : (inicio2-inicio1)
            sen2 = [0,sen2];
            numMues2=numMues2+1;%anadir num de muestras
            inicio2=inicio2-1;%mover el inicio uno a la izquierda
        end
    end
    
    if fin2>fin1 
        for j=1 : (fin2-fin1)
            sen1 = [sen1,0];
            numMues1=numMues1+1;%anadir num de muestras
            fin1=fin1+1;%mover el inicio uno a la izquierda
        end
    end
    if fin2<fin1
        for j=1 : (fin1-fin2)
            sen2 = [sen2,0];
            numMues2=numMues2+1;%anadir num de muestras
            fin2=fin2+1;%mover el inicio uno a la izquierda
        end
    end
    
    sen1Cero=sen1;
    sen2Cero=sen2;
    inicio=inicio1-1;
    fin=fin1;
    numMues=numMues1+2;
end