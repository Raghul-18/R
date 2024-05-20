import RPi.GPIO as GPIO 
import time 
GPIO.setmode(GPIO.BOARD) 
GPIO.seetup(40,GPIO.OUT) 
while True: 
GPIO.output(40,True) 
print(“Beep”) 
Time.sleep(2) 
GPIO.output(40,False) 
print(“No Beep”) 
