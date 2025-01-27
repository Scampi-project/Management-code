import os
import json
from datetime import datetime
import gc
class Logger:
    path="/home/pi1/SCAMPI"
    def log_info(self,name,txt):
        #os.chdir("C:/Users/benja/Documents/AERO_2/STAGE/SCAMPI/Management") #A modifier avec le chemin du raspberry
        os.chdir(path)
        file = open(f"./{name}.log",'a')
        file.write(f'\n{txt}')
        file.close()
        
    def log_values(self,sensor,value):
        with open(path+"/sensors_values.json", 'r') as file :
            self.txt = json.load(file)
            file.close()
        self.txt["sensors"][sensor]["time"].append(datetime.now().strftime("%d-%m , %H:%M:%S"))
        self.txt["sensors"][sensor]["values"].append(value)
        with open(path+"/sensors_values.json", 'w') as file :
            json.dump(self.txt,file,indent=2)
            file.close()
    
    def log_cleaning(self,all=False,file=''):
        
        if all:
            list = ['power_operations','nominal_operations','transmission_operations','measurement_operations','errors']
            for i in list :
                file = open(f"{i}.log","r+")
                file.truncate(0)
                file.close()
        else :
                file = open(f"{file}.log","r+")
                file.truncate(0)
                file.close()
                
    def json_cleaning(self):
        self.time=datetime.now().strftime("%d-%m , %H:%M:%S")
        with open(path+"/sensors_values.json", 'w') as file :
            json.dump({"sensors": {"tmp36_temperature":{"time": [], "values": []},"OBC_temperature":{"time": [],"values": []},"probe_temperature":{"time": [], "values": []},"pressure":{"time": [],"values": []}}, "count": 0 , "shutdown" : [self.time]},file,indent=2)
            file.close()
            
class SystemStatus:
    
    def __init__(self):
        self.current_mode = 'PowerOff'
        self.log = Logger()
        
    def update_mode(self,mode):
        self.log.log_info("power_operations",f"mode is changing from {self.current_mode} to {mode}")
        if mode=="Initialisation":
            gc.collect(generation=0) #nettoyage de la RAM
            #if critical == False :
            #    self.log_cleaning(file)
            #os.system("source /home/pi1/env/bin/activate")
        self.current_mode = mode
        self.log.log_info("power_operations",f"{mode}")
    """
    def set_mode(self,mode,critical=False) :
        if mode == 'Initialization':
            # cleaning ram with garbage collector
            #if critical == False :
            #    self.log_cleaning(file)
            # os.system("source /home/pi1/env/bin/activate")
            
            self.log.log_info("power_operations","Initialization complete")
        if mode == 'PowerOff':
            self.log.log_info("power_operations","Power is Off")
        
        if mode == 'PowerOn':
            self.log.log_info("power_operations","Power is On")

        if mode == 'Nominal':
    
            print('Trying to change the world')
        if mode == 'Transmission':
    
            print('Vous êtes satellisé')
        if mode == 'Measurement':
    
            print('Vous êtes satellisé mesurément')
        if mode == 'DataAnalysis':
    
            print('Vous êtes satellisé analytiquement')
            
     """   
    
        

        
if __name__ == '__main__' :   
    test = Logger()
    #test.log_cleaning(True)
    #test.log_values("tmp36_temperature",28)
    test.json_cleaning()
    #test.log_info("transmission_operations","tout va bien,mais pas trop")
    #test2 = SystemStatus()
    #test2.set_mode('Intialization')


