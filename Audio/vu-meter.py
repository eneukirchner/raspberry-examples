#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore 
import alsaaudio
import audioop
import sys
import math

class VuMeter(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.initUI()
			
	def initUI(self):
		self.inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)
		self.inp.setchannels(1)                          
		self.inp.setrate(8000)                           
		self.inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)  
		self.inp.setperiodsize(320)
		
		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.getPCM)
		self.timer.start(5)
		
		self.bar = QtGui.QProgressBar()
		self.bar.setMinimum(0)
		self.bar.setMaximum(32768)
		self.bar.setTextVisible(0)
		
		self.setCentralWidget(self.bar)
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Audio')
		
		self.show()
        
        def getPCM(self):
			l, data = self.inp.read()
			hi = 32768.0
			if l > 0:
				# vu = 20*math.log(max(audioop.max(data, 2),1)/hi)
				vu = audioop.max(data,2)
				self.bar.setValue(vu)
		      
def main():
	app = QtGui.QApplication(sys.argv)
	main = VuMeter()
	main.show()
	sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()    

