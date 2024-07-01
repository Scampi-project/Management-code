import time
from utils import Logger, SystemStatus

class PowerManager:
    def __init__(self):
        self.logger = Logger()
        self.is_power_on = True
        self.handle_scheduled_shutdown = 2
        self.handle_critical_shutdown = 2
          
        
    def check_power_status(self):
        # Check power status and handle transitions
        y = 3
    
    def handle_power_on(self):
        # Perform the power on sequence, after booting
        # ........
        self.logger.log_info("Powering on")
        SystemStatus.set_mode('Initialization')
        self.run_initialization_sequence()
    
    def handle_scheduled_shutdown(self):
        # Perform the scheduled shutdown sequence
        # ........
        self.logger.log_info("Scheduled shutdown")
        SystemStatus.set_mode('PowerOff')
        self.run_shutdown_sequence()
    
    def handle_critical_shutdown(self):
        # Perform the critical shutdown sequence
        # ........
        self.logger.log_info("Critical shutdown")
        SystemStatus.set_mode('PowerOff')
        self.run_shutdown_sequence()
    
    def run_initialization_sequence(self):
        # Perform initialization steps
        # ..........
        time.sleep(5)
        self.logger.log_info("Initialization complete")
        SystemStatus.set_mode('Nominal')
    
    def run_shutdown_sequence(self):
        # Perform shutdown steps
        # .......
        self.logger.log_info("Shutdown complete")