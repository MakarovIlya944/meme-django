const {EchoRequest, EchoResponse} = require('./echo_pb.js');
const {EchoServiceClient} = require('./echo_grpc_web_pb.js');

var echoService = new EchoServiceClient('http://localhost:8080');

var request = new EchoRequest();
request.setMessage('Hello World!');

echoService.echo(request, {}, function(err, response) {
  // ...
});

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

function getUsers() {

}