import RPi.GPIO as GPIO 
import time 
GPIO.setmode(GPIO.BOARD) 
GPIO.seetup(40,GPIO.OUT) 
GPIO.seetup(38,GPIO.OUT) 
while True: 
GPIO.output(40,True) 
GPIO.output(38,False) 
print(“LED 1 ON”) 
print(“LED 2 OFF”) 
Time.sleep(2) 
GPIO.output(40,False) 
GPIO.output(38,True) 
print(“LED 1 OFF”) 
print(“LED 2 ON”) 
Time.sleep(2)
