from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import subprocess

app = Flask(__name__)
socketio = SocketIO(app)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# WebSocket route to handle CNC commands
@socketio.on('send_command')
def handle_command(data):
    command = data['command']
    try:
        # Replace this with your actual bCNC command execution
        result = subprocess.run(['python3', '-m', 'bCNC', command], capture_output=True, text=True)
        response = result.stdout if result.stdout else result.stderr
        emit('command_response', {'response': response})
    except Exception as e:
        emit('command_response', {'response': str(e)})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
