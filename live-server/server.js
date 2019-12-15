const server = require("http").createServer();
const io = require("socket.io")(server);
const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('../meme/meme/db.sqlite3');
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

function updateUsers() {
  
}
