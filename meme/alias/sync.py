import socketio

sio = socketio.Client()
isInit = False

@sio.event
def connect():
    print('connection established')

def createTeam(user, team):
    global sio
    print(f'user {user} create {team}')
    sio.emit('createTeam', {'user': user,'team':team})

@sio.event
def disconnect():
    print('disconnected from server')

def init():
    global sio
    global isInit
    if not isInit:
        sio.connect('http://localhost:5000')
        isInit = True