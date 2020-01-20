const server = require("http").createServer();
const io = require("socket.io")(server);
const fs = require('fs');

let words = new Set();
let teams = {};
let clients = [];
uploadWords(words);

io.on("connection", function (client) {
  clients.push(client);
  updateTeams();
  console.log(`Client ${client.id} connected`);
  client.on("disconnect", () => { disconnect(client); });
  client.on("createTeam", createTeam);
  client.on("joinTeam", joinTeam);
  client.on("wordAction", wordAction);
});
server.listen(5000);

function disconnect(client) {
  console.log(`Client ${client} disconnected`);
  const index = clients.indexOf(client);
  clients.splice(index, 1);
}

function emitEvent(name, data) {
  clients.forEach(client => {
    client.emit(name, data);
  });
}

function createTeam(data) {
  let user = Object.keys(data)[0];
  let name = data[user];
  console.log(`user ${user} create ${name}`);
  teams[user] = name;
  updateTeams();
}

function joinTeam(data) {
  console.log(`user ${data["user"]} append ${data["team"]}`);
}

function wordAction(word, guess) {
  console.log(`${word} is ${guess ? "" : "not"} guessed`);
}

function uploadWords(words) {

  fs.readFile('alias\\data\\words.txt', 'utf8', (err, data) => {
    if (err) throw err;
    data.toString().split('\n').forEach((v, i, a) => { words.add(v); });
  });
}

function updateTeams() {
  console.log(`teams ${teams.toString()}`);
  emitEvent('updateTeams', teams);
}

function tick(sec) {
  console.log(`time ${sec}s`);
  emitEvent('tick', sec);
}

function endRound() {
  console.log('end round');
  emitEvent('endRound');
}

function wordNew(word) {
  console.log('new word ', word);
  emitEvent('wordNew', word);
}