console.log('d3_bar.js loaded')

dataFile = "../static/data/bar_chart_csv/cap_color.csv"

var svgWidth = 960;
var svgHeight = 660;

// Define the chart's margins as an object
var chartMargin = {
  top: 50,
  right: 50,
  bottom: 50,
  left: 50
};

// Define dimensions of the chart area
var chartWidth = svgWidth - chartMargin.left - chartMargin.right;
var chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

// Select body, append SVG area to it, and set the dimensions
var svg = d3.select("body")
  .append("svg")
  .attr("height", svgHeight)
  .attr("width", svgWidth);

// Append a group to the SVG area, translate to right and bottom
var chartGroup = svg.append("g")
  .attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`);

// Load data
d3.csv(dataFile).then(function(mushData) {

  console.log(mushData);

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

  // Append two SVG group elements to the chartGroup area,
  // and create the bottom and left axes inside of them
  chartGroup.append("g")
    .call(leftAxis);

  chartGroup.append("g")
    .attr("transform", `translate(0, ${chartHeight})`)
    .call(bottomAxis);

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
    .delay(function(d,i){console.log(i) ; return(i*100)});

  chartGroup.selectAll("text")
    .data(mushData)
    .enter()
    .append("text")
    .text(d => {console.log(d) ; d.count})
    .attr("text-anchor", "middle")
    .attr("x", d => xBandScale(d.value) + xBandScale.bandwidth() / 2)
    .attr("y", d => chartHeight - yLinearScale(d.count) + 15)
    .attr("font-family", "sans-serif")
    .attr("font-size", "11px")
    .attr("fill", "#black");

}).catch(function(error) {
  console.log(error);
});
