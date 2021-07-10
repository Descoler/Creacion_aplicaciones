# ------------------------- PyQt6 ----------------
# Instalar PyQt6: pip install pyqt6
# importamos el diseño hecho con PyQt Designer (editor de ventanas de PyQt).
# el archivo tine la extension *.ui

import sys
# importar libreria para cargar el archivo *.ui
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QDialog
# from PyQt5.QtWidgets import QApplication, QMainWindow

class ejemplo_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        # copiamos el path donde tenemos el archivo .ui (designer_1.ui)
        # /home/obert/opt/proyectos/PyQt
        uic.loadUi("/home/obert/opt/proyectos/PyQt/pyqt6_GUID.ui", self)

# ----------------------- función Main -------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI()
    #uic.loadUi("/home/obert/opt/proyectos/PyQt/pyqt6_GUID.ui")
    GUI.show()
    sys.exit(app.exec())
