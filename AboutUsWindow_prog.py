from AboutUsWindow import *
from PyQt5.QtGui import * 
from PyQt5.uic import loadUi
import os

def OpenAboutUsWindow(self):
    AboutUs_Window.hide()
    os.system('MainWindow_prog.py')
    AboutUs_Window.close()


def ubah(self):
    self.label1.setText(self.text1.text())

def signals(self):
    self.AboutUs_PB_Home.clicked.connect(lambda: self.OpenAboutUsWindow())
    self.PB_update.clicked.connect(lambda: self.ubah())

Ui_AboutUs_Window.signals = signals
Ui_AboutUs_Window.ubah = ubah
Ui_AboutUs_Window.OpenAboutUsWindow = OpenAboutUsWindow

if __name__ == "__main__":              
    import sys 
    app = QtWidgets.QApplication(sys.argv) 
    AboutUs_Window = QtWidgets.QMainWindow() 
    ui = Ui_AboutUs_Window() 
    ui.setupUi(AboutUs_Window) 
    ui.signals()
    AboutUs_Window.show() 
    sys.exit(app.exec_()) 