#Author : Benjamin PONTY
import time
from power_operations import PowerManager
from nominal_operations import NominalOperations
# from measurement_operations import MeasurementManager
# from data_analysis_operations import DataAnalyzerOperations
# from transmission_operations import TransmissionManager
from Utils import Logger, SystemStatus
import threading
class Main:
    def __init__(self):
        # Initialize all modules
        self.power_manager = PowerManager()
        self.nominal_ops = NominalOperations()
        # measurement_manager = MeasurementManager()
        self.systate = SystemStatus()
        # data_analyzer = DataAnalyzer()
        # transmission_manager = TransmissionManager()
        self.logger = Logger()


        self.systate.update_mode('PowerOn')
        self.power_manager.check_power_status()
        self.systate.set_mode('PowerOn') 
        self.systate.update_mode('Initialization')
        self.power_manager.handle_power_on()
        
        self.systate.set_mode('Initialization',self.power_manager.critical)
        self.power_manager.check_power_status()
        self.systate.update_mode('Nominal')
    def main_loop(self) :
        # Main loop
        while True:
            try:
                # Check and handle power status
                self.power_manager.check_power_status()
                # Perform nominal operations
                self.nominal_ops.perform_nominal_operations()
                ## Complete the transition of the System states ? 
                
                
                # Perform measurements if in Measurement mode
                # if self.systate.current_mode == 'Measurement':
                    # self.measurement_manager.perform_measurements()

                # Perform data analysis and recording if in Data Analysis mode
                # if self.systate.current_mode == 'DataAnalysis':
                #     self.data_analyzer.analyze_and_record_data()

                # # Perform data transmission if in Transmission mode
                # if self.systate.current_mode == 'Transmission':
                #     transmission_manager.transmit_data()
                time.sleep(10.0)   
            except Exception as e:
                self.logger.log_info("errors",f"Error in main loop: {str(e)}")
                # You need to expand on the error with the ones that are easy to handle.
#Should be greate to create an interface
    def set_status(self):
        while True :
            print("Here the mode you can set :\n\n    -Transmission\n    -DataAnalysis\n    -Measurement\n")
            self.systate.update_mode(input("choose a mode "))
         
 
        
    

if __name__ == "__main__":
    test= Main()
    thread1 = threading.Thread(target=test.main_loop)
    thread2 = threading.Thread(target=test.set_status)

    thread1.start()
    thread2.start()
 
