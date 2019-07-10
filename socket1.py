import RPi.GPIO as GPIO
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.1.106", 2020))
s.listen(10)
sc,addr = s.accept()
print("Cliente: ", addr)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
continuar = True

while continuar == True:
    mensaje = sc.recv(64)
    m = str(mensaje)[2]
    print("Letra recibida: ", m)
    if m == "a":
        GPIO.output(2,GPIO.HIGH)
    elif m == "b":
        GPIO.output(2,GPIO.LOW)
    if m == "c":
        continuar = False

sc.close()
s.close()
print("Fin del programa")
