
from time import sleep
import RPi.GPIO as GPIO
import board
import adafruit_mpu6050




def range(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)


i2c = board.I2C()  # uses board.SCL and board.SDA
mpu = adafruit_mpu6050.MPU6050(i2c)
Device_Address = 0x68 


servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)
servo = GPIO.PWM(18,50)
servo.start(0)


sleep(1)





mpu.accelerometer_range(8)#2_G,4_G,8_G,16_G
mpu.gyro_range(500);#250,500,1000,2000
mpu.filter_bandwidth(21)

sleep(1)



while True:


# Get new sensor events with the readings 
 acc_x, acc_y, acc_z =  mpu.acceleration()

 acc_y =range(acc_y,-10,10,180,0) 

 servo.start(acc_y)


 sleep(.01)

