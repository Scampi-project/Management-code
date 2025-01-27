import json
from Utils import Logger, SystemStatus

class DataAnalysis :
    path="/home/pi1/SCAMPI/sensors_values.json"
    def __init__(self):
        self.log = Logger()
        
        
    def mean_std(self,sensor):
        with open(path, 'r') as file :
            self.txt = json.load(file)
            file.close()
        if len(self.txt["sensors"][sensor]["values"])<5 :
            self.log.log_info("DataAnalysis",f"Not enough measures for {sensor}")
            self.log.log_info("errors",f"Not enough measures for {sensor}")
        else :   
            self.mean=0
            for i in range (5):
                self.mean+=self.txt["sensors"][sensor]["values"][-i-1]
            self.mean=self.mean/5
            self.std=0
            for i in range(5):
                self.std+=(self.txt["sensors"][sensor]["values"][-i-1]-self.mean)**2
            self.std=self.std**(1/2)        
            self.log.log_info("DataAnalysis",f"mean_{sensor}_5-last-measures : {self.mean}") 
            self.log.log_info("DataAnalysis",f"standard-deviation_{sensor}_5-last-measures : {self.std}")
    

if __name__ ==  '__main__':
    test=DataAnalysis()
    test.mean_std("tmp36_temperature")
    

