import time
from Utils import Logger, SystemStatus
import sys
sys.path.insert(1,"/home/pi/SCAMPI/Sensors")
from readT_P import T_P_probe
from camera import Camera
from temperature import Temperature
class MeasurementManager:
    def __init__(self):
        self.log = Logger()
        self.camera = Camera()
        self.tempressure= T_P_probe()
        self.temp = Temperature()

    def perform_sensors_measurements(self):
        self.log.log_info("measurement_operation","Performing measurements")
        self.measure_external_temp()
        self.measure_abiotic_factors(17)
        self.record_photos()
        self.record_videos(True) #When starting take a long video
        
    def measure_external_temp(self):
        self.temp.get_temperature()
        

    def measure_abiotic_factors(self,pin):
        #self.tempressure.readProbe("<pin number>") 
        self.tempressure.readProbe(17)
        self.pressure = self.tempressure.pressure
        self.inside_temp = self.tempressure.inside_temp  
        
    """Fake input to emulate the temperature reading"""
    def record_photos(self):
        self.camera.capture_photo()
        # Record videos and take photos
        # ........
    def record_videos(self,Long=False):
        self.camera.capture_video(Long)
if __name__ == "__main__":
    test = MeasurementManager()
    test.measure_external_temp()
