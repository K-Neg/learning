ws = new WebSocket("ws://localhost:8000/ws")
//event.preventDefault();


Highcharts.chart("container", {
    title: {
        text: "Scatter Test",
        type: 'scatter',
        zoomType: 'xy'
    },

    subtitle: {
        text: "Subtitulo"
    },

    yAxis: {
        title: {
            text: "Y coord"
        }
    },
    xAxis: {
        title: {
            text: "X coord"
        }
    },
    legend: {
        layout: "vertical",
        align: "right",
        verticalAlign: "middle"
    },

    plotOptions: {
        scatter: {
            marker: {
                radius: 20,
                states: {
                    hover: {
                        enabled: true,
                    }
                }
            },
            states: {
                hover: {
                    marker: {
                        enabled: false
                    }
                }
            },
            tooltip: {
                headerFormat: "<b>{series.name}</b><br>",
                pointFormat: "{point.x} cm, {point.y} kg"
            }
        }
    },

    series: [
        {
            name: "Installation",
            color: "rgba(223, 83, 83, .5)",
            data: [
                [1, 1],
                [1, 2],
            ]
        }
    ]
});


ws.onmessage = function (event) {
    var content = event.data
    console.log('here')
    ws.send('add')
    data.push(content)

}
