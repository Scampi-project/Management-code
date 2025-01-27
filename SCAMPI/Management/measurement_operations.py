import time
from Utils import Logger, SystemStatus
import sys
sys.path.insert(1,"/home/pi1/SCAMPI/Sensors")
from readT_P import T_P_probe
from camera import Camera
from temperature import Temperature
class MeasurementManager:
    def __init__(self):
        self.log = Logger()
        self.camera = Camera()
        self.probe= T_P_probe()
        self.temp = Temperature()

    def perform_sensors_measurements(self):
        self.log.log_info("measurement_operation","Performing measurements")
        self.measure_external_temp()
        self.measure_OBC_temp()
        self.read_probe()
        
    
    def measure_OBC_temp():
        self.temp.IR()
        
    def measure_external_temp(self):
        self.temp.tmp36()
	
    def read_probe(self):
        self.probe.read_measure()
	
    def record_photos(self,auto=True,focus_length=1000000):
        self.camera.capture_photo(auto,focus_length)
	
    def record_videos(self,Long=False):
        self.camera.capture_video(Long)

    def measure_abiotic_factors(self,pin):
        #self.tempressure.readProbe("<pin number>") 
        self.tempressure.readProbe(17)
        #self.pressure = self.tempressure.pressure
	    #self.inside_temp = self.tempressure.inside_temp  uncomment when sensors are connected
  
if __name__ == "__main__":
    test = MeasurementManager()
    test.perform_sensors_measurements()
