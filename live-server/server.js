const server = require("http").createServer();
const io = require("socket.io")(server);
const users = [];

io.on("connection", client => {
  client.on("event", event);
  client.on("disconnect", disconnect);
  console.log("Client connected");
  io.emit("update");
});
server.listen(3000);

function disconnect() {}

function event(data) {
  io.send();
}

function updateUsers() {}
