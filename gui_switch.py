from tkinter import *
import RPi.GPIO as GPIO
import time

led_pin = 4
tv_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(tv_pin, GPIO.OUT)

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.check_var_led = BooleanVar()
        self.check_var_tv = BooleanVar()
        led_check = Checkbutton(frame, text='Pin Led (Pin 4)',
                            command=self.encender_led,
                            variable=self.check_var_led, onvalue=True, offvalue=False)
        tv_check = Checkbutton(frame, text='Pin TV (Pin 17)',
                            command=self.encender_tv,
                            variable=self.check_var_tv, onvalue=True, offvalue=False)
        led_check.grid(row=0, column=0)
        tv_check.grid(row=1, column=0)
        
    def encender_led(self):
        GPIO.output(led_pin, self.check_var_led.get())
        
    def encender_tv(self):
        GPIO.output(tv_pin, self.check_var_tv.get())

root = Tk()
root.wm_title('TABLERO DE CONTROL')
app = App(root)
root.geometry("350x50+0+0")
root.mainloop()
