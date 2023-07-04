from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize, Qt, QPoint
from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.acceptDrops()

        self.setWindowTitle('Weather App')
        
        self.setFixedSize(QSize(400, 300))

        self.setWindowFlags(Qt.FramelessWindowHint)

        #Adding image of sun to widget
        self.label = QLabel(self)
        self.pixmap = QPixmap('sun_icon.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())

        self.show()



    def mousePressEvent(self, event):
        self.tabPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        num = QPoint(event.globalPos() - self.tabPosition)
        self.move(self.x() + num.x(), self.y() + num.y())
        self.tabPosition = event.globalPos()
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()