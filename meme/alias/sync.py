import socketio
from time import sleep
sio = socketio.Client()
isInit = False

def clientInit(url):
    global isInit
    if isInit:
        return
    n = 5
    for i in range(n):
        try:
            sio.connect(url)
            isInit = True
            break
        except Exception:
            print('Socker Server not found!\nSleeping...')
            sleep(1)
    else:
        raise ConnectionError('Socket Server not found!')
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
