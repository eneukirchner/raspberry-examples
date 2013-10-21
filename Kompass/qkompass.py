#!/usr/bin/python

import smbus
import time
import math
import sys
from PySide import QtCore, QtGui

OFFSET = 2048
DEVICE = 0x30 # Geraete Adresse 1D (30)
CONTROL = 0x00 # Steuerregister
XMSB = 0x01
XLSB = 0x02
YMSB = 0x03
YLSB = 0x04

class i2c():
    def __init__(self):
        self.bus = smbus.SMBus(1)
        # set / reset coil
        self.bus.write_byte_data (DEVICE,CONTROL,0x00)
        self.bus.write_byte_data (DEVICE,CONTROL,0x02)
        time.sleep(0.2)

        self.bus.write_byte_data (DEVICE,CONTROL,0x00)
        self.bus.write_byte_data (DEVICE,CONTROL,0x04)
        time.sleep(0.2)

    def getAngle(self):
        self.bus.write_byte_data (DEVICE,CONTROL,0x00) # Reset des Geraetes
        time.sleep(0.1)
        self.bus.write_byte_data (DEVICE,CONTROL,0x01) # set des Geraetes
        time.sleep(0.1)
        self.bus.write_byte_data (DEVICE,CONTROL,0x00) # TM (take mesurement)
        time.sleep(0.1)

        dummy = self.bus.read_byte_data (DEVICE,CONTROL)
        rXMSB = self.bus.read_byte_data (DEVICE,XMSB)
        rXLSB = self.bus.read_byte_data (DEVICE,XLSB)
        rYMSB = self.bus.read_byte_data (DEVICE,YMSB)
        rYLSB = self.bus.read_byte_data (DEVICE,YLSB)

        x = rXMSB*256+rXLSB-OFFSET
        y = rYMSB*256+rYLSB-OFFSET
        # print (x)
        # print (y)
        angle = math.atan2(y,x)*180.0/math.pi
        angle = angle if  angle >= 0 else angle + 360.0
        # print (round(angle,1))
        # print ("------------")
        return angle


class Compass(QtGui.QWidget):
    northHand = QtGui.QPolygon([
        QtCore.QPoint(7, 0),
        QtCore.QPoint(-7, 0),
        QtCore.QPoint(0, -70)
    ])

    southHand = QtGui.QPolygon([
        QtCore.QPoint(7, 0),
        QtCore.QPoint(-7, 0),
        QtCore.QPoint(0, 70)
    ])

    northColor = QtGui.QColor(255, 0, 0)
    southColor = QtGui.QColor(0, 0, 255)

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.comp = i2c()
        timer = QtCore.QTimer(self)
        self.connect(timer, QtCore.SIGNAL("timeout()"), self, QtCore.SLOT("update()"))
        timer.start(500)

        self.setWindowTitle(self.tr("Compass"))
        self.resize(200, 200)

    def paintEvent(self, event):
        side = min(self.width(), self.height())
        time = QtCore.QTime.currentTime()

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 200.0, side / 200.0)

        painter.save()
        painter.setPen(Compass.southColor)
        painter.rotate(-45.0)
        for j in range(0, 7):
                painter.drawLine(92, 0, 96, 0)
                painter.rotate(45.0)

        painter.setPen(Compass.northColor)
        painter.drawLine(88, 0, 96, 0)
        painter.restore()

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(Compass.northColor)

        phi = self.comp.getAngle()
        painter.save()
        painter.rotate(phi)
        painter.drawConvexPolygon(Compass.northHand)
        painter.restore()

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(Compass.southColor)

        painter.save()
        painter.rotate(phi)
        painter.drawConvexPolygon(Compass.southHand)
        painter.restore()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    c = Compass()
    c.show()
    sys.exit(app.exec_())
