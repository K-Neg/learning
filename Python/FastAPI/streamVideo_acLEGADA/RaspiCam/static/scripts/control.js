var local_ip = document.getElementById('script_1').getAttribute("data")
ws = new WebSocket("ws://" + local_ip + "/ws");
event.preventDefault()



function order(order) {
    var bin = order
    ws.send(bin)
    event.preventDefault();
}

function record(video_parameters) {
    ws.send("gravar_video_passar_parametros")
    event.preventDefault();
}

