clc
clear all




disp('ingresa los datos de la señal 1');
[senalM1, numMues1,inicio1,fin1] = creaSenal();
disp('ingresa los datos de la señal 2');
[senalM2, numMues2,inicio2,fin2] = creaSenal();

vector1 = (inicio1-1):fin1;%generamos un vector con nmustras elementos para graficar
vector2 = (inicio2-1):fin2;%generamos un vector con nmustras elementos para graficar
    

disp('introduce la opcion que quieres hacer con las señales');
disp('1 Sumar');
disp('2 Restar');
disp('3 Amplficar/atenuar');
disp('4 Desplazar');
disp('5 Reflejar');
disp('6 Diezmar');
disp('7 Interpolar');
disp('8 Convolucionar ');
opcion = input('');

switch opcion
    case 1
        disp('vamos a sumar las dos señales');
        suma(senalM1,numMues1,inicio1,fin1,senalM2,numMues2,inicio2,fin2);
    case 2
        disp('vamos a restar: sen1-sen2 ');
        resta(senalM1,numMues1,inicio1,fin1,senalM2,numMues2,inicio2,fin2);
    case 3
        disp('vamos a multiplicar por N ');
        n=input('introduce la N');
        [senamp1]=Amplifica(senalM1,n);
        disp(senalM1);
        disp(senamp1);
        disp(vector1);
        [senamp2]=Amplifica(senalM2,n);
        disp(senalM2);
        disp(senamp2);
        disp(vector2);
        subplot(2,2,1), stem(vector1,senalM1),title('Senal 1');
            grid on;
            subplot(2,2,2), stem(vector2,senalM2),title('Senal 2');
            grid on;
            subplot(2,2,3), stem(vector1,senamp1),title('Senal1 amplificada');
            grid on;
            subplot(2,2,4), stem(vector2,senamp2),title('Senal2 amplificada');
            grid on;
    case 4
        senalD=input('cual de las dos señales desea desplazar?');
        
        switch senalD
            case 1
                desplazamiento=input('Desplazar señal 1 X(n+k), introduzca K (negativo o positivo): ');
                desplazar(senalM1,inicio1,fin1,numMues1,desplazamiento)
            case 2
                desplazamiento2=input('Desplazar señal 2 X(n+k), introduzca K (negativo o positivo): ');
                desplazar(senalM2,inicio2,fin2,numMues2,desplazamiento2)
        end
    case 5
        senalR=input('cual de las dos señales desea reflejar?');
        
        switch senalR
            case 1
                reflejar(senalM1,inicio1,fin1,numMues1);
            case 2
                reflejar(senalM2,inicio2,fin2,numMues2);
        end
    case 6
        numeroo=input('introduce el valor de k en x(kn)');
        senalInter=input('cual de las dos señales desea diezmar?');
        
        switch senalInter
            case 1
                diezma(senalM1,inicio1,fin1,numMues1,numeroo);
            case 2
                diezma(senalM2,inicio2,fin2,numMues2,numeroo);
        end
    case 7
         numeroo=input('introduce el valor de k en x(n/k)');
        senalInter=input('cual de las dos señales desea interpolar?');
        
        switch senalInter
            case 1
                interpola(senalM1,inicio1,fin1,numMues1,numeroo);
            case 2
                interpola(senalM2,inicio2,fin2,numMues2,numeroo);
        end
        
    case 8
        convolucion(senalM1,numMues1,inicio1,fin1,senalM2,numMues2,inicio2,fin2);
    case 9
        
end
