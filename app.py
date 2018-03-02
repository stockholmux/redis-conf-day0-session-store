
from flask import Flask, session
from flask_session import Session
from flask import render_template
import os

app = Flask(__name__)
app.config.from_object(__name__)


port = os.getenv('APP_PORT',5000)
# port can come in as an int or a string, so we have to typecast
portInt = int(port)
portStr = str(port)
app.config['SECRET_KEY'] = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = 'sessions/'+portStr
Session(app)

# DRY: literals 
template = 'session.html'
sessionVar = 'value'

@app.route('/')
def index():
    if 'value' not in session:
        value =  ''
    else:
        value = '' if (session[sessionVar] is None) else session[sessionVar]
    return render_template(template, sessionvalue=value, port=portStr)

@app.route('/session/unset/')
@app.route('/session/set/<value>')
def sessionRoutes(value=None):
    session[sessionVar] = value
    return render_template(template, sessionvalue=value, port=portStr, sessionaction=('unsetting' if (value is None) else 'setting')+' session var')

if __name__ == "__main__":
    app.logger.info('starting... '+portStr)
    app.run(host=os.getenv('APP_HOST', '0.0.0.0'), port=portInt)
