import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

while True:
    print("Solenoide activado!")
    GPIO.output(2,GPIO.HIGH)
    time.sleep(10)
    print("Solenoide desactivado!")
    GPIO.output(2,GPIO.LOW)
    time.sleep(10)
