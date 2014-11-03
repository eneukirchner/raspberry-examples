#!/usr/bin/python
# -*- coding: utf-8 -*-
# Edgar Neukirchner 2014

from PyQt4 import QtGui, QtCore 
import alsaaudio
import audioop
import sys
import math

class VuMeter(QtGui.QWidget):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK, 'sysdefault:CARD=AUDIO')
                # self.inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)
                self.inp.setchannels(1)                          
                self.inp.setrate(8000)                           
                self.inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)  
                self.inp.setperiodsize(320)
                
                self.timer = QtCore.QTimer(self)
                self.timer.timeout.connect(self.getPCM)
                self.timer.start(5)
                
                self.setGeometry(0, 0, 320, 240)
                self.setWindowTitle('VU Meter')
                self.bar = QtGui.QProgressBar(self)
                self.bar.setGeometry(20, 100, 280, 40)
                
                self.steps = float(32768)
                self.min = 20*math.log10(1/self.steps)
                self.bar.setMinimum(int(self.min))
                self.bar.setMaximum(0)
                self.bar.setFormat("%v dB")
                                
        def getPCM(self):
                l, data = self.inp.read()
                hi = 32768.0
                if l > 0:
                        # Dezibel
                        vu = 20*math.log10(max(audioop.max(data, 2),1)/self.steps)
                        # vu = audioop.max(data,2)
                        self.bar.setValue(vu)
                        # print vu
                      
def main():
        app = QtGui.QApplication(sys.argv)
        main = VuMeter()
        main.show()
        sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()    

