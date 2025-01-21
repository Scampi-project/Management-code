import os
import json
from datetime import datetime
class Logger:
    def log_info(self,name,txt):
        #os.chdir("C:/Users/benja/Documents/AERO_2/STAGE/SCAMPI/Management") #A modifier avec le chemin du raspberry
        os.chdir("/home/pi/SCAMPI/Management")
        file = open(f"./{name}.log",'a')
        file.write(f'\n{txt}')
        file.close()
    def log_values(self,sensor,value):
        json_file = open("/home/pi/SCAMPI/Sensors/sensors_values.json", 'r')
        txt = json.load(json_file)
        json_file.close()
        json_file = open("/home/pi/SCAMPI/Sensors/sensors_values.json", 'w')
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
        #json_file = open("C:/Users/benja/Documents/AERO_2/STAGE/SCAMPI/Management/sensors_values.json(1)", 'w')
        json_file = open("/home/pi/SCAMPI/Sensors/sensors_values.json", 'w')
        json.dump({"sensors": {"tmp36_temperature":{"time": [], "values": []},"OBC_temperature":{"time": [],"values": []},
        "probe_temperature":{"time": [], "values": []},"pressure":{"time": [],"values": []}}},json_file,indent=2)
class SystemStatus:
    def __init__(self):
        self.current_mode = 'PowerOff'
        self.log = Logger() 
            
        
    def update_mode(self,mode,mode2):
        dict = {'Initialization':['power_operations',"\nInitialization complete"],'PowerOff':["power_operations",'\nPower is Off'],
                'PowerOn':['power_operations','\nStarting sequence finished'],'Nominal':['measurement_operations','\nTrying to change the world'],
                'Transmission':['transmission_operations','transmission complete'],'DataAnalysis':['data_analysis_operations','Data analysis complete'], }
        self.log.log_info(dict[mode][0],dict[mode][1])
        self.current_mode = mode
        

        
if __name__ == '__main__' :   
    test = Logger()
    #test.log_values("tmp36_temperature",28)
    test.json_cleaning()
    #test.log_info("transmission_operations","tout va bien,mais pas trop")
    #test2 = SystemStatus()
    #test2.set_mode('Intialization')


