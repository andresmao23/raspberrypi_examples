import RPi.GPIO as GPIO
import time

led_pin = 4
delay = 0.1

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)
"""
# Ciclo que permite controlar el brillo del led desde el teclado

while True:
    duty_s = input("Enter Brightness (0 to 100):")
    duty = int(duty_s)
    pwm_led.ChangeDutyCycle(duty)"""

while True:
    # Encendido gradual
    for duty in range(100):
        time.sleep(delay)
        #print (duty)
        pwm_led.ChangeDutyCycle(duty)

    # Apagado gradual
    for duty in range(100,-1,-1):
        time.sleep(delay)
        #print (duty)
        pwm_led.ChangeDutyCycle(duty)
