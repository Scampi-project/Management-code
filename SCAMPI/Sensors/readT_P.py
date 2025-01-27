import numpy as np
import RPi.GPIO as GPIO
import time 
import sys
from convert import Convert
sys.path.insert(1,"/home/pi1/SCAMPI/Management")
from Utils import Logger

class T_P_probe:
    def __init__ (self): 
        self.convert=Convert()
        self.log=Logger()
        self.freq=100
        
    def read_measure(self):
        self.list=[]
        self.nptime=np.linspace(0,2,1000)
        t0=time.time()
        i=0
        while i<1000 :
            while (time.time()-t0<=self.nptime[i]):
                True
            self.list.append(self.convert("probe"))
            i+=1
        self.temp=value("temperature")
        self.pressure=value("pressure")
        self.log.log_values("probe_temperature",self.temp)
        self.log.log_values("pressure",self.pressure)
        
    def value(sensor) :
        self.nplist=np.array(self.list)
        dt=self.nptime[1]-self.nptime[0]
        slef.fourrier=np.fft.fft(self.nplist)
        self.fourrier_freq=np.fft.fftfreq(len(self.nplist),d=dt)
        
        if (sensor=="temperature"):
            self.f=self.freq*2
        else :
            self.f=self.freq
            
        self.bool=(self.f+1 >self.fourrier_freq > self.f-1)
        
        return np.sum(self.bool*self.fourrier)/np.sum(self.bool)
            
