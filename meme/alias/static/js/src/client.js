
import io from "./socket.io.js";
// const io = require("socket.io-client");
const socket = io("http://localhost:3000");
socket.on("connect", connect);
socket.on("event", event);
socket.on("disconnect", disconnect);

function connect(
  
) {console.log('Hello');}

function event(data) {
  console.log('event');
  updateTable(data);
}

function disconnect() {}

// window.onload = initialize;

// function initialize() {
//   var button = document.getElementById("alias-btn");
//   document.onload = updateTable();
// }

function updateTable(data) {
  let table = document.getElementById("client-table");
  deleteRows(table);
  rows = table.rows();
  console.log(rows);
  for(let i=0;i<data.length;i++)
  {
    table.insertRow();
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
