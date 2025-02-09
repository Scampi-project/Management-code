import time
from Utils import Logger, SystemStatus
import power_operations as po
import sys
sys.path.insert(1,"/home/pi/SCAMPI/Sensors")
from led_panel import Led_panel
from datetime import datetime
class NominalOperations:
    def __init__(self):
        self.log = Logger()
        self.lp = Led_panel()

    def perform_nominal_operations(self,inside_temp):
        self.log.log_info("nominal_operations","Performing nominal operations")
        self.monitor_obc_status()
        self.daylight_circle()
        time.sleep(5)
        self.lp.check_luminosity(inside_temp)
         
    def monitor_obc_status(self):
        # Monitor temperature, current, etc.
        self.get_obc_temperature()
        obc_current = self.get_obc_current()
        # Tests here Temp high or low ? Critical temperature shutting down some services ? 
        if self.obc_temp> 100 :
            self.log.log_info("nominal_operations",f"OBC Temp: {self.obc_temp} temperature is too high critical error, critical OBC shutdown\nOBC Current: {obc_current}")
            po.PowerManager(critical_shutdown=True)
        if self.obc_current< 12132 or self.obc_current>894598:#see which reel value to replace this fake one
            self.log.log_info("nominal_operations",f"OBC Current: {self.obc_current} temperature is too high critical error, critical OBC shutdown\nOBC Temp: {obc_temp}")
            po.PowerManager(critical_shutdown=True)
        # .....
        self.log.log_info("nominal_operations",f"OBC Temp: {self.obc_temp}, OBC Current: {self.obc_current}")
    
    def daylight_circle(self):
        self.current_hour = datetime.now().hour
        if 8 <= self.current_hour < 20:  # Between 8am and 8pm
            self.lp.turn_on()
        else :
            self.lp.turn_off()
    def get_obc_temperature(self):
        self.obc_temp = 50
        # getting temperature
        # ......
        self.log.log_values("OBC_temperature",50)#FAKE VALUE
    
    def get_obc_current(self):
        # Simulate getting current
        # .......
        self.obc_current = 15000
        
