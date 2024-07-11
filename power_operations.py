class PowerManager:
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
            

    def handle_power_on(self):
        # Perform the power on sequence, after booting
        # ........
        self.logger.log_info("power_operations","Initialization start")
        self.run_initialization_sequence()
        self.system.set_mode('Initialization')
        
    
    def handle_scheduled_shutdown(self):
        # Perform the scheduled shutdown sequence
        # ........
        self.logger.log_info("power_operations","Scheduled shutdown")
        self.system.set_mode("PowerOff")
        # os.system("shutdown /s /t time")
        self.run_shutdown_sequence()
    
    def handle_critical_shutdown(self):
        # Perform the critical shutdown sequence
        # ........
        self.critical = True
        self.logger.log_info("power_operations","Critical shutdown") # add hour
        self.system.set_mode('PowerOff')
        self.run_shutdown_sequence()
    
    def run_initialization_sequence(self):
        # Perform initialization steps
        # ..........
        time.sleep(5)
        self.logger.log_info("power_operations","Initialization complete")
        self.system.set_mode('Nominal')
    
    def run_shutdown_sequence(self):
        # Perform shutdown steps
        # .......
        self.logger.log_info("power_operations","Shutdown complete")

if __name__ ==  '__main__':
    test0 = PowerManager()
