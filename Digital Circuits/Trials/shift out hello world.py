
import os
import sys
cwd=os.getcwd()

(setpath_,Using_IC)=os.path.split(cwd)
print setpath_
(setpath,Codes)=os.path.split(setpath_)
print setpath
sys.path.append(setpath) 

from Arduino.Arduino import Arduino

from time import sleep

class SIPO_IC:

    
    def __init__(self,baudrate):
        self.baudrate=baudrate
        self.setup()
        self.run()
        self.exit()


    def setup(self):
        
        self.obj_arduino=Arduino()
        self.port=self.obj_arduino.locateport()
        self.obj_arduino.open_serial(1,self.port,self.baudrate)

       # self.obj_icm=IC_methods(self.baudrate)

    def run(self):

        
        
        dataPin=11
        clockPin=9
        latchPin=10
        #inPin=5

        
        
        for x in range(0,256):
            
            
            

            self.obj_arduino.cmd_digital_out(1,latchPin,0) #So that the data is stored and not passed on to the output LEDs
            self.obj_arduino.cmd_shift_out(dataPin,clockPin,'MSBFIRST',x)
            self.obj_arduino.cmd_digital_out(1,latchPin,1) #So that the stored data is now passed on to the output LEDs
                                                            #and the output is obtained
            
            sleep(0.5)

            
            

    
        
        
    def exit(self):
        self.obj_arduino.close_serial()

    


def main():
    sipo=SIPO_IC(115200)

if __name__=='__main__':
    main()
  
