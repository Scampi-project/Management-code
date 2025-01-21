import time
from Utils import Logger, SystemStatus
from gc import collect
import os
import json
from datetime import datetime,timedelta
from nominal_operations import NominalOperations
from measurement_operations import MeasurementManager

class PowerManager:
    def __init__(self,critical_shutdown=False,scheduled_shutdown=False):
        self.nominal_ops = NominalOperations()
        self.logger = Logger()
        self.system = SystemStatus()
        self.time = "01-01 , 00:00:00"
        self.is_power_on = True
        self.critical = False
        if critical_shutdown:
            self.handle_critical_shutdown()
        if scheduled_shutdown:
            self.handle_scheduled_shutdown()
        
          
        
    def check_power_status(self):
        self.volt = 13 #Fake value
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
    
    def handle_scheduled_shutdown(self,date1,hour1,date2,hour2):
        if date1 != "11/10/2004" :
        # Perform the scheduled shutdown sequence
        # ........
        #Envoyer à un "interrupteur l'info de débrancher de telle date à telle date "
                self.logger.log_info("power_operations","Scheduled shutdown")
                self.system.set_mode("PowerOn","PowerOff")
                self.run_shutdown_sequence()
        else:
                print("cela a marché")
    
    def handle_critical_shutdown(self):
        # Perform the critical shutdown sequence
        # ........
        self.critical = True
        self. logger.log_info("power_operations","Critical shutdown") # add hour
        self.system.update_mode("PowerOn",'PowerOff')
        self.run_shutdown_sequence()
    
    def run_initialization_sequence(self,measure):
        self.measure = measure
        self.logger.log_info(f"power_operations",f"mode is shifting from 'PowerOff' to 'PowerOn'")
        self.check_power_status()
        self.system.update_mode('PowerOn','Initialization')
        self.logger.log_info(f"power_operations",f"mode is shifting from 'Power On' to Initialization")
        self.measure.perform_sensors_measurements()
        self.nominal_ops.perform_nominal_operations(self.measure.inside_temp)
        self.time = time.time()
        
        #Maybe add camera photo date comparaison
        self.json_file = open("/home/pi/SCAMPI/Sensors/sensors_values.json",'r')
        #self.json_file = open("C:/Users/benja/Documents/AERO_2/STAGE/SCAMPI/Management/sensors_values.json","r")
        #self.txt = json.load(self.json_file)
        #self.tmp36 = datetime.strptime(self.txt["sensors"]['tmp36_temperature']["time"][-1],"%d-%m , %H:%M:%S")
        #self.OBC = datetime.strptime(self.txt["sensors"]["OBC_temperature"]["time"][-1],"%d-%m , %H:%M:%S")
        #self.pressure = datetime.strptime(self.txt["sensors"]["pressure"]["time"][-1],"%d-%m , %H:%M:%S")
        #self.delta  = self.time - self.tmp36
        #self.delta1  = self.time - self.OBC
        #self.delta2 = self.time - self.pressure
        #time comparasion
        #self.delta = (self.delta.days*3600 + self.delta.seconds)/60
        #self.delta1 = (self.delta1.days*3600 + self.delta1.seconds)/60
        #self.delta2 = (self.delta2.days*3600 + self.delta2.seconds)/60
        #self.check = True
        #if self.delta> 30 :
        #        self.logger.log_info("measurement_operation",f"tmp36 sensor stop to take measure\nlast measure : {self.tmp36}")
        #        self.check = False
        #if self.delta1> 5 :
        #        self.logger.log_info("measurement_operation",f"missing data OBC temp\nlast measure : {self.OBC}")
        #        self.check = False
        #if self.delta2> 30 :
        #       self.logger.log_info("measurement_operation",f"missing data pressure \nlast measure : {self.pressure}")
        #       self.check = False
        #if self.check:
        #        self.logger.log_info("measurement_operation","sensors data: fine\n collecting garbage...")
        #        collect()
        time.sleep(5)
        self.system.update_mode('Initialization','Nominal')
        self.logger.log_info(f"power_operations",f"mode is shifting from 'Initialization' to 'Nominal'")
    
    def run_shutdown_sequence(self):
        # Perform shutdown steps
        self.time = datetime.now().strftime("%d-%m , %H:%M:%S")
        self.time = datetime.strptime(self.time,"%d-%m , %H:%M:%S")
        self.logger.log_info("power_operations","Shutdown complete")
        # os.system("shutdown /s /t time")
if __name__ ==  '__main__':
    test0 = PowerManager()
    test0.run_shutdown_sequence()
    test0.run_initialization_sequence()
