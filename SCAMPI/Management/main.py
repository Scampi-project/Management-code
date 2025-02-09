#Author : Benjamin PONTY, modified by : Viren OLLIVIER
import datetime
from power_operations import PowerManager
from nominal_operations import NominalOperations
from measurement_operations import MeasurementManager
from DataAnalysis import DataAnalysis
# from transmission_operations import TransmissionManager
from Utils import Logger, SystemStatus
import threading
import tkinter
from datetime import datetime
import json

class Main:
    path="/home/pi1/SCAMPI/sensors_values.json",
    def __init__(self):
        # Initialize all modules
        self.power_manager = PowerManager()
        self.nominal_ops = NominalOperations()
        self.measure = MeasurementManager()
        self.systate = SystemStatus()
        self.data_analysis = DataAnalysis()
        # transmission_manager = TransmissionManager()
        self.log = Logger()
        self.power_manager.run_initialization_sequence(self.measure)
        with open(path, 'r') as file :
            self.txt = json.load(file)
            file.close()
        self.delatacount = (datetime.now()-datetime.strptime(self.txt["shutdown"][-1],"%d-%m , %H:%M:%S")).total_seconds()//300 #tranche de 5min
    def main_loop(self) :
        with open(path, 'r') as file :
            self.txt = json.load(file)
            file.close()
        self.count= self.txt["count"]+selfdeltacount
        self.measure.perform_sensors_measurements() #mesures initiales
        self.camera.capture_photo()
        self.camera.capture_video(True) #When starting take a long video
        # Main loop
        while True:
            try:
       
               
                     
                # Perform measurements if in Measurement mode
                # if self.systate.current_mode == 'Measurement':
                    # self.measurement_manager.perform_measurements()
                # Perform data analysis and recording if in Data Analysis mode
                #if self.systate.current_mode == 'DataAnalysis':
                #     self.data_analyzer.analyze_and_record_data()
                

                # # Perform data transmission if in Transmission mode
                # if self.systate.current_mode == 'Transmission':
                #     transmission_manager.transmit_data()
                
                
                #waiting 5 min for recording new data 
                time.sleep(300.0) 
                self.count +=1
                
                with open(path, 'r') as file :
                        self.txt = json.load(file)
                        file.close()
                        
                self.txt["count"]+=1
                with open(path, 'r') as file :
                        json.dump(self.txt,file)
                        file.close()
                
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
                #if self.systate.current_mode == 'DataAnalysis':
                #     self.data_analyzer.analyze_and_record_data()
                

                # # Perform data transmission if in Transmission mode
                # if self.systate.current_mode == 'Transmission':
                #     transmission_manager.transmit_data()
                  
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
    def bouton6(self):
        self.measure.measure_external_temp()
    def bouton7(self):
        self.measure.measure_OBC_temp()
    def bouton8(self):
        self.measure.read_probe()
    
    def valider(self):
        a=int(self.entree.get())
        self.measure.record_photos(auto=False, focus_length=a)
	

        
    def menu(self):
        window = tkinter.Tk()
        window.geometry("800x800")
        window.title("Command Menu")
        #CAMERA PART
        focus= tkinter.Label(text="focus length in cm")
        self.entree=tkinter.Entry()
        bouton=tkinter.Button(text="valid",command=self.valider)
        focus.pack()
        self.entree.pack()
        bouton.pack()
        cam_lab = tkinter.Label (text = "Camera management")
        button = tkinter.Button(text = "Take a picture (auto focus)",command=self.bouton)
        button1 = tkinter.Button(text = "Take a short video",command=self.bouton1)
        button2 = tkinter.Button(text = "Take a long video",command=self.bouton2)
        cam_lab.place(x=100,y=100)
        button1.place(x=50,y=160)
        button2.place(x=190,y=160)
        button.place(x=100,y=200)
        focus.place(x=130,y=240)
        self.entree.place(x=100,y=260)
        bouton.place(x=170,y=280)
        #SET MODE PART
        set_mode = tkinter.Label (text = "Mode management")
        button3 = tkinter.Button(text = "Nominal",command=self.bouton3)
        button4 = tkinter.Button(text = "Transmission",command=self.bouton4)
        button5 = tkinter.Button(text = "Data Analysis",command=self.bouton5)
        set_mode.place(x=500,y=100)
        button3.place(x=460,y=160)
        button4.place(x=560,y=160)
        button5.place(x=560,y=190)
        #temperature part
        temp_lab = tkinter.Label (text = "Temperature and pressure management")
        temp_lab.place(x=250,y=400)
        button6 = tkinter.Button(text = "external temperature",command=self.bouton6)
        button6.place(x=100,y=420)
        button7 = tkinter.Button(text = "OBC temperature",command=self.bouton7)
        button7.place(x=300,y=420)
        button8 = tkinter.Button(text = "probe temperature and pressure",command=self.bouton8)
        button8.place(x=500,y=420)
        window.mainloop() 

if __name__ == "__main__":
    test= Main()
    #thread1 = threading.Thread(target=test.main_loop)
    thread2 = threading.Thread(target=test.menu)

    #thread1.start()
    thread2.start()
 
