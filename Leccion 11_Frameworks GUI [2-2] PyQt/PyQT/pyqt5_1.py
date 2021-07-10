# ------------------------- PyQt5 ----------------
# pip install pyqt5
from PyQt5.QtWidgets import *
# from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# ----------------------- Applicatción -------------------
# Creamos la ventana con un título y unas dimensiones
# setGeometry(left,top,width,height)
app=QApplication(sys.argv)
ventana=QMainWindow()
ventana.setGeometry(800,100,500,500)
# he colocado la ventana de 500x500
# y que aparezca a la derecha del texto.
ventana.setWindowTitle("Mi primera Aplicación PyQt")
#----------------------------------------------------------

#----------- Labels ----------------
# Creamos 2 Labels para la ventana. 
# Indicamos un texto para cada una Le decimos que se ajuste (en tamaño) al texto 
# Le indicamos la posición, siendo (0,0) arriba a la izquierda
label_1 = QLabel(ventana)
label_1.setText("Aplicacion programada con PyQt5!")
label_1.adjustSize()
label_1.move(150,20)

label_2 = QLabel(ventana)
label_2.setText("Escribe algo en el siguiente QLineEdit:")
label_2.adjustSize()
label_2.move(20, 100)
#---------------------------------------

#---------- funcion_imprimir -------
# Defino 2 funciones que me harán falta posteriormente
# Una de ellas es para imprimir en la “cmd”. 
# La otra función sirve para salir.

# funcion asociada a un boton (boton_1)
# combinamos con line_edit_1
def funcion_imprimir():
    print(line_edit_1.text())
#-------------------------------------
# ----------------- funcion salir -------------
# función asociada al boton_2
# Le decimos que salga de la ventana.
def funcion_salir():
    ventana.close()
#----------------------------------------------

# -------------- botones-----------
# Creo 2 botones (y les ubicaré en la ventana) 
# El primero de ellos lo conecto con la función_imprimir
# El segundo de ellos sirve para salir de la aplicación
# Botón para imprimir
boton1 = QPushButton(ventana)
boton1.setText("Imprimir en cmd")
boton1.clicked.connect(funcion_imprimir)
boton1.move(20, 200)

# Botón para salir de la aplicación
boton2 = QPushButton(ventana)
boton2.setText("Salir")
boton2.clicked.connect(funcion_salir)
boton2.move(390, 450)
#------------------------------------

# ----------------------- line_edit ----------------
# Sirve para hacer una entrada de texto. 
# La misma será impresa en “cmd” gracias a su vinculación con el botón de imprimir y 
# la propia función asociada a ese botón
line_edit_1 = QLineEdit(ventana)
line_edit_1.move(20,150)
#--------------------------------------------------

# ---------------- show y exit --------------------
# Muestra la ventana y cierra la ventana 
# También podemos cerrar la Aplicación con el aspa (x) de cerrar
ventana.show()
sys.exit(app.exec_())
#---------------------------------------------------
