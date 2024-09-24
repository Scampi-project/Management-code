#Author : Benjamin PONTY
import time
from power_operations import PowerManager
from nominal_operations import NominalOperations
from measurement_operations import MeasurementManager
# from data_analysis_operations import DataAnalyzerOperations
# from transmission_operations import TransmissionManager
from Utils import Logger, SystemStatus
import threading
import tkinter
class Main:
    def __init__(self):
        # Initialize all modules
        self.power_manager = PowerManager()
        self.nominal_ops = NominalOperations()
        self.measure = MeasurementManager()
        self.systate = SystemStatus()
        # data_analyzer = DataAnalyzer()
        # transmission_manager = TransmissionManager()
        self.log = Logger()


        self.systate.update_mode('PowerOn')
        self.power_manager.check_power_status()
        self.systate.set_mode('PowerOn') 
        self.systate.update_mode('Initialization')
        self.power_manager.handle_power_on()

        self.systate.set_mode('Initialization',self.power_manager.critical)
        self.systate.update_mode('Nominal')
        self.nominal_ops.perform_nominal_operations()
        self.measure.perform_sensors_measurements()
        self.time = time.time()
    def main_loop(self) :
        self.count = 1
        # Main loop
        while True:
            try:
                self.count +=1
                print("5 minutes se sont écoulées")
                # Check and handle power status
                self.power_manager.check_power_status()
                # Perform nominal operations
                 # OBC condition, waiting for 5min
                self.nominal_ops.perform_nominal_operations()
                if self.count%6 == 0: # temp & pressure condition, waiting for 30min
                    self.measure.perform_sensors_measurements()
                if self.count%12 == 0 : # short photo condition, waiting for 1h
                    self.measure.record_photos()
                if self.count%36 == 0: # short video condition, waiting for 30h
                    self.measure.record_videos()    
                if self.count%1440 == 0: # long video condition, waiting for 5days
                    self.measure.record_videos(True)    
                    
                # Perform measurements if in Measurement mode
                # if self.systate.current_mode == 'Measurement':
                    # self.measurement_manager.perform_measurements()
                # Perform data analysis and recording if in Data Analysis mode
                # if self.systate.current_mode == 'DataAnalysis':
                #     self.data_analyzer.analyze_and_record_data()

                # # Perform data transmission if in Transmission mode
                # if self.systate.current_mode == 'Transmission':
                #     transmission_manager.transmit_data()
                #waiting 5 min for recording new data 
                time.sleep(300.0)   
            except Exception as e:
                self.log.log_info("errors",f"Error in main loop: {str(e)}")
                # You need to expand on the error with the ones that are easy to handle.
        
    def bouton(self):
        self.measure.record_photos()
    def bouton1(self):
        self.measure.record_videos()
    def bouton2(self):
        self.measure.record_videos(True)
    def bouton3(self):
        self.systate.update_mode("Nominal")
    def bouton4(self):
        self.systate.update_mode("Transmission")
    def bouton5(self):
        self.systate.update_mode("Data_analysis")
        
    def menu(self):
        window = tkinter.Tk()
        window.geometry("800x800")
        window.title("Command Menu")
        #CAMERA PART
        cam_lab = tkinter.Label (text = "Camera management")
        button = tkinter.Button(text = "Take a picture",command=self.bouton)
        button1 = tkinter.Button(text = "Take a short video",command=self.bouton1)
        button2 = tkinter.Button(text = "Take a long video",command=self.bouton2)
        cam_lab.place(x=100,y=100)
        button.place(x=60,y=160)
        button1.place(x=180,y=160)
        button2.place(x=100,y=200)
        #SET MODE PART
        set_mode = tkinter.Label (text = "Mode management")
        button3 = tkinter.Button(text = "Nominal",command=self.bouton3)
        button4 = tkinter.Button(text = "Transmission",command=self.bouton4)
        button5 = tkinter.Button(text = "Data Analysis",command=self.bouton5)
        set_mode.place(x=500,y=100)
        button3.place(x=460,y=160)
        button4.place(x=560,y=160)
        button5.place(x=560,y=190)
        # SCHEDULED PART 
        scheduled = tkinter.Label (text = "Scheduled Power Off")
        from_ = tkinter.Label (text = "from")
        to = tkinter.Label (text = "to")
        
        start = tkinter.Entry(width=10)
        start.insert(0,"11/10/2004")
        
        start_heure = tkinter.Entry(width=5)   
        start_heure.insert(0,"11h11")
        
        end = tkinter.Entry(width=10)
        end.insert(0,"19/10/2004")
        
        end_heure = tkinter.Entry(width=5)  
        end_heure.insert(0,"11h11")   
          
        
        scheduled.place(x=100,y=300)
        start.place(x=60,y=360)
        from_.place(x=20,y=360)
        to.place(x=155, y= 360)
        end.place(x=180,y=360)
        start_heure.place(x=80,y=390)
        end_heure.place(x=200,y=390)
        self.power_manager.handle_scheduled_shutdown(start.get(),start_heure.get(),end.get(),end_heure.get())
        window.mainloop() 

if __name__ == "__main__":
    test= Main()
    thread1 = threading.Thread(target=test.main_loop)
    thread2 = threading.Thread(target=test.menu)

    thread1.start()
    thread2.start()
 
