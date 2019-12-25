const http = require("http");
const server_socket_io = http.createServer();
const io = require("socket.io")(server_socket_io);

const users = [];
const server_django = new http.Server(function (req, res) {
  let userdata = '';
  res.setHeader('Content-Type', 'application/json');
  req.on('data', (data) => {
    userdata += data;
  });
  req.on('end', () => {
    var result = "";
    for (var i = 0; i < userdata.length; i++) {
      result += String.fromCharCode(parseInt(userdata[i], 2));
    }

    updateUsers(result);
    userdata = {};
  });
});
server_django.listen(3030);

io.on("connection", client => {
  client.on("event", event);
  client.on("disconnect", disconnect);
  console.log("Client connected");
  io.emit("update");
});
server_socket_io.listen(3000);

function disconnect() { }

function event(data) {
  io.send(data);
}

function updateUsers(data) {
  return '';
  const user = users.find((e, i, a) => { e.username === data.username });
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
      user['logout_time'] = date.time;
    else if (data.action === 'login')
      user['login_time'] = date.time;
    users.push(user);
  }

  event(users);
}
