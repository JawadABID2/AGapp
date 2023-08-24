const ctx = document.getElementById('myChart');
const ctxt = document.currentScript.dataset;
data = JSON.parse(ctxt.context)
console.log(data)

new Chart(ctx, {
type: 'line',
data: {
    labels : data.labels,
        
    datasets: [{
    label: 'Temperature : ',
    data: data.temperature,
    borderWidth: 2 ,
    borderColor : 'red',
    pointRadius : 1,
    tension : 0.8
    }]
},
options: {
    scales: {
    x : {
        display : false
    },
    y: {
        beginAtZero: true,
        // suggestedMax: 80
    }
    }
}
});
const ctx1 = document.getElementById("myChart1");
new Chart(ctx1, {
type : 'line',
data : {
    labels : data.labels,
    datasets : [{
    label : 'humidity : ',
    data : data.humidity, 
    borderWidth : 1,
    pointRadius : 1,
    tension : 0.8
    }],
},
options : {
    scales : {
    x : {
        display : false
    },
    y : {
        beginAtZero : true
    }
    }
}

});
const ctx2 = document.getElementById("myChart2");
new Chart(ctx2, {
type : 'line',
data : {
    labels : data.labels,
    datasets : [{
    label : 'battery : ',
    data : data.battery,
    borderWidth : 1,
    pointRadius : 1,
    tension : 0.8
    }]
},
options : {
    scales :{
    x : {
        display : false
    },
    y : {
        beginAtZero : true
    }
    }
}
});
const ctx3 = document.getElementById("myChart3");
new Chart(ctx3, {
type : 'line',
data : {
    labels : data.labels,
    datasets : [{
    label : 'CO2 : ',
    data : data.CO2,
    borderWidth : 1,
    pointRadius : 1,
    tension : 0.8
    }]
},
options : {
    scales : {
    x : {
        display : false
    },
    y : {
        beginAtZero : true
    }
    }
}

})
function openModal1() {
    var modal1 = document.getElementById("setting_deepSleep_duration");
    modal1.style.display = "block";
    
}
window.onclick = function(e){
    var modal1 = document.getElementById("setting_deepSleep_duration");
    if(e.target == modal1){
        modal1.style.display = "none";
    }
    }