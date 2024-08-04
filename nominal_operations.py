import time
from Utils import Logger, SystemStatus
import power_operations as po

class NominalOperations:
    def __init__(self):
        self.log = Logger()
        

    def perform_nominal_operations(self):
        self.log.log_info("nominal_operations","Performing nominal operations")
        self.monitor_obc_status()
        self.control_led_panels()
        
    
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
    
    def control_led_panels(self):
        # Control LED panels
        # ....
        return  2
    def get_obc_temperature(self):
        self.obc_temp = 50
        # getting temperature
        # ......
        self.log.log_values("OBC_temperature",50)#FAKE VALUE
    
    def get_obc_current(self):
        # Simulate getting current
        # .......
        self.obc_current = 15000
        
        
  # .... Missing other error handling functions .... 
