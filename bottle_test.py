from bottle import route, run, template
from datetime import datetime

@route('/')
def index(name='time'):
    dt = datetime.now()
    time = "{:%Y-%m-%d %H:%M:%S}".format(dt)
    return template('<h1>Pi mao thinks the date/time is: {{t}}</h1>', t=time)

run(host='0.0.0.0', port=80)
