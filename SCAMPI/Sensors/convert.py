#for MCP3008
import RPi.GPIO as GPIO

class Convert:
    
    def __init__(self):
        self.clockpin=11
        self.cspin=8
        self.mosipin=10
        self.misopin=9
        
         
        
    def readadc(self,sensor):
        
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.mosipin, GPIO.OUT)
        GPIO.setup(self.misopin, GPIO.IN)
        GPIO.setup(self.clockpin, GPIO.OUT)
        GPIO.setup(self.cspin, GPIO.OUT)
        
        if (sensor=="tmp36") :
            self.adcnum=1
        if (sensor=="probe"):
            self.adcnum=0
        if(sensor=="IR"):
            self.adcnum=2
        else :
            return error()
            
        GPIO.output(self.cspin, True)
        GPIO.output(self.clockpin, False)  # start clock low
        GPIO.output(self.cspin, False)	 # bring CS low

        self.commandout = self.adcnum
        self.commandout |= 0x18  # start bit + single-ended bit
        self.commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):       #initialising the MCP3008
            if (self.commandout & 0x80):
                GPIO.output(self.mosipin, True)
            else:  
                GPIO.output(self.mosipin, False)
            self.commandout <<= 1
            GPIO.output(self.clockpin, True)
            GPIO.output(self.clockpin, False)   
        self.adcout = 0
            # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
            GPIO.output(self.clockpin, True)
            GPIO.output(self.clockpin, False)
            self.adcout <<= 1
            if (GPIO.input(self.misopin)):
                self.adcout |= 0x1
     
        GPIO.output(self.cspin, True)
        self.adcout /= 2	   # first bit is empty, second is 'null' so drop it
        return self.adcout
        
