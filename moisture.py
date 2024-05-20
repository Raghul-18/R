import RPi.GPIO as gp 
gp.setmode (gp.BOARD) 
gp.setup(8,gp.IN) 
while True: 
try: 
print(not gp.input(8)) 
except : 
gp.cleanup()
