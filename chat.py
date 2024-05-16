from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message')
def handle_message(msg):
    print('Received message:'+ msg)

if __name__ == '__main__':
    socketio.run(app, debug=True)
