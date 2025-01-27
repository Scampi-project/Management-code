#import board
# import analogio
#!/usr/bin/env python
import time
from convert import Convert
import sys
sys.path.insert(1,"/home/pi1/SCAMPI/Management")
from Utils import Logger

class Temperature :
    
    def __init__ (self): 
        self.convert=Convert()
        self.log=Logger()
    
    #fonction lisant les donnees SPI de la puce MCP3008, parmi 8 entrees, de 0 a 7
    def tmp36(self) : 
    
            # Lecture de la valeur brute du capteur
        self.adcout=self.convert.readadc("tmp36")
            # conversion de la valeur brute lue en milivolts = ADC * ( 3300 / 1024 )
        self.millivolts = self.adcout * ( 3300.0 / 1024.0)
        self.bias=0
        # 10 mv per degree
        self.temp_C = (self.millivolts / 10.0) - 40.0+ self.bias
        self.temp_C=((self.temp_C*10)//1 )/10.0 #juste une décimale
        self.log.log_values("tmp36_temperature",self.temp_C)
       
        return self.temp_C
        
    def IR(self):
        self.adcout=self.convert.readadc("IR")
            

if __name__ == "__main__":
    test=temperature()
    while True :
        a=test.tmp36()
        print ("valeurs lues : ")
        print ("\ttemperature : %s C" % a)
        time.sleep(0.2)
