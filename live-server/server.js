const http = require("http");
const server_socket_io = http.createServer();
const io = require("socket.io")(server_socket_io);

const users = [];
let clients = [];
const server_django = new http.Server(function (req, res) {
  let userdata = '';
  res.setHeader('Content-Type', 'application/json');
  req.on('data', (data) => {
    userdata += data;
  });
  req.on('end', () => {
    // var result = userdata.split('&').map((p,i,r)=> { let x = p.split("=")[0]; { x:p.split("=")[1] }});
    const data = userdata.split('&');
    var result = {};
    for (let i = 0; i < data.length; i++) {
      kv = data[i].split('=');
      result[kv[0]] = kv[1];
    }
    updateUsers(result);
    userdata = '';
  });
});
server_django.listen(3030);

io.on("connection", client => {
  clients.push(client);
  console.log("Client connected");
  client.on("update", update)
  client.on("disconnect", disconnect);
});
server_socket_io.listen(3000);

function disconnect() {
  console.log("Client disconnected");
}

function update(data) {
  console.log("Update")
  updateUsers(data)
}

function event(data) {
  for (let i = 0; i < clients.length; i++)
    clients[i].emit("event", data);
}

function updateUsers(data) {
  if (data) {
    let user = users.find((e, i, a) => { e.username === data.username });
    if (user) {
      if (data.action === 'login') {
        user['login_time'] = data.time;
        user.active = true;
      }
      else if (data.action === 'logout') {
        user['logout_time'] = data.time;
        user.active = false;
      }
    }
    else {
      user = {
        'username': data.username,
        'active': data.action === 'logout',
        'logout_time': '',
        'login_time': ''
      }
      if (data.action === 'logout')
        user['logout_time'] = data.time;
      else if (data.action === 'login')
        user['login_time'] = data.time;
      users.push(user);
    }
  }
  event(users);
}
