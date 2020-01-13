import io from "socket.io-client";
const socket = io("http://localhost:5000");

socket.on("connect", _ => {
  console.log(`Client ${socket.id} connected`);
});
socket.on("event", event);
socket.on("updateTeams", updateTeams);

function updateTeams(data) {
  console.log('updateTeams');
  updateTable(data);
}

function event(data) {
  console.log('event');
  // updateTable(data);
}

window.onload = initialize;

function initialize() {
  alias_new_team_button.onclick = createTeamPress;
}

function createTeamPress() {
  let user = alias_username.textContent.split(',')[1].split('.')[0].substr(1);
  let data = {};
  data[user] = alias_new_team.value;
  socket.emit('createTeam', data);
}

// function refresh() {
//   socket.emit("update", {
//     'username': 'test',
//     'action': 'login',
//     'login_time': '12312312eda'
//   });
// }

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
    `<td>${user}</td><td>${name}</td>`;
  };
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