import os

class Logger:

    def log_info(self,name,txt):
        os.chdir("C:/Users/benja/Documents/AERO_2/STAGE/SCAMPI/Management") #A modifier avec le chemin du raspberry
        #os.chdir("/home/pi/SCAMPI/Management")
        file = open(f"./{name}.log",'a')
        file.write(f'\n{txt}')
        file.close()
        print(f"j'ai écrit {txt}")

class SystemStatus:
    def __init__(self):
        self.current_mode = 'PowerOff'
        self.log = Logger()
    def set_mode(self,mode,critical=False) :
        if mode == 'Initialization':
            # cleaning ram with garbage collector
            if critical == False :
                self.log_cleaning()
            # os.system("source /home/pi/env/bin/activate")
            self.current_mode = mode
            self.log.log_info("power_operations","Initialization complete")
        if mode == 'PowerOff':
            file = open(f"./power_operations.log",'a')
            self.current_mode = mode
            file.write(f'\nPower is Off')
        if mode == 'PowerOn':
            file = open(f"./power_operations.log",'a')
            self.current_mode = mode
            file.write(f'\nPower is On')

        if mode == 'Nominal':
            self.current_mode = mode
            print('Trying to change the world')
            
    def log_cleaning(self):
        print("heho")
        list = ['power_operations','nominal_operations','transmission_operations','measurement_operations','errors']
        for i in list :
            file = open(f"{i}.log","r+")
            file.truncate(0)
    def update_mode(self,mode):
        self.log.log_info(f"power_operations",f"mode is changing from {self.current_mode} to {mode}")
        
   

        
if __name__ == '__main__' :   
    test = Logger()
    test.log_info("transmission_operations","tout va bien,mais pas rtrop")
    test2 = SystemStatus()
    test2.set_mode('Intialization')


