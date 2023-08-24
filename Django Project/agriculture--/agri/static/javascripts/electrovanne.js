let url = `ws://${window.location.host}/loraDevice_socket/`;
const devSocket = new WebSocket(url);

let cmd_form = document.getElementById("valveCmdForm");
const data = document.currentScript.dataset;

cmd_form.addEventListener("submit", (e) => {
    e.preventDefault();
    let cmdCode = {
        'OpenValve' : 0xA0,
        'CloseValve' : 0xB0
    }
    let cmdKey = ''
    let cmds = document.getElementsByName("cmd");
    cmds.forEach(cmd => {
        if(cmd.checked){
            cmdKey = cmd.value;
        }
    });

    var duration = document.getElementById("cmd_dur").value;
    var command = cmdCode[cmdKey];
    if(duration <= 0 ){
        duration = 1;
        command = (0xA0 + 0xB0) - command
    }
    
    let s_data = {
        'type' : 'LoRaWAN.downlink',
        'devEui' : data.actuatorId,
        'data' : {
            'command' : command,
            'duration' : duration,
            'duration_bytes' : 3
        }
    }
    devSocket.send(JSON.stringify(s_data))
});

function endlessCheck(target) {
    if(target.checked){
        document.getElementById('cmd_dur').disabled = true;
        document.getElementById('cmd_dur').value = -100;
    }else{
        document.getElementById('cmd_dur').disabled = false;
        document.getElementById('cmd_dur').value = 1200;
    }
}