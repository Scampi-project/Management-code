import time
from utils import Logger, SystemStatus

class NominalOperations:
    def __init__(self):
        self.logger = Logger()

    def perform_nominal_operations(self):
        self.logger.log_info("Performing nominal operations")
        self.monitor_obc_status()
        self.control_led_panels()
        # Any actions ? Updates ? 
    
    def monitor_obc_status(self):
        # Monitor temperature, current, etc.
        obc_temp = self.get_obc_temperature()
        obc_current = self.get_obc_current()
        # Tests here Temp high or low ? Critical temperature shutting down some services ? 
        # Error handling ? 
        # .....
        self.logger.log_info(f"OBC Temp: {obc_temp}, OBC Current: {obc_current}")
    
    def control_led_panels(self):
        # Control LED panels
        # ....
        return  2
    def get_obc_temperature(self):
        print(3)
        # getting temperature
        # ......
        return  2
    
    def get_obc_current(self):
        # Simulate getting current
        # .......
        return 2
        
        
  # .... Missing other error handling functions .... 