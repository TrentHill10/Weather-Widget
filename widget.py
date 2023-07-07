from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QSize, Qt, QPoint
from PyQt5.QtWidgets import *
import sys
from weather_API import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Sets title
        self.setWindowTitle('Weather App')

        #Background
        self.setStyleSheet('background-color: lightblue;')
        
        #Sets size
        self.setFixedSize(QSize(400, 300))

        #Creates borderless widget
        self.setWindowFlags(Qt.FramelessWindowHint)

        #Adding image of pushpin/location pin
        self.label = QLabel(self)
        self.pixmap = QPixmap('location.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())
        
        #Adding image of sun to widget
        self.label1 = QLabel(self)
        self.pixmap1 = QPixmap('sun.png')
        self.label1.setPixmap(self.pixmap1)
        self.label1.resize(self.pixmap1.width(), self.pixmap1.height())
        self.label1.move(0,100)

        #Adding image of thermometer
        self.label2 = QLabel(self)
        self.pixmap2 = QPixmap('thermometer.png')
        self.label2.setPixmap(self.pixmap2)
        self.label2.resize(self.pixmap2.width(), self.pixmap2.height())
        self.label2.move(0,200)

        #Addiing location text
        self.label3 = QLabel(self)
        self.label3.setText(location['name'])
        self.label3.setFont(QFont('Ariel', 20))
        self.label3.setFixedWidth(150)
        self.label3.setFixedHeight(32)
        self.label3.move(100,35)
        
        #Adding weather condition text
        self.label4 = QLabel(self)
        self.label4.setText(condition['text'])
        self.label4.setFont(QFont('Ariel', 20))
        self.label4.move(100,135)
        
        #Adding temp in F to widget
        self.label5 = QLabel(self)
        self.label5.setText(str(current['temp_f']) + '°F')
        self.label5.setFont(QFont('Ariel', 20))
        self.label5.move(100,235)

    #Function to recognize a mouse click
    def mousePressEvent(self, event):
        self.tabPosition = event.globalPos()

    #Function to move widget where ever the mouse drags it to after clicking and holding
    def mouseMoveEvent(self, event):
        num = QPoint(event.globalPos() - self.tabPosition)
        self.move(self.x() + num.x(), self.y() + num.y())
        self.tabPosition = event.globalPos()
        
#Allows widget to accept command line arguments
app = QApplication(sys.argv)

#Creates actual window with all the functions and properties defined in the class
window = MainWindow()
#!!!IMPORTANT!!! Allows window to be visible when running code
window.show()

app.exec()