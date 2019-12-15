import io from "socket.io-client";

const socket = io("http://localhost");
socket.on("connect", connect);
socket.on("event", event);
socket.on("disconnect", disconnect);

function connect() {}

function event(data) {}

function disconnect() {}

window.onload = initialize;

function initialize() {
  var button = document.getElementById("alias-btn");
  document.onload = updateTable();
}

function updateTable() {
  let table = document.getElementById("client-table");
  deleteRows(table);
}

function deleteRows(table) {
  let n = table.getElementsByTagName("tr").length;
  while (n != 0) {
    table.deleteRow(0);
    n = table.getElementsByTagName("tr").length;
  }
}

function getUsers() {}
