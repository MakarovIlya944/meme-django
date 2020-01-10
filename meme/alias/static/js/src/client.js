import io from "socket.io-client";
const socket = io("http://localhost:5000");
socket.on("connect", _ => {
  console.log('Hello');
  socket.on("event", event);
  socket.on("updateTeams", updateTeams);
});

function updateTeams(data) {
  console.log('updateTeams');
  updateTable(data);
}

function event(data) {
  console.log('event');
  updateTable(data);
}

window.onload = initialize;

function initialize() {
  socket.emit("connect")
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

  for (let key of Object.keys(data)) {
    table.insertRow();
    rows[i].className = "table-dark";
    rows[i].innerHTML = 
    `<td>${key}</td><td>${data[key]}</td>`;
  }  

  // for (let i = 0; i < data.length; i++) {
  //   table.insertRow();
  //   rows[i].className = "table-dark";
  //   rows[i].innerHTML = 
  //   `<td>${i}</td><td>${data[i].username}</td>`;
  //   console.log(table);
  // }
}

function deleteRows(table) {
  let n = table.getElementsByTagName("tr").length;
  while (n != 0) {
    table.deleteRow(0);
    n = table.getElementsByTagName("tr").length;
  }
}

$(function(){

    // Initializing the swiper plugin for the slider.
    // Read more here: http://idangero.us/swiper/api/
    
    var mySwiper = new Swiper ('.swiper-container', {
        loop: true,
        pagination: '.swiper-pagination',
        paginationClickable: true,
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev'
    });
    
});