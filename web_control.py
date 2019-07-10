from bottle import route, run, template
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led_pins = [4, 17]
led_states = [0, 0]

GPIO.setup(led_pins[0], GPIO.OUT)
GPIO.setup(led_pins[1], GPIO.OUT)

def html_for_led(led):
    l = str(led)
    result = " <input type='button' style='width:100px; height:60px' onClick='changed(" + l + ")' value='LED " + l + "'/>"
    return result

def update_leds():
    for i, value in enumerate(led_states):
        GPIO.output(led_pins[i], value)

@route('/')
@route('/<led>')
def index(led):
    if led >= '0' and led <= '9':
        led_num = int(led)
        led_states[led_num] = not led_states[led_num]
        update_leds()
        response = "<script>"
        response += "function changed(led)"
        response += "{"
        response += " window.location.href='/' + led"
        response += "}"
        response += "</script>"

        response += '<div align="center" style="width:100%; height:100%; background-color:gray;">'
        response += '<h1>TABLERO DE CONTROL GPIO</h1>'
        response += '<h2>DISPOSITIVOS</h2>'
        response += html_for_led(0)
        response += html_for_led(1)
        response += '<h3>Estado del LED 0: {{led0}}, Estado del LED 1: {{led1}}</h3>'
        response += '</div>'
        return template(response, led0=led_states[0], led1=led_states[1])
        #return response

try:
    run(host='0.0.0.0', port=80)
finally:
    print('\nCleaning up')
    GPIO.cleanup()
