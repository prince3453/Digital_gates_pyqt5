from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow 
import sys

class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('Tech with Prince!!!')
        self.initUI()

    def initUI(self):
        self.label =QtWidgets.QLabel(self)
        self.label.setText("First name : ")
        self.label.move(10,0)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Submit!!!")
        self.b1.clicked.connect(self.clicked)

        self.b1.move(0,20)

    def clicked(self):
        self.label.setText('You Pressed the button.')
        self.update()

    def update(self):
        '''Automatic adjust the size of the label when pressed the button'''
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = mywindow()
    win.show()
    sys.exit(app.exec_())

window()