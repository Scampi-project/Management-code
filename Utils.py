import os
import json
from datetime import datetime
class Logger:
    def log_info(self,name,txt):
        os.chdir("C:/Users/benja/Documents/AERO_2/STAGE/SCAMPI/Management") #A modifier avec le chemin du raspberry
        # os.chdir("/home/pi/SCAMPI/Management")
        file = open(f"./{name}.log",'a')
        file.write(f'\n{txt}')
        file.close()
    def log_values(self,sensor,value):
        json_file = open("C:/Users/benja/Documents/AERO_2/STAGE/SCAMPI/Management/sensors_values.json", 'r')
        txt = json.load(json_file)
        json_file.close()
        json_file = open("C:/Users/benja/Documents/AERO_2/STAGE/SCAMPI/Management/sensors_values.json", 'w')
        txt["sensors"][sensor]["time"].append(datetime.now().strftime("%d-%m , %H:%M:%S"))
        txt["sensors"][sensor]["values"].append(value)
        
        json.dump(txt,json_file,indent=2)
        json_file.close()
    def log_cleaning(self,all=False,file=''):
        print("heho")
        if all:
            list = ['power_operations','nominal_operations','transmission_operations','measurement_operations','errors']
            for i in list :
                file = open(f"{i}.log","r+")
                file.truncate(0)
        else :
                file = open(f"{file}.log","r+")
                file.truncate(0)
    def json_cleaning(self):
        json_file = open("C:/Users/benja/Documents/AERO_2/STAGE/SCAMPI/Management/sensors_values.json", 'w')
        json.dump({"sensors": {"tmp36_temperature":{"time": [], "values": []},"OBC_temperature":{"time": [],"values": []},"pressure":{"time": [],"values": []}}},json_file)
class SystemStatus:
    def __init__(self):
        self.current_mode = 'PowerOff'
        self.log = Logger()
    def set_mode(self,mode,critical=False) :
        if mode == 'Initialization':
            # cleaning ram with garbage collector
            #if critical == False :
            #    self.log_cleaning(file)
            # os.system("source /home/pi/env/bin/activate")
            
            self.log.log_info("power_operations","Initialization complete")
        if mode == 'PowerOff':
            file = open(f"./power_operations.log",'a')
    
            file.write(f'\nPower is Off')
        if mode == 'PowerOn':
            file = open(f"./power_operations.log",'a')
            
            file.write(f'\nPower is On')

        if mode == 'Nominal':
    
            print('Trying to change the world')
        if mode == 'Transmission':
    
            print('Vous êtes satellisé')
        if mode == 'Measurement':
    
            print('Vous êtes satellisé mesurément')
        if mode == 'DataAnalysis':
    
            print('Vous êtes satellisé analytiquement')
            
        
    def update_mode(self,mode):
        self.set_mode(mode)
        self.current_mode = mode
        self.log.log_info(f"power_operations",f"mode is changing from {self.current_mode} to {mode}")
        

        
if __name__ == '__main__' :   
    test = Logger()
    test.log_values("tmp36_temperature",28)
    # test.json_cleaning()
    #test.log_info("transmission_operations","tout va bien,mais pas trop")
    #test2 = SystemStatus()
    #test2.set_mode('Intialization')


