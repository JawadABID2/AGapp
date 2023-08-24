let url = `ws://${window.location.host}/loraDevice_socket/`;
const devSocket= new WebSocket(url);
window.setInterval('refresh()', 60000); // millisecond
let valve_flow_form = document.getElementById("valve_flow_form");

function refresh() {
    // window .location.reload();
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        console.log('******************************function*************************')
        if(this.readyState == 4 && this.status == 200){
            data = JSON.parse(this.response)
            // console.log(data.bv)
            document.getElementById("valve_bat_value").innerText = data.bv.bat + " V"
            document.getElementById("valve_data_timeago").innerText = "(il ya " + data.bv.timeago + ")"
            document.getElementById("capsol_timeago").innerText = "(il ya " + data.tab.timeago + ")"
            document.getElementById("capsol2_timeago").innerText = "(il ya " + data.cap2.timeago + ")"

            document.getElementById("capsol_temp").innerText = data.tab.Temp + " °C"
            document.getElementById("capsol_hum").innerText = data.tab.Hum + " %"
            document.getElementById("capsol_sal").innerText = data.tab.Sal + " mg/L"
            document.getElementById("capsol_ec").innerText = data.tab.Ec + " µS/cm"
            document.getElementById("capsol_bat").innerText = data.tab.Bat + " V"
            // ***************************************************************************************************************
            document.getElementById("capnpk_az").innerText = data.capnpk.Azoute + "mg/kg"
            document.getElementById("capnpk_ph").innerText = data.capnpk.Phosphore + "mg/kg"
            document.getElementById("capnpk_po").innerText = data.capnpk.Potassium + "mg/kg"
            document.getElementById("capnpk_ba").innerText = data.capnpk.Bat + " V"
            document.getElementById("capnpk_timeago").innerText = "(il ya " + data.capnpk.timeago + ")"

            // ********************************************************************************************************************
            
            document.getElementById("capsol2_temp").innerText = data.cap2.Temp + " °C"
            document.getElementById("capsol2_hum").innerText = data.cap2.Hum + " %"
            document.getElementById("capsol2_sal").innerText = data.cap2.Sal + " mg/L"
            document.getElementById("capsol2_ec").innerText = data.cap2.Ec + " µS/cm"
            document.getElementById("capsol2_bat").innerText = data.cap2.Bat + " V"
        }
    }
    xmlHttp.open( "GET", "/home/refresh", false ); // false for synchronous request
    xmlHttp.send();
}

function sendCMD(command, duration, devEui) {
    console.log('connect bis')
    console.log(devEui)
    let s_data = {
        'type' : 'LoRaWAN.downlink',
        'devEui' : devEui,
        'data' : {
            'command' : command,
            'duration' : duration*1000,
            'duration_bytes' : 3
        }
    }
    
    devSocket.send(JSON.stringify(s_data));
    // devSocket.close()
}

function openValve() {
    console.log('click')
    sendCMD(0xB0, 1, "2ee5270e481778fb")
}
function closeValve() {
    console.log('click')
    sendCMD(0xA0, 1, "2ee5270e481778fb")
}

valve_flow_form.addEventListener("submit", (e) => {
    var flow = document.getElementById('valve_flow_value').value;
    let s_data = {
        'DnameBFlow' : 'ValveFlow',
        'Flow' : flow
    }

    devSocket.send(JSON.stringify(s_data));
})

