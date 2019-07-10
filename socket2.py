import RPi.GPIO as GPIO
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.8.133", 2020))
s.listen(10)
sc,addr = s.accept()
print("Cliente: ", addr)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
continuar = True
parp      = True

while continuar == True:
    mensaje = sc.recv(64)
    m = str(mensaje)[2]
    print("Letra recibida: ", m)
    if m == "a":
        GPIO.output(2,GPIO.HIGH)
        
    elif m == "b":
        GPIO.output(2,GPIO.LOW)
        
    elif m == "d":
        for i in range(10):
            GPIO.output(2,GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(2,GPIO.LOW)
            time.sleep(0.25)
            
    if m == "c":
        continuar = False

sc.close()
s.close()
print("Fin del programa")
