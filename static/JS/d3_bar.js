dataClass = "../static/data/bar_chart_csv/class.csv"
dataCapColor = "../static/data/bar_chart_csv/cap_color.csv"
dataCapShape = "../static/data/bar_chart_csv/cap_shape.csv"
dataCapSurface = "../static/data/bar_chart_csv/cap_surface.csv"
dataBruiseBleed = "../static/data/bar_chart_csv/bruise_bleed.csv"
dataGillAttachment = "../static/data/bar_chart_csv/gill_attachment.csv"
dataGillColor = "../static/data/bar_chart_csv/gill_color.csv"
dataGillSpacing = "../static/data/bar_chart_csv/gill_spacing.csv"
dataHabitat = "../static/data/bar_chart_csv/habitat.csv"
dataRing = "../static/data/bar_chart_csv/has_ring.csv"
dataRingType = "../static/data/bar_chart_csv/ring_type.csv"
dataSeason = "../static/data/bar_chart_csv/season.csv"
dataStemColor = "../static/data/bar_chart_csv/stem_color.csv"

var svgWidth = 960;
var svgHeight = 500;

// Define the chart's margins as an object
var margin = {
  top: 50,
  right: 50,
  bottom: 110,
  left: 100
};

// Define dimensions of the chart area
var chartWidth = svgWidth - margin.left - margin.right;
var chartHeight = svgHeight - margin.top - margin.bottom;

updateBar(dataClass);

function updateBar(ClickedData) {

  var area = d3.select("#explore-bar");

  area.html("");

  // Select body, append SVG area to it, and set the dimensions
  var svg = area
    .append("svg")
    .attr("height", svgHeight)
    .attr("width", svgWidth)
    .style("margin", "20px")
    .attr("class", "visual");

  // Append a group to the SVG area, translate to right and bottom
  var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

    // Load data
  d3.csv(ClickedData).then(function(mushData) {

    // Cast the count value to a number for each piece of data
    mushData.forEach(function(d) {
      d.count = +d.count;
    });

    // Configure a band scale for the horizontal axis with a padding of 0.1 (10%)
    var xBandScale = d3.scaleBand()
      .domain(mushData.map(d => d.value))
      .range([0, chartWidth])
      .padding(0.1);

    // Create a linear scale for the vertical axis.
    var yLinearScale = d3.scaleLinear()
      .domain([0, d3.max(mushData, d => d.count)])
      .range([chartHeight, 0]);

    // Create two new functions passing our scales in as arguments
    // These will be used to create the chart's axes
    var bottomAxis = d3.axisBottom(xBandScale);
    var leftAxis = d3.axisLeft(yLinearScale).ticks(10);

    // chartGroup.exit().remove();

    // Append two SVG group elements to the chartGroup area,
    // and create the bottom and left axes inside of them
    chartGroup.append("g")
      .style('font-size', "12px")
      .style("font-family", "Raleway")
      .call(leftAxis);

    chartGroup.append("g")
      .attr("transform", `translate(0, ${chartHeight})`)
      .style("font-size", "14px")
      .style("font-family", "Raleway")
      .call(bottomAxis)
        .selectAll("text")  
        .style("text-anchor", "end")
        .attr("dx", "-.8em")
        .attr("dy", ".15em")
        .attr("transform", "rotate(-65)");

    // Create one SVG rectangle per piece of mushData
    // Use the linear and band scales to position each rectangle within the chart
    chartGroup.selectAll(".bar")
      .data(mushData)
      .enter()
      .append("rect")
      .style("fill", d => d.color)
        .attr("x", d => xBandScale(d.value))
        .attr("y", chartHeight)
        .attr("width", xBandScale.bandwidth())
        .attr("height", d => chartHeight - yLinearScale(0))

    chartGroup.selectAll("rect")
      .transition()
      .duration(700)
      .ease(d3.easeCubicInOut)
      .attr("y", d => yLinearScale(d.count))
      .attr("height", d => chartHeight - yLinearScale(d.count))
      .delay(function(d,i){return(i*100)});

    chartGroup.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left + 15)
      .attr("x", 0 - (chartHeight / 2))
      .attr("dy", "1em")
      .attr("class", "axis-labels")
      .text("Percentage of Total Data");

    chartGroup.append("text")
      .attr("transform", `translate(${(chartWidth / 2)}, ${chartHeight + margin.top + 30})`)
      .attr("class", "axis-labels")
      .text("Category");

    
    chartGroup.selectAll(".bar")
      .data(mushData)
      .enter()
      .append("text")
      .text(d => {console.log(d) ; return d.count + "%"})
      .attr("text-anchor", "middle")
      .attr("x", d => xBandScale(d.value) + xBandScale.bandwidth() / 2)
      .attr("y", d => yLinearScale(d.count) - 3)
      .attr("font-family", "sans-serif")
      .attr("font-size", "14px")
      .attr("fill", "white");
    
    chartGroup.selectAll("text")
      .transition()
      .duration(700)
      .ease(d3.easeCubicInOut)
      .attr("fill", "black")
      .delay(function(d,i){return(i*50)});

  }).catch(function(error) {
    console.log(error);
  });
}