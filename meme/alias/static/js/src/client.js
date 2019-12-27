import io from "./socket.io.js";
const socket = io("http://localhost:3000");
socket.on("connect", connect);
socket.on("event", event);

function connect() {
  console.log('Hello');
}

function event(data) {
  console.log('event');
  updateTable(data);
}

window.onload = initialize;

function initialize() {
  var button = document.getElementById("alias-refresh");
  button.onclick = refresh;
}

function refresh() {
  socket.emit("update", {
    'username': 'test',
    'action': 'login',
    'login_time': '12312312eda'
  });
}

function updateTable(data) {
  let table = document.getElementById("client-table");
  deleteRows(table);
  let rows = table.rows;
  console.log(rows);
  for (let i = 0; i < data.length; i++) {
    table.insertRow();
    rows[i].className = "table-dark";
    rows[i].innerHTML = 
    `<td>${i}</td><td>${data[i].username}</td>`;
    console.log(table);
  }
}

function deleteRows(table) {
  let n = table.getElementsByTagName("tr").length;
  while (n != 0) {
    table.deleteRow(0);
    n = table.getElementsByTagName("tr").length;
  }
}
