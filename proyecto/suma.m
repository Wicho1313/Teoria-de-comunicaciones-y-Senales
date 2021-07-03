function[sen,numMues,inicio,fin] = suma(sen1,numMues1,inicio1,fin1,sen2,numMues2,inicio2,fin2)
    [sen1,sen2,inicio,fin,numMues]=acompleta(sen1,sen2,inicio1,inicio2,fin1,fin2,numMues1,numMues2);
    vector = linspace(inicio,fin, numMues);%generamos un vector con nmustras elementos para graficar
    disp(vector);
    disp('senal 1');
    disp(sen1);
    disp('senal 12');
    disp(sen2);
    suma= sen1+sen2;
    sen=suma;
    disp(suma);
    subplot(1,3,1), stem(vector,sen1),title('Senal 1');
        grid on;
        subplot(1,3,2), stem(vector,sen2),title('Senal 2');
        grid on;
        subplot(1,3,3), stem(vector,suma),title('Suma de las senales');
        grid on;