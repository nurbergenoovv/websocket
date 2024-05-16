from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

# Переменная для хранения состояния (0 или 1)
device_status = 0

@app.route('/')
def index():
    return render_template('index.html', status=device_status)

@socketio.on('message')
def handle_message(msg):
    global device_status
    print('Received message:'+ msg)
    if msg == 'toggle':
        device_status = 1 if device_status == 0 else 0
        send(device_status, broadcast=True)
    else:
        send(device_status, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
