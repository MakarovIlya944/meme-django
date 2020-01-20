import io from "socket.io-client";
const socket = io("http://localhost:5000");

socket.on("connect", _ => {
  console.log(`Client ${socket.id} connected`);
});
socket.on("updateTeams", updateTeams);

function updateTeams(data) {
  console.log('updateTeams');
  updateTable(data);
}

window.onload = initialize;

function initialize() {
  alias_new_team_button.onclick = createTeamPress;
}

function createTeamPress() {
  let user = alias_username.textContent.split(',')[1].substr(1);
  let data = {};
  data[user] = alias_new_team.value;
  socket.emit('createTeam', data);
}

function join(team) {
  let user = alias_username.textContent.split(',')[1].substr(1);
  let data = {'user':user,'team':team};
  socket.emit('joinTeam', data);
}

function updateTime() {
  round_time.text = `${round_range.value} сек`
}

function updateTable(data) {
  let table = alias_teams;
  deleteRows(table);
  let rows = table.rows;
  let i = 0;
  for (let user of Object.keys(data)) {
    table.insertRow();
    let name = data[user];
    rows[i].className = "table-dark";
    rows[i++].innerHTML = 
    `<td>${user}</td><td>${name}</td><td><button class="btn btn-info" type="button" id="button_${user}"><i class="fa fa-plus d-xl-flex justify-content-xl-center align-items-xl-center" style="font-size: 40px;"></i></button></td>`;
    document.getElementById(`button_${user}`).onclick = () => {join(name)};
  };
  table.tHead.innerHTML = "<th>Имя</th><th>Команда</th><th></th>"
}

function deleteRows(table) {
  let n = table.getElementsByTagName("tr").length;
  while (n != 0) {
    table.deleteRow(0);
    n = table.getElementsByTagName("tr").length;
  }
}