import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio)

words = set()

@sio.event
def connect(sid, environ):
    print('connect ', sid)

def updateTeams(sid, teams):
    print('teams ', teams)
    sio.emit('updateTeams', teams)

def tick(sid, sec):
    print(f'time {sec}s')
    sio.emit('tick', sec)

@sio.event
def wordAction(sid, word, guess):
    print(f'{word} is {"" if guess else "not"} guessed')

def endRound(sid):
    print('end round')
    sio.emit('endRound')

def wordNew(sid, word):
    print('new word ', word)
    sio.emit('wordNew', word)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

def uploadWords():
    with open('alias/words.txt') as f:
        lines = f.readlines()
    global words
    for l in lines:
        words.add(l)

if __name__ == '__main__':
    uploadWords()
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)