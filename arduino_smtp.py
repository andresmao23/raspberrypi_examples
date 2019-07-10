import serial
import time
import smtplib


USUARIO_GMAIL = 'cmauricio10@gmail.com'
CONTRASENA_GMAIL = 'robinho10'

DESTINATARIO = 'amcaicedo@unimayor.edu.co'
REMITENTE = 'cmauricio10@gmail.com'

ASUNTO  = 'Alarma'
MENSAJE = 'Se produjo un cambio inesperado en la temperatura, favor revisar!!!'

arduino = serial.Serial('COM3', 9600, timeout = 3.0)    #Establece la comunicacion serial entre el arduino y el puerto COM3 del PC


 
def enviarCorreoElectronico():
    print("Enviando e-mail")
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)     
    smtpserver.ehlo()                                   
    smtpserver.starttls()                               
    smtpserver.ehlo()
    smtpserver.login(USUARIO_GMAIL, CONTRASENA_GMAIL)   
    header  = 'To:      ' + DESTINATARIO + '\n'               
    header += 'From:    ' + REMITENTE    + '\n'
    header += 'Subject: ' + ASUNTO       + '\n'
    print header
    msg = header + '\n' + MENSAJE + ' \n\n'             
    smtpserver.sendmail(REMITENTE, DESTINATARIO, msg)   
    smtpserver.close()	


	
while True:
    lineaLeida = arduino.readline()                  #Lee lo que llega por el puerto COM3 del PC                
    print(lineaLeida)                                #Inicialmente no imprime nada, cuando hay alarma en el sensor, se imprime la palabra ("Alarma!!!")
    print len(lineaLeida)	                         #Muestra la longitud de la cadena recibida por el puerto COM3 del PC ("Alarma!!!")
    if len(lineaLeida) != 0 :                        #Compara la longitud de la cadena enviada (0 = nada), (11 = alarma => llamar al metodo para enviar correo)
        enviarCorreoElectronico()
        break

		
# EOF
