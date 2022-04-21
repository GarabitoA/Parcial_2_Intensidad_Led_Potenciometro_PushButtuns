
from xmlrpc.client import ProtocolError
from numpy import append
import serial,time
import matplotlib.pyplot as plt
from tkinter import * 


from pyqtgraph.Qt import QtGui,QtCore
import pyqtgraph as pg
from pyfirmata import Arduino,util
port = "COM5"
board = Arduino(port)
it = util.Iterator(board)
it.start()

app=QtGui.QApplication([])
win=pg.GraphicsWindow(title='Tiempo Real')
p=win.addPlot(title='Grafica en tiempo real')
curva=p.plot(pen='y')

p.setRange(yRange=[0,255])
dataX=[]
dataY=[]
lastY= 0
analog0=board.get_pin('a:0:i')

def Update():
    global curva, dataX,dataY, lastY, nuevoDato

    dato = analog0.read()
    if dato is not None:
        nuevoDato=dato*255
        print(nuevoDato)
        time.sleep(1)
    else:
            nuevoDato=0
    
    dataX.append(nuevoDato)
    dataY.append(lastY)
    lastY+=1

    if len(dataX)>200:
        dataX=dataX[:-1]
        dataY=dataY[:-1]
    
    curva.setData(dataY,dataX)
    QtGui.QApplication.processEvents()

try:
    while True: Update()
except KeyboardInterrupt:
    pg.QtGui.Application.exec_()
    board.exit()


# PARA BOTONES EN LA INTERAZ DE PYTHON
arduino = serial.Serial("COM5",9600)
#time.sleep(2)

# CREANDO FUNCIONES PARA BOTONES
def buttonA():
    print("Boton pulsado para - LED ROJO","\n")
    time.sleep(2)
    print("Potenciometro listo para manipular","\n")
    time.sleep(3)
    print("Mostrando valores analogicos del potenciometro","\n")
    time.sleep(3)
    while 1:
        lectura = arduino.readline().decode("UTF-8")
        print(lectura)



def buttonB():
    print("Boton pulsado para LED AMARILLO","\n")
    time.sleep(2)
    print("Potenciometro activado automaticamente","\n")
    time.sleep(3)
    print("Mostrando valores analogicos del potenciometro","\n")
    time.sleep(3)
    while 1:
        lecturaa = arduino.readline().decode("UTF-8")
        print(lecturaa)


def buttonExit():
    time.sleep(3)
    quit()


print("\n","---------- 2DO PARCIAL ARQUITECTURA DE COMPUTADORAS ------","\n","\n","-> PROGRAMA INICIADO","\n")



# CREACION DE BOTONES QUE ENVIARAN SEÑAL A ARDUINO
#CREANDO INTERFAZ
ventana = Tk() #se crea la ventana
ventana.title("BOTONES PARA ENVIO DE SEÑAL ARDUINO") #Definimos el nombre de nuestra ventana
ventana.geometry('550x350') #El primer numero es el ancho y el segundo es el alto de la ventana
ventana.configure(background='indian red') #Le damos a nuestra ventana un color de fondo negro


#CREANDO BOTONES
# BOTON A
botonA = Button(ventana, text="INICIAR POTENCIOMETRO - LED ROJO", fg="black", command=buttonA) #El command llama la accion del boton, en este caso una funcion que muestra un resultado en especifico
botonA.config(width=30, height=3) #Defino anchura y altura del boton
botonA.place(x=40, y=110) #coordenadas donde quiero que este el boton en la ventana

# BOTON B
botonB = Button(ventana, text="BOTON - LED AMARILLO", fg="black", command=buttonB)
botonB.config(width=30, height=3)
botonB.place(x=300, y=110)

# BOTON EXIT
botonExit = Button(ventana, text="EXIT", fg="black", command=buttonExit)
botonExit.config(width=20, height=3)
botonExit.place(x=180, y=210)

ventana.mainloop()
