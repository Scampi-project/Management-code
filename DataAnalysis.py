import json
from Utils import Logger, SystemStatus

class DataAnalysis :
    
    def _init_(self):
        raspberrydir="/home/pi/SCAMPI"
        self.logger = Logger()
        self.system = SystemStatus()
        self.json_file=open(raspberrydir+"/Sensors/sensors_values.json",'r')
        self.txt=json.load(self.json_file)
        
    def tmp36_temperature(self):
        if len(self.txt["sensors"]["tmp36_temperature"]["values"])<5 :
            self.logger.log_info("DataAnalysis","Not enough measures")
        else :   
            self.mean=0
            for i in range (5):
                self.mean+=self.txt["sensors"]["tmp36_temperature"]["values"][-i-1]
            self.mean=self.mean/5
            self.srd=0
            for i in range(5):
                self.std+=self.txt["sensors"]["tmp36_temperature"]["values"][-i-1]**2
            self.std=self.std**(1/2)        
            self.logger.log_info("DataAnalysis",f"mean_tmp36-temperature_5-last-measures : {self.mean} , standard-deviation-type_tmp36-temperature_5-last-measures : {self.std}")
    
    def obc_temperature(self):
        if len(self.txt["sensors"]["OBC_temperature"]["values"])<5 :
            self.logger.log_info("DataAnalysis","Not enough measures")        
        else :   
            self.mean=0   
            for i in range (5):
                self.mean+=self.txt["sensors"]["OBC_temperature"]["values"][-i-1]
            self.mean=self.mean/5
            self.srd=0
            for i in range(5):
                self.std+=self.txt["sensors"]["OBC_temperature"]["values"][-i-1]**2
            self.std=self.std**(1/2)
            self.logger.log_info("DataAnalysis",f"mean_OBC-temperature_5-last-measures : {self.mean} , standard-deviation-type_OBC-temperature_5-last-measures : {self.std}")
      
        
    def pressure(self):        
        if len(self.txt["sensors"]["pressure"]["values"])<5 :
            self.logger.log_info("DataAnalysis","Not enough measures")        
        else :   
            self.mean=0            
            for i in range (5):
                self.mean+=self.txt["sensors"]["pressure"]["values"][-i-1]
            self.mean=self.mean/5            
            self.srd=0            
            for i in range(5):
                self.std+=self.txt["sensors"]["pressure"]["values"][-i-1]**2
            self.std=self.std**(1/2)    
            self.logger.log_info("DataAnalysis",f"mean_pressure_5-last-measures : {self.mean} , standard-deviation-type_pressure_5-last-measures : {self.std}")
   
   
    

