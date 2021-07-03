# -*- coding: utf-8 -*-
"""
    Se ingresan X[n] y h[n] especificando el centro con un 
    asterísco después del centro.
    Si no se especifica el centro, la mitad del arreglo se 
    establece por defecto.
"""

#Se importan librerías necesarias para graficar
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
#Para la interfaz gráfica
from tkinter import *
#Para expresiones regulares
import re

#Ventana de la aplicación
root = Tk()
root.title("Convolucion Discreta")
myFrame = Frame(root, width = 500, height = 520)
myFrame.pack()
labelTitle = Label(myFrame, text="Convolucion Discreta", font=("Quicksand",18))
labelTitle.place(x=120,y=10)
labelIns = Label(myFrame,text="Indicar el centro de la funcion con el simbolo '*'",font=("Quicksand",14))
labelIns.place(x=30, y=50)

#Funciones
def whereIsCenter(list):
    indice = 0
    while indice < len(list):
        if '*' in list[indice]:
            return indice
        indice += 1
    return 0


def convertFunc(list):
    indice = 0
    while indice < len(list):
        if '*' in list[indice]:
            list[indice] = list[indice].replace('*','')
        indice += 1
    return list


"""
Recibe: list, (int)center,Gi,Gf
            - G(n) : Elementos de la funcion
            - Center G(n): Elemento central de la funcion
            - Gi : índice de inicio donde comienza la funcion 
            - Gf : índice final donde comienza la funcion          
"""
def infoGn(list,center,Gi,Gf):
    print("G(n) = ",list)
    print("Center G(n): ",center)
    print("Gi: ",Gi)
    print("Gf: ",Gf)

"""
Rango del grafico: Esta función devuelve Xi, índice inicial, y Xf, índice final.
        En otras palabras, indica desde dónde comienza la función,
        y de donde termina
Recibe: list, (int)center
Retorna: rango
"""
def rangeToGraph(list,int):
    Gi = getGi(list,int)  #Xi : Inicio de X(n)
    Gf = getGf(list,int)  #Xf : Fin de X(n)
    
    return np.arange(Gi,Gf)


"""
ObtenerGi: Esta función devuelve el Xi, índice inicial
Recibe (list)Xn, (int)center
Retorna: Gi: índice inicial
"""
def getGi(Xn,center):
    Gi = 0
    if center!=0:
        while Gi < center:         #Vemos desde donde inicia la funcion X(n)
            Gi += 1
        Gi = (-1)*Gi
    else:
        Gi = 0
    
    return Gi

"""
Obtener Gf: Esta función devuelve el índice final Xf
Recibe: (list)Xn, (int)center
Retorna: Gi: índice final
"""
def getGf(Xn,center):
     return len(Xn)-center
     

#Obtener datos de entrada para convolucionar

Xn = []
Hn = []
entradaXn = StringVar()
entradaHn = StringVar()

entradaNx = StringVar()
entradaNh = StringVar()

labelXn = Label(myFrame, text="Introduce X(n):", font=("Quicksand",12))
labelXn.place(x=10, y=120)
txtXn = Entry(myFrame,width = 57,textvariable = entradaXn )
txtXn.place(x=10,y=140)

labelHn = Label(myFrame, text="Introduce h(n):", font=("Quicksand",12))

txtHn = Entry(myFrame,width = 57,textvariable = entradaHn)

labelNx = Label(root,text="Nx : ",font=("Quicksand",12))
txtNx = Entry(myFrame,width = 10,textvariable = entradaNx,state='disabled')

labelNh = Label(root,text="Nh : ",font=("Quicksand",12))
txtNh = Entry(myFrame,width = 10,textvariable = entradaNh, state='disabled')

labelNx.place(x=10, y=170)
txtNx.place(x=50, y=170)

labelNh.place(x=10, y=260)
txtNh.place(x=50, y=260)

lablelConv = Label(root,text="",font=("Quicksand",12))

buttonCal = Button(root,text="Calcular",font=("Quicksand",12),command=lambda:calculaConv(txtXn.get(),txtHn.get()))

buttonLimp = Button(root,text="Limpiar",font=("Quicksand",12),command=lambda:limpiar())

buttonGrafS = Button(root,text="Salida",font=("Quicksand",12),command=lambda:graficaSalida(calculaConv(txtXn.get(),txtHn.get())))

buttonGrafE = Button(root,text="Entrada",font=("Quicksand",12),command=lambda:graficaIn(txtXn.get(),txtHn.get()))


labelHn.place(x=10, y=210)
txtHn.place(x=10,y=230)
lablelConv.place(x=10,y=340)
buttonCal.place(x=30,y=300)
buttonLimp.place(x=130,y=300)
buttonGrafS.place(x=230,y=300)
buttonGrafE.place(x=320,y=300)
# ==============================================


#Xn = input("X[n]: ").split(",")
#Hn = input("H[n]: ").split(",")


#Se obtiene el centro de la función
centerX = whereIsCenter(Xn)
centerH = whereIsCenter(Hn)

if(centerX==0):
    centerX = (int)(len(Xn)/2)   
if(centerH==0):
    centerH = (int)(len(Hn)/2)
    
Xi = getGi(Xn,centerX)  #Xi : Inicio X(n)
Xf = getGf(Xn,centerX)  #Xf : Fin X(n)
Hi = getGi(Hn,centerH)  #Hi : Inicio H(n)
Hf = getGf(Hn,centerH)  #Hf : Fin H(n)

rangeXn = rangeToGraph(Xn,centerX)  #Obteniendo el rango para graficar X(n)
rangeHn = rangeToGraph(Hn,centerH)  #Obteniendo el rango para graficar H(n)

#Convierte las funciones necesarias
Xn = [float(i) for i in convertFunc(Xn)] #convierte de list a float list
Hn = [float(i) for i in convertFunc(Hn)] #convierte de list a float list

"""
#Informacion de X(n) y H(n)
print("\n_____DATA X(n)_____\n")
infoGn(Xn,centerX,Xi,Xf)
print("\n_____DATA H(n)_____\n")
infoGn(Hn,centerH,Hi,Hf)
"""

#Dibujar primero las dos funciones: X(n) y H(n)

#Dibuja la funcion X(n) 
plt.figure(1)
plt.subplot(121)
markerline, stemlines, baseline = plt.stem(rangeXn, Xn, '-.')
plt.setp(baseline, color='r', linewidth=2)
plt.title("X[n]")
plt.grid(True)

print("\n\n")

#Dibuja la function H(n) 
plt.subplot(122)
markerline, stemlines, baseline = plt.stem(rangeHn, Hn, '-.')
plt.setp(baseline, color='b', linewidth=2)
plt.title("H[n]")
plt.grid(True)
plt.show()

#Convolucion
Yn = np.convolve(Xn,Hn).tolist()
Yi = Xi+Hi
Yf = Xf+Hf-1
rangeYn = np.arange(Yi,Yf)

print("\nY[n]: ",Yn)
print("Yi: ",Yi)
print("Yf: ",Yf)
print("Range: ",rangeYn)


plt.figure(2)
markerline, stemlines, baseline = plt.stem(rangeYn, Yn, '-.')
plt.setp(baseline, color='r', linewidth=2)
plt.title("Y[n] = X[n]*H[n]")
plt.grid(True)
plt.show()