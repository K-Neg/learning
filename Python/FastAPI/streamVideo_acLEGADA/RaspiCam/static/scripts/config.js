var local_ip = document.getElementById('script_1').getAttribute("data")
ws = new WebSocket("ws://" + local_ip + "/ws");
event.preventDefault()
     
     
function sendMessage(event) {
    var campo = document.getElementById("messageText")
    ws.send(campo.value)
    campo.value = ''
    event.preventDefault()
}