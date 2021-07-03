from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import re

root = Tk()

Xn = []
Hn = []
matrizTotal = [[]]
entradaXn = StringVar()
entradaHn = StringVar()

entradaNx = StringVar()
entradaNh = StringVar()

# ConvCircular
bConv = False

# ConvPeriodica
bConvPe = False

varCir = IntVar()

root.title("Convolucion Discreta")

# ==============================================

myFrame = Frame(root, width = 500, height = 520)
myFrame.pack()

labelTitle = Label(myFrame, text="Convolucion Discreta", font=("Quicksand",18))
labelTitle.place(x=120,y=10)

labelIns = Label(myFrame,text="Indicar el centro de la funcion con el simbolo '*'",font=("Quicksand",14))
labelIns.place(x=30, y=50)

labelXn = Label(myFrame, text="Introduce x(n):", font=("Quicksand",12))
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

buttonCal = Button(root,text="Calcular",font=("Quicksand",12),command=lambda:calculaConv(txtXn,txtHn))

buttonLimp = Button(root,text="Limpiar",font=("Quicksand",12),command=lambda:limpiar())

buttonGrafS = Button(root,text="Salida",font=("Quicksand",12),command=lambda:graficaSalida(calculaConv(txtXn,txtHn)))

buttonGrafE = Button(root,text="Entrada",font=("Quicksand",12),command=lambda:graficaIn(calculaConv(txtXn,txtHn)))


labelHn.place(x=10, y=210)
txtHn.place(x=10,y=230)
lablelConv.place(x=10,y=340)

buttonCal.place(x=30,y=300)
buttonLimp.place(x=130,y=300)
buttonGrafS.place(x=230,y=300)
buttonGrafE.place(x=320,y=300)

#	Convolucion Normalona
convCir = Radiobutton(myFrame,text="Conv. Normal", variable = varCir, value = 0, command = lambda:bloquearTxt(0))
convCir.place(x=10, y=90)

#	Convolucion Circular
convCir = Radiobutton(myFrame,text="Conv. Circular", variable = varCir, value = 1, command = lambda:bloquearTxt(1) )
convCir.place(x=140, y=90)

#	Convolución Periodica
convCir = Radiobutton(myFrame,text="Conv. Periodica", variable = varCir, value = 2, command = lambda:bloquearTxt(2) )
convCir.place(x=270, y=90)

# =======================================================================================================================
def graficaIn(varList):
    print("entrada")
    plt.figure(1)
    plt.subplot(121)
    markerline, stemlines, baseline = plt.stem(varList[0][:],varList[1][:] , '-.')
    plt.setp(baseline, color='r', linewidth=2)
    plt.title("X[n]")
    plt.grid(True)  

    print("\n\n")
    #Dibuja la function H(n) 
    plt.subplot(122)
    markerline, stemlines, baseline = plt.stem(varList[2][:], varList[3][:], '-.')
    plt.setp(baseline, color='b', linewidth=2)
    plt.title("H[n]")
    plt.grid(True)

    plt.show()

def graficaSalida(varListSal):
    #Dibuja la convolución
    plt.figure(2)
    markerline, stemlines, baseline = plt.stem(varListSal[4][:], varListSal[5][:], '-.')
    plt.setp(baseline, color='r', linewidth=2)
    plt.title("Y[n] = X[n]*H[n]")
    plt.grid(True)
    plt.show()  


def redondear(x):
    n = int(x)
    return n if n-1 < x <= n else n+1

#	Funcion para habilitar o deshabilitar los campos de texto
def bloquearTxt(xd):
	global bConv
	global bConvPe

	if xd == 0:
		txtNx.config(state='disabled') 
		txtNh.config(state='disabled') 
		bConv = False
		bConvPe = False

	elif xd == 1:
		txtNx.config(state='normal')
		txtNh.config(state='normal')
		bConv = True
		bConvPe = False
		
	elif xd == 2:
		txtNx.config(state='normal')
		txtNh.config(state='disabled') 
		bConv = False
		bConvPe = True

#Funciones
def limpiar():

	lablelConv.config(text="")
	entradaXn.set("")
	entradaHn.set("")
	entradaNx.set("")
	entradaNh.set("")

def whereIsCenter(list):
    indice = 0
    while indice < len(list):
        if '*' in list[indice]:
            return indice
        indice += 1
    return 0

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

def convertFunc(list):
    indice = 0
    while indice < len(list):
        if '*' in list[indice]:
            list[indice] = list[indice].replace('*','')
        indice += 1
    return list

def calculaConv(entradaXn, entradaHn):
    #se obtienen los datos de entrada 
    textXn = entradaXn.get().split(",")
    textHn = entradaHn.get().split(",")

    print("x: " + str(textXn) + " H: " + str(textHn))

    #Se obtiene el centro de la función
    centerX = whereIsCenter(textXn)
    centerH = whereIsCenter(textHn)
    
    if(centerX==0):
        centerX = (int)(len(textXn)/2)   
    if(centerH==0):
        centerH = (int)(len(textHn)/2)  

    Xi = getGi(textXn,centerX)  #Xi : Inicio X(n)
    Xf = getGf(textXn,centerX)  #Xf : Fin X(n)
    Hi = getGi(textHn,centerH)  #Hi : Inicio H(n)
    Hf = getGf(textHn,centerH)  #Hf : Fin H(n)
    
    rangeXn = rangeToGraph(textXn,centerX)  #Obteniendo el rango para graficar X(n)
    rangeHn = rangeToGraph(textHn,centerH)  #Obteniendo el rango para graficar H(n)

    #Convierte las funciones necesarias
    Xn = [float(i) for i in convertFunc(textXn)] #convierte de list a float list
    Hn = [float(i) for i in convertFunc(textHn)] #convierte de list a float list

    Yn = np.convolve(Xn,Hn).tolist()
    Yi = Xi+Hi
    Yf = Xf+Hf-1
    rangeYn = np.arange(Yi,Yf)

    print("\nY[n]: ",Yn)
    print("Yi: ",Yi)
    print("Yf: ",Yf)
    print("Rango: ",rangeYn)
    lablelConv.config(text="Convolucion: \n\n"+str(Yn))
    
    lista = [rangeXn, Xn, rangeHn, Hn, rangeYn, Yn]
    return lista

root.mainloop()