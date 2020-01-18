import socketio
from time import sleep
sio = socketio.Client()
while True:
    try:
        sio.connect('http://localhost:5000')
        break
    except Exception:
        sleep(1)
teams = []

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error():
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")

def createTeam(data):
    global sio
    teams.append(data)
    print(f'user {data["user"]} create {data["team"]}')
    sio.emit('createTeam', data)

@sio.on('createTeamPress')
def createTeamPress(data):
    print('createTeamPress')
    createTeam(data)

@sio.event
def event(data):
    print('event')
