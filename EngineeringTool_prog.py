
from sys import float_repr_style
from EngineeringToolWindow import *
from PyQt5.QtGui import *    

def CalculateCurrent(self):
    capacity=float(self.Txt1_MotorCapacity.text())
    efficiency=float(self.Txt1_Eff.text())
    powerfactor=float(self.Txt1_PF.text())
    voltage=float(self.Txt1_Volt.text())

    if (self.comboBoxKw_Hp.currentText() == 'horsepower (hp)'):
        capacity=capacity*1000*0.746
    else:
        capacity=capacity*1000

    current1ph_RLA = float(capacity/(voltage*(efficiency/100)))
    current3ph_RLA = float(capacity/(1.732*voltage*powerfactor*(efficiency/100)))

    self.Lbl_1ph_RLA.setText(str("{:.2f}".format(current1ph_RLA)))
    self.Lbl_1ph_FLA.setText(str("{:.2f}".format(current1ph_RLA*1.25)))
    self.Lbl_3ph_RLA.setText(str("{:.2f}".format(current3ph_RLA)))
    self.Lbl_3ph_FLA.setText(str("{:.2f}".format(current3ph_RLA*1.25)))
  

def CalculatePower(self):
    current=float(self.Txt2_Current.text())
    efficiency=float(self.Txt2_Eff.text())
    powerfactor=float(self.Txt2_PF.text())
    voltage=float(self.Txt2_Volt.text())

    Power1ph=float(voltage*current*(efficiency/100))/1000
    Power3ph=float((1.732*voltage*current*(efficiency/100)*powerfactor)/1000)

    self.Lbl_1ph_powerkW.setText(str("{:.2f}".format(Power1ph)))
    self.Lbl_1ph_powerHP.setText(str("{:.2f}".format(Power1ph/0.746)))
    self.Lbl_3ph_powerkW.setText(str("{:.2f}".format(Power3ph)))
    self.Lbl_3ph_powerHP.setText(str("{:.2f}".format(Power3ph/0.746)))

def CalculatekVA(self):
    capacity=float(self.Txt3_MotorCapacity.text())
    efficiency=float(self.Txt3_Eff.text())
    powerfactor=float(self.Txt3_PF.text())

    if (self.comboBox3_Kw_Hp.currentText() == 'horsepower (hp)'):
        capacity=capacity*0.746

    kva = float(capacity/(powerfactor*(efficiency/100)))
    
    self.Lbl_kVA.setText(str("{:.2f}".format(kva)))
    
def signals(self):
    self.PB1_Calculate.clicked.connect(lambda: self.CalculateCurrent())
    self.PB2_Calculate.clicked.connect(lambda: self.CalculatePower())
    self.PB3_Calculate.clicked.connect(lambda: self.CalculatekVA())

Ui_EngineeringTool_Window.signals = signals
Ui_EngineeringTool_Window.CalculateCurrent = CalculateCurrent
Ui_EngineeringTool_Window.CalculatePower = CalculatePower
Ui_EngineeringTool_Window.CalculatekVA = CalculatekVA

if __name__ == "__main__":              
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EngineeringToolWindow = QtWidgets.QMainWindow()
    ui = Ui_EngineeringTool_Window()
    ui.setupUi(EngineeringToolWindow)
    ui.signals()
    EngineeringToolWindow.show()
    sys.exit(app.exec_())