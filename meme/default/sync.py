import datetime
import json

__socketIoUrl = 'http://localhost:3030'

def __error(r):
    print(f'Error {r.status}')

def syncLogin(username):
    time = datetime.datetime.now()
    r = requests.post(__socketIoUrl,
    headers={
        'Content-Type': 'application/json'
    },
    data={
        'action': 'login',
        'username': username,
        'time':time.strftime("%Y-%m-%d-%H.%M.%S")
        })
    if not r.ok:
        __error(r)

def syncLogout(username):
    time = datetime.datetime.now()
    r = requests.post(__socketIoUrl, 
    headers={
        'Content-Type': 'application/json'
    },
    data={
        'action': 'login',
        'username': username,
        'time':time.strftime("%Y-%m-%d-%H.%M.%S")
        })
    if not r.ok:
        __error(r)