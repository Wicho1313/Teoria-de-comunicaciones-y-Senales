% Funci?n que obtiene una se?al de audio y la almacena en un arreglo de
% enteros
function[senial] = obtenerAudio()
tiempo = 6;
% 8000 muestras / segundo
    recObj = audiorecorder;
    f = msgbox('Grabando audio ... ');
    recordblocking(recObj, tiempo);
    delete(f);
    %g = msgbox('? Fin de la grabaci?n !');
   % pause(1)
   % close(g);

    % Almacenamos la grabacion en un arreglo de enteros
    senial = getaudiodata(recObj);
    % Verificaci?n en consola
    tam= length(senial);
    disp(tam);
end