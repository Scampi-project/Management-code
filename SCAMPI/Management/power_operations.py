import time
from Utils import Logger, SystemStatus
from gc import collect
import os
import json
from datetime import datetime

class PowerManager:
    path = r'/home/pi1/SCAMPI/sensors_values.json'
    def __init__(self,critical_shutdown=False,scheduled_shutdown=False):
        self.logger = Logger()
        self.system = SystemStatus()
        self.is_power_on = True
        self.critical = False
        if critical_shutdown:
            self.handle_critical_shutdown()
        if scheduled_shutdown:
            self.handle_scheduled_shutdown()
        
          
        
    def check_power_status(self):
        self.system.update_mode('PowerOn')
        self.volt = 3 #Fake value
        self.ampere = 1 #Fake value
        self.check = True
        # Check power status and handle transitions
        if 2<self.volt<5 :
            self.logger.log_info("power_operations",f"Volt OK : V = {self.volt}V")
        else :
            self.logger.log_info("power_operations", f"Volt anomaly V = {self.volt}V")
            self.check = False
        if 0.5<self.ampere<1.5:
            self.logger.log_info("power_operations",f"Ampere A = {self.ampere}A")
        else :
            self.logger.log_info("power_operations", f"Ampere anomaly A ={self.ampere}A")
            self.check = False
        if self.check:
            self.logger.log_info("power_operations","Power is OK")
        else :
            self.handle_critical_shutdown() # Have to complete
            

    def handle_power_on(self):
       
        self.logger.log_info("power_operations","Initialization start")
        self.system.update_mode('Initialization')
        
        if os.path.exists(path) :
                with open(path, 'r') as file :
                        self.txt=json.load(file)
                if self.txt["sensors"]["tmp36_temperature"]["time"]==[]:
                        self.logger.log_info("power_operations","Initialization complete")
                        self.system.update_mode('Nominal')
                else :
                        self.run_initialization_sequence()
        else : 
                self.logger.json_cleaning()
                self.logger.log_info("power_operations","Initialization complete")
                self.system.update_mode('Nominal')

    def run_initialization_sequence(self):
        self.time = datetime.now()
        # Perform initialization steps
        with open(path, 'r') as file :
                self.txt = json.load(file)
                file.close()
        self.tmp36 = datetime.strptime(self.txt["sensors"]['tmp36_temperature']["time"][-1],"%d-%m , %H:%M:%S")
        self.OBC = datetime.strptime(self.txt["sensors"]["OBC_temperature"]["time"][-1],"%d-%m , %H:%M:%S")
        self.pressure = datetime.strptime(self.txt["sensors"]["pressure"]["time"][-1],"%d-%m , %H:%M:%S")
        self.delta  = self.time - self.tmp36
        self.delta1  = self.time - self.OBC
        self.delta2 = self.time - self.pressure
        #time comparasion
        self.delta = (self.delta.days*3600 + self.delta.seconds)/60
        self.delta1 = (self.delta1.days*3600 + self.delta1.seconds)/60
        self.delta2 = (self.delta2.days*3600 + self.delta2.seconds)/60
        self.check = True
        if self.delta> 30 :
                self.logger.log_info("measurement_operation",f"tmp36 sensor stop to take measure\nlast measure : {self.tmp36}")
                self.check = False
        if self.delta1> 5 :
                self.logger.log_info("measurement_operation",f"missing data OBC temp\nlast measure : {self.OBC}")
                self.check = False
        if self.delta2> 30 :
                self.logger.log_info("measurement_operation",f"missing data pressure \nlast measure : {self.pressure}")
                self.check = False
        if self.check:
                self.logger.log_info("measurement_operation","sensors data: fine\n collecting garbage...")
                collect()
                
        #Maybe add camera photo date comparaison
        
        time.sleep(5)
        self.logger.log_info("power_operations","Initialization complete")
        self.system.update_mode('Nominal')
        
        
    """
    def handle_scheduled_shutdown(self):
        # Perform the scheduled shutdown sequence
        # ........
        self.logger.log_info("power_operations","Scheduled shutdown")
        self.system.update_mode("PowerOff")
        self.run_shutdown_sequence()
    """
    def handle_critical_shutdown(self):
        self.critical = True
        self.time= datetime.now().strftime("%d-%m , %H:%M:%S")
        self.logger.log_info("power_operations",f"Critical shutdown {self.time} ") # add hour
        self.system.update_mode("PowerOff")
        self.run_shutdown_sequence()
    
    def run_shutdown_sequence(self):
        # Perform shutdown steps
        #transmettre l'heure à la terre
        self.time = datetime.now().strftime("%d-%m , %H:%M:%S")
        json_file = open(path, 'r')
        self.txt = json.load(json_file)
        json_file.close()
        json_file = open(path, 'w')
        self.txt["shutdown"].append(self.time)
        json.dump(self.txt,json_file)
        json_file.close()
        self.logger.log_info("power_operations",f"Shutdown complete at {self.time}")
        os.system('shutdown now')
    
    
    
if __name__ ==  '__main__':
    test0 = PowerManager()
    #test0.run_shutdown_sequence()
    #test0.run_initialization_sequence()
    test0.handle_power_on()
