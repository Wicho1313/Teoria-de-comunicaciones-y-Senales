function[senal,numMues,inicio,fin] = creaSenal()
    numMues = input('Introduce el numero de muestras en la señal: ');
    inicio = input('en que N va a empezar la muestra? ');
    fin = inicio + numMues;
    % vamos a crear la senal
    senal(1)= 0;
        for j=2: (numMues+1)
            chr=int2str(inicio+j-2);
            palabra=strcat('ingrese el valor de n[', chr, ']');
            senal(j)=input(palabra);
        end
    senal(numMues+2) = 0
end