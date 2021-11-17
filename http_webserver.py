
import RPi.GPIO as GPIO
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = " " # Ip address of rasberry pi.
host_port = 8000

def setupGPIO(): #setup pins
    GPIO.setmode(GPIO.BCM) #or BOARD
    GPIO.setup() #sets pinmode setip([pin[], GPIO.IN/GPIO.OUT])
    #digitalWrite is GPIO.output(18,GPIO.HIGH)
    #GPIO.PWN([pin],[frequency])
    #To adjust pwm use pwm.ChangeDutyCycle(percent)
    #to turn PWM off, use pwm.stop()
    





def 



####### Main #######

if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()