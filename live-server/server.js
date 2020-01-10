const server = require("http").createServer();
const io = require("socket.io")(server);
const fs = require('fs');

let words = new Set();
let teams = {};
let clients = new Set();
uploadWords(words);

io.on("connection", client => {
  clients.add(client);
  console.log("Client connected");
  client.on("disconnect", ()=>{disconnect(client);});

  client.on("createTeam", createTeam);
  client.on("appendTeam", appendTeam);
  client.on("wordAction", wordAction);
});
server.listen(5000);

function disconnect(client) {
  console.log("Client disconnected");
  clients.delete(client);
}

function emitEvent(name, data) {
  clients.forEach((c, n, s) => { c.emit(name, data); });
}

function createTeam(data) {
  console.log(`user ${data["user"]} create ${data["team"]}`);
  teams[data["user"]] = data["team"];
  updateTeams();
}

function appendTeam(data) {
  console.log(`user ${data["user"]} append ${data["team"]}`);
}

function wordAction(word, guess) {
  console.log(`${word} is ${guess ? "" : "not"} guessed`);
}

function uploadWords(words) {

  fs.readFile('alias\\words.txt', 'utf8', (err, data) => {
    if (err) throw err;
    data.toString().split('\n').forEach((v, i, a) => { words.add(v); });
  });
}

function updateTeams() {
  console.log('teams ', teams);
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