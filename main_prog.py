
from Main import *
from PyQt5.QtGui import *
import os

def OpenCalculatorWindow(self):
    # AboutUs_Window.hide()
    os.system('Calculator_prog.py')
    # AboutUs_Window.close()
    

def OpenEngineeringWindow(self):
    os.system('EngineeringTool_prog.py')
    

def OpenNetworkToolWindow(self):
    pass

def OpenAboutUsWindow(self):
    os.system('AboutUsWindow_prog.py')
    

def signals(self):
    self.PB_Kalkulator.clicked.connect(lambda: self.OpenCalculatorWindow())
    self.PB_EngineeringTool.clicked.connect(lambda: self.OpenEngineeringWindow())
    self.PB_NetworkTool.clicked.connect(lambda: self.OpenNetworkToolWindow())
    self.PB_AboutUs.clicked.connect(lambda: self.OpenAboutUsWindow())

Ui_Main.signals = signals
Ui_Main.OpenCalculatorWindow = OpenCalculatorWindow
Ui_Main.OpenEngineeringWindow = OpenEngineeringWindow
Ui_Main.OpenNetworkToolWindow = OpenNetworkToolWindow
Ui_Main.OpenAboutUsWindow = OpenAboutUsWindow

if __name__ == "__main__":              
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    ui.signals()
    Main.show()
    sys.exit(app.exec_())