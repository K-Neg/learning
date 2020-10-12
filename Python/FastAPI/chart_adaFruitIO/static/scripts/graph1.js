var dados = [{ x: 0, y: 0 }, { x: 0, y: 0 }]

setInterval(update(), 3000);

function update() {


    d3.json("https://io.adafruit.com/api/v2/Kneg/feeds/temp1020/data", function (data) {
        //console.log(temps);



        for (var i = 0, j = data.length; i < j; i++) {


            dados.push({
                x: data[i].value,
                //x: i * 2,
                y: i
            });
        }

        /*
        var margin = { top: 10, right: 30, bottom: 30, left: 60 },
            width = 460 - margin.left - margin.right,
            height = 400 - margin.top - margin.bottom;
        // append the svg object to the body of the page
        var svg = d3.select("#dataviz")
            .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform",
                "translate(" + margin.left + "," + margin.top + ")");
        //Read the data
        
        
        
        d3.csv("https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/connectedscatter.csv",
            // When reading the csv, I must format variables:
            function (d) {
                return { date: d3.timeParse("%Y-%m-%d")(d.date), value: d.value }
        
        
            },
            // Now I can use this dataset:
            function (data) {
        
                // Add X axis --> it is a date format
                var x = d3.scaleTime()
                    .domain(d3.extent(data, function (d) { return d.date; }))
                    .range([0, width]);
                svg.append("g")
                    .attr("transform", "translate(0," + height + ")")
                    .call(d3.axisBottom(x));
                // Add Y axis
                var y = d3.scaleLinear()
                    .domain([8000, 9200])
                    .range([height, 0]);
                svg.append("g")
                    .call(d3.axisLeft(y));
                // Add the line
                svg.append("path")
                    .datum(data)
                    .attr("fill", "none")
                    .attr("stroke", "#69b3a2")
                    .attr("stroke-width", 1.5)
                    .attr("d", d3.line()
                        .x(function (d) { return x(d.date) })
                        .y(function (d) { return y(d.value) })
                    )
                // Add the points
                svg
                    .append("g")
                    .selectAll("dot")
                    .data(data)
                    .enter()
                    .append("circle")
                    .attr("cx", function (d) { return x(d.date) })
                    .attr("cy", function (d) { return y(d.value) })
                    .attr("r", 5)
                    .attr("fill", "#69b3a2")
            })
        */




        // set the dimensions and margins of the graph
        var margin = { top: 20, right: 20, bottom: 20, left: 20 },
            width = 300 - margin.left - margin.right,
            height = 300 - margin.top - margin.bottom;

        // append the svg object to the body of the page
        var svG = d3.select("#dataviz")
            .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform",
                "translate(" + margin.left + "," + margin.top + ")");

        // Create data
        //var data = [{ x: 10, y: 20 }, { x: 40, y: 90 }, { x: 80, y: 50 }]

        // X scale and Axis
        var x = d3.scaleLinear()
            .domain([0, 100])         // This is the min and the max of the data: 0 to 100 if percentages
            .range([0, width]);       // This is the corresponding value I want in Pixel
        svG
            .append('g')
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x));

        // X scale and Axis
        var y = d3.scaleLinear()
            .domain([0, 60])         // This is the min and the max of the data: 0 to 100 if percentages
            .range([height, 0]);       // This is the corresponding value I want in Pixel
        svG
            .append('g')
            .call(d3.axisLeft(y));

        // Add 3 dots for 0, 50 and 100%
        svG
            .selectAll("whatever")
            .data(dados)
            .enter()
            .append("circle")
            .attr("cx", function (d) { return x(d.x) })
            .attr("cy", function (d) { return y(d.y) })
            .attr("r", 7)
    });
}