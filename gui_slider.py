from tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 500)
pwm.start(5)

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=100, orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)
        
    def update(self, duty):
        pwm.ChangeDutyCycle(float(duty))


root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("300x50+0+0")
root.mainloop()
            
