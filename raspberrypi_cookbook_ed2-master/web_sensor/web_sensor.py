import os, time, smtplib
from bottle import route, run, template

USUARIO_GMAIL = 'cmauricio10@gmail.com'
CONTRASENA_GMAIL = 'robinho10'
DESTINATARIO = 'amcaicedo@unimayor.edu.co'
REMITENTE = 'cmauricio10@gmail.com'
ASUNTO  = 'Alarma Raspberry Pi'
MENSAJE = 'Se produjo un incremento importante en la temperatura, favor revisar!!! Temperatura mayor a 55 grados centigrados'

def enviarCorreoElectronico():
    print("Enviando correo electronico!!!")
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

"""
GMAIL_USER = 'cmauricio10@gmail.com' 
GMAIL_PASS = 'robinho10' 
SMTP_SERVER = 'smtp.gmail.com' 
SMTP_PORT = 587

def send_email(recipient, subject, text): 
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT) 
    smtpserver.ehlo() 
    smtpserver.starttls() 
    smtpserver.ehlo 
    smtpserver.login(GMAIL_USER, GMAIL_PASS) 
    header = 'To:' + recipient + '\n' + 'From: ' + GMAIL_USER 
    header = header + '\n' + 'Subject:' + subject + '\n' 
    msg = header + '\n' + text + ' \n\n' 
    smtpserver.sendmail(GMAIL_USER, recipient, msg) 
    smtpserver.close()"""

def cpu_temp():
    dev = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cpu_temp = dev.read()[5:-3]
    print(cpu_temp)    
    if float(cpu_temp) > 55.0:
	enviarCorreoElectronico()
	#send_email('amcaicedo@unimayor.edu.co', 'Temperatura Raspberry Pi', 'Aumento en la temperatura de la CPU...')
	#print("Enviando correo electronico")
    return cpu_temp

@route('/temp')
def temp():
    return cpu_temp()
	
@route('/')
def index():
    return template('main.html')
	
@route('/raphael')
def index():
    return template('raphael.2.1.0.min.js')

@route('/justgage')
def index():
    return template('justgage.1.0.1.min.js')

run(host='0.0.0.0', port=80)
