import time 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


GPIO.setup(7, GPIO.OUT) # Connected to PWMA
GPIO.setup(11, GPIO.OUT) # Connected to AIN1
GPIO.setup(12, GPIO.OUT) # Connected to AIN2
GPIO.setup(13, GPIO.OUT) # Connected to STBY
GPIO.setup(15, GPIO.OUT) # Connected to BIN1
GPIO.setup(16, GPIO.OUT) # Connected to BIN2
GPIO.setup(18, GPIO.OUT) # Connected to PWMB


# Motor A on right side 
# Motor B on left side


#clockwise (foward)
 

#A
GPIO.output(11, GPIO.HIGH) 
GPIO.output(12, GPIO.LOW) 
#B
GPIO.output(15, GPIO.HIGH) 
GPIO.output(16, GPIO.LOW) 

time.sleep(0.2)

#Right

#A
GPIO.output(11, GPIO.LOW) 
GPIO.output(12, GPIO.HIGH) 
#B
GPIO.output(11, GPIO.HIGH) 
GPIO.output(12, GPIO.LOW) 

time.sleep(0.2)



#Left

#A
GPIO.output(11, GPIO.HIGH) 
GPIO.output(12, GPIO.LOW) 
#B
GPIO.output(11, GPIO.LOW) 
GPIO.output(12, GPIO.HIGH)

time.sleep(0.2)

#A
GPIO.output(11, GPIO.LOW) 
GPIO.output(12, GPIO.LOW) 
#B
GPIO.output(11, GPIO.LOW) 
GPIO.output(12, GPIO.LOW)

time.sleep(0.5)



# Counter-clockwise (Backwards)
#A
GPIO.output(11, GPIO.LOW) 
GPIO.output(12, GPIO.HIGH) 
#B
GPIO.output(11, GPIO.LOW) 
GPIO.output(12, GPIO.HIGH) 


#Turn off STBY
GPIO.output(13, GPIO.HIGH)


