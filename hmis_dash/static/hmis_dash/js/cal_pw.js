let width1 = 200,
height1 = 50;

//   let prjType = 'Urban';
let height1 = [];
let mmRsd1 = [];
height1.push('All States');
let selectedYear1 = "{{fy}}";

const svg1 = d3.select('#chart').append('svg1').attr('id', 'svg11').attr('width', 3500)
.attr('height', 3000).call(responsivefy_new);

// const legendbox = d3.select('#legendList').append('svg1').attr('id', 'svg12').attr('width1', 350)
//   .attr('height1', 950).call(responsivefy);

let ticks1;
let selectedCategory1 = 'PW given 360 Calcium tablets';

function responsivefy_new(svg1) {

// Container is the DOM element, svg1 is appended. 
// Then we measure the container and find its 
// aspect1 ratio.

const container = d3.select(svg1.node().parentNode),
  width1 = parseInt(svg1.style('width1'), 10),
  height1 = parseInt(svg1.style('height1'), 10),
  aspect1 = width1 / height1;

// Add viewBox attribute to set the value to initial size 
// add preserveaspect1Ratio attribute to specify how to scale  
// and call resize_new so that svg1 resize_news on page load 
svg1.attr('viewBox', `0 0 ${width1} ${height1}`).
  attr('preserveaspect1Ratio', 'xMinYMin').
  call(resize_new_);

d3.select(window).on('resize.', resize_new);

function resize_new() {
  const targetwidth1 = $(window).width1();
  const targetheight1 = $(window).height1();
  //var targetheight1 = $(window).height1();
  d3.select('#svg11').attr('width1', targetwidth1);
  d3.select('#svg11').attr('height1', targetheight1);
  // d3.select('#svg12').attr('width1', targetwidth1);
  // d3.select('#svg12').attr('height1', targetheight1);
}
}

//   function filterCSV1(csv, key, value) {
//     var result1 = [];
//     for (var i = 0; i < value.length; i++) {
//       csv.forEach(function (val, idx, arr) {

//         if (val[key] == value[i]) {

//           result1.push(val)
//         }
//       })
//     }
//     return result1;
//   }

function filterCSV1(csv, key, value) {
    var result1 = [];
    csv.forEach(function (val, idx, arr) {

        if (val[key] == value) {

            result1.push(val)
        }
    })
    return result1;
}

//   var mouseG

var margin1 = { top: 10, right: 20, bottom: 30, left: 150 },
innerwidth1 = 1000 - margin1.left - margin1.right,
innerheight1 = 550 - margin1.top - margin1.bottom;

// Set the ranges
var xScale1 = d3.scale.ordinal().rangePoints([0, innerwidth1], 0.5);
var yScale1 = d3.scale.linear().range([innerheight1, 0]);

// Define the axes
var xAxis1 = d3.svg1.axis().scale(xScale1)
.orient("bottom")

var yAxis1 = d3.svg1.axis().scale(yScale1)
.orient("left");

// Define the line
var stateline1 = d3.svg1.line()
.interpolate("linear")
.x(function (d) { return xScale1(d.month); })
.y(function (d) { return yScale1(d.value); });

var g1 = svg1.append('g')
.attr('transform', `translate(${margin1.left}, ${margin1.top})`);

//make a rectangle so there is something to click on
g1.append("rect")
.attr(width1, innerwidth1)
.attr("height", innerheight1)
.attr("class", "plot");

//make a clip1 path for the graph  
var clip1 = g1.append("clip1Path")
.attr("id", "clip1")
.append("svg1:rect")
.attr("x", 0)
.attr("y", 0)
.attr("width", innerwidth1)
.attr("height", innerheight1);


var color1 = d3.scale.category10();

const render = data => {
console.log('mean, lower, upper', mmRsd1)
var width1;

// Scale the range of the data

ticks1 = data.map(function (d) {
  return d.month
});
xScale1.domain(ticks1);

yScale1.domain([d3.min(data, function (d) { return d.value; }), d3.max(data, function (d) { return d.value; }) * 1.7]);

// Nest the entries by block1

dataNest1 = d3.nest()
  .key(function (d) { return d.state })
  .entries(data);

var result1 = dataNest1.filter(function (val, idx, arr) {
  return $("." + val.key).attr("fill") != "#ccc"
  // matching the data with selector status
})


var block1 = g1.selectAll(".line")
  .data(result1, function (d) { return d.key });

block1.enter().append("path")
  .attr("class", "line");

block1.transition()
  // .style("stroke", function (d, i) { return d.color1 = color1(d.key); })
  .style("stroke", "#a55fa5")
  .attr("id", function (d) { return 'tag' + d.key.replace(/\s+/g, ''); }) // assign ID
  .attr("d", function (d) {
    return stateline1(d.values);
  });


block1.exit().remove();

// let legend = d3.select("#svg12")
//   .selectAll("text")
//   .data(dataNest1, function (d) { return d.key });


// //checkboxes
// legend.enter().append("rect")
//   .attr(width1, 20)
//   .attr("height", 20)
//   .attr("x", 0)
//   .attr("y", function (d, i) { return 0 + i * 30; })  // spacing
//   .attr("fill", "#a55fa5")
//   // .attr("fill", function (d) {
//   //   return color1(d.key);

//   // })
//   .attr("class", function (d, i) { return "legendcheckbox " + d.key })

// // Add the Legend text
// legend.enter().append("text")
//   .attr("x", 25)
//   .attr("y", function (d, i) { return 18 + i * 30; })
//   .attr("class", "legend");

// legend.transition()
//   .style("fill", "#777")
//   .text(function (d) { return d.key; });

// legend.exit().remove();

svg1.selectAll(".axis").remove();
svg1.selectAll(".mean-line").remove();
svg1.selectAll(".line-text").remove();


// Add the X Axis
g1.append("g")
  .attr("class", "x axis")
  .attr("transform", "translate(0," + innerheight1 + ")")
  .call(xAxis1)
  .attr("font-size", "20px")
  .attr("font-weight", "bold")
  .selectAll("text")
  .attr("y", 0)
  .attr("x", 9)
  .attr("dy", ".35em")
  .attr("transform", "rotate(45)")
  .style("text-anchor", "start");

// Add the Y Axis
g1.append("g")
  .attr("class", "y axis")
  .call(yAxis1)
  .attr("font-size", "20px")
  .attr("font-weight", "bold")
  .append("text")
  .attr("transform", "rotate(-90)")
  .attr("y", 6)
  .attr("dy", ".71em");


  g1.append("line")
.attr("class", "mean-line")
.attr("x1", 0 )
.attr("x2",innerwidth1)
.attr("y1", yScale1(mmRsd1[0]))   // whatever the y-val should be
.attr("y2", yScale1(mmRsd1[0]))
.attr("stroke-width1", 3)
.attr("stroke", "red");

g1.append("text")
.attr("class", "line-text")
.attr("transform", "translate("+(innerwidth1+3)+","+yScale1(mmRsd1[0])+")")
.attr("dy", ".35em")
.attr("text-anchor", "start")
.style("fill", "red")
.text("AVERAGE");


g1.append("line")
.attr("class", "mean-line")
.attr("x1", 0 )
.attr("x2",innerwidth1)
.attr("y1", yScale1(mmRsd1[1]))   // whatever the LOWER should be
.attr("y2", yScale1(mmRsd1[1]))
.attr("stroke-width1", 3)
.attr("stroke", "grey");


g1.append("text")
.attr("class", "line-text")
  .attr("transform", "translate("+(innerwidth1+3)+","+yScale1(mmRsd1[1])+")")
  .attr("dy", ".35em")
  .attr("text-anchor", "start")
  .style("fill", "#696969")
  .text("LOWER");

g1.append("line")
.attr("class", "mean-line")
.attr("x1", 0 )
.attr("x2",innerwidth1)
.attr("y1", yScale1(mmRsd1[2]))   // whatever the y-val should be
.attr("y2", yScale1(mmRsd1[2]))
.attr("stroke-width1", 3)
.attr("stroke", "grey");

g1.append("text")
.attr("class", "line-text")
  .attr("transform", "translate("+(innerwidth1+3)+","+yScale1(mmRsd1[2])+")")
  .attr("dy", ".35em")
  .attr("text-anchor", "start")
  .style("fill", "#696969")
  .text("UPPER");

  g1.append("line")
.attr("class", "mean-line")
.attr("x1", 0 )
.attr("x2",innerwidth1)
.attr("y1", yScale1(mmRsd1[3]))   // whatever the y-val should be
.attr("y2", yScale1(mmRsd1[3]))
.attr("stroke-width1", 3)
.attr("stroke", "green");

g1.append("text")
.attr("class", "line-text")
  .attr("transform", "translate("+(innerwidth1+3)+","+yScale1(mmRsd1[3])+")")
  .attr("dy", ".35em")
  .attr("text-anchor", "start")
  .style("fill", "green")
  .text("ANNUAL TARGET");

};

function clearAll() {
d3.selectAll(".line")
  .transition().duration(100)
  .attr("d", function (d) {
    return null;
  });
// d3.select("#legend").selectAll("rect")
//   .transition().duration(100)
//   .attr("fill", "#ccc");
};

function showAll() {
d3.selectAll(".line")
  .transition().duration(100)
  .attr("d", function (d) {
    return stateline1(d.values);
  });
// d3.select("#legend").selectAll("rect")
//   .attr("fill", function (d) {
//     if (d.active == true) {
//       return color1(d.key);
//     }
//   })
};

// Get the data
data_from_django = {{ data | safe }};
console.log(data_from_django)
var data = []
data_from_django.forEach(element => {
data.push(element.fields);
});

data.forEach(function (d) {

d.tot_no_pw_reg_anc = +d.tot_no_pw_reg_anc;
d.no_early_anc_register = +d.no_early_anc_register;
d.no_anc_4_or_more = +d.no_anc_4_or_more;
d.no_pw_given_tt1 = +d.no_pw_given_tt1;
d.no_pw_given_tt2 = +d.no_pw_given_tt2;
d.no_pw_given_tt_booster = +d.no_pw_given_tt_booster;
d.no_pw_given_calcium = +d.no_pw_given_calcium;
d.no_pw_given_ifa = +d.no_pw_given_ifa;
d.no_pw_given_albendazole = +d.no_pw_given_albendazole;
d.tot_c_section_deliveries = +d.tot_c_section_deliveries;
d.tot_still_birth = +d.tot_still_birth;
d.state = d.state;
d.month = d.month;
d.year = d.year;
});


console.log("data", data)
let section = 'no_pw_given_calcium'

// $(".category a").click(function () {

//   var val = $(this).text();
//   selectedCategory1 = val;
//   setSection(val);
//   st_data = filterCSV1(data, 'state', height1);
//   d3.selectAll(".mouse-per-line circle").remove();
//    mmRsd1 = [];

//   mmRsd1 = calc_mean(st_data, section); 

//   setData(st_data, section, mmRsd1);

// });

// let choices = parseURLParameters(window.location.href);
// if (choices.length > 0) {
// mmRsd1 = [];

//   let selectedCat = choices[0].replace(/_/g, ' ');
//   selectedCategory1 = selectedCat;
//   $('.category a').parents('.dropdown').find('.dropdown-toggle').html(selectedCat + ' <span class="selectedCategory1"></span>');
//   st_data = filterCSV1(data, 'state', height1);
//   setSection(selectedCat);
//    mmRsd1 = [];

//   mmRsd1 = calc_mean(st_data, section); 
//   setData(st_data, section, mmRsd1);
// }
// else {
st_data = filterCSV1(data, 'state', height1);
 mmRsd1 = [];

mmRsd1 = calc_mean(st_data, section); 
setData(st_data, section, mmRsd1);
// }

// function setSection(val) {
//   if (val == 'Total no of PW registered for ANC')
//     section = 'tot_no_pw_reg_anc';
//   else if (val == 'Early ANC Registeration')
//     section = 'no_early_anc_register';
//   else if (val == 'PW received 4 or more ANC check ups')
//     section = 'no_anc_4_or_more';
//   else if (val == 'PW given TT1')
//     section = 'no_pw_given_tt1';
//   else if (val == 'PW given TT2')
//     section = 'no_pw_given_tt2';
//   else if (val == 'PW given TT Booster')
//     section = 'no_pw_given_tt_booster';
//   else if (val == 'PW given 360 Calcium tablets')
//     section = 'no_pw_given_calcium';
//   else if (val == 'PW given 180 Iron Folic Acid (IFA) tablets')
//     section = 'no_pw_given_ifa';
//   else if (val == 'PW given one Albendazole tablet after 1st trimester')
//     section = 'no_pw_given_albendazole';
//   else if (val == 'C-section deliveries')
//     section = 'tot_c_section_deliveries';
//   else
//     section = 'tot_still_birth'
// }


$("#state").change(function () {
height1 = [];
height1 = $('#state').val();
st_data = filterCSV1(data, 'state', height1);
// legendbox.selectAll("*").remove();
 mmRsd1 = [];

mmRsd1 = calc_mean(st_data, section); 
setData(st_data, section, mmRsd1);
});

//Initial Graph
// st_data = filterCSV1(data, 'state', height1);
//  mmRsd1 = [];

// mmRsd1 = calc_mean(st_data, section); 

// setData(st_data, section, mmRsd1);

function setData(data, section, mmRsd1) {
var dataFilter = data.map(function (d) { return { year: d.year, month: d.month, state: d.state, value: d[section] } })

//debugger

dataFilter.forEach(function (d) {
  d.value = +d.value;
});

//debugger
render(dataFilter, mmRsd1);

jQuery('h1.page-header').html(section);
}



function parseURLParameters() {
var query = (window.location.search || '?').substr(1);
var map = [];
query.replace(/([^&=]+)=?([^&]*)(?:&+|$)/g, function (match, key, value) {
  map.push(value);
});
return map;
}

function calc_mean(data, section) {
console.log(data, "data")
var dataF = data.map(function(d){return {value: d[section] }})
let pw_data = [];

data.map(d =>{
  pw_data.push(+d.no_pw_given_calcium)
})
// console.log("pw_data", pw_data)

//Calculating Annual Target
let pw_sum = 0, annual_target;
for (let i = 0; i < pw_data.length; i++) {
    pw_sum += pw_data[i];
  }
  
  annual_target = (pw_sum / 12);

let mmRsd1Calc =[];  


let X = [];

    dataF.map(d =>{
  X.push(+d.value)
})
  let tot_count = dataF.length;  
  //Finding Process Mean
  let pm_sum = 0, process_mean;
  
  for (let i = 0; i < X.length; i++) {
    pm_sum += X[i];
  }
  
  process_mean = (pm_sum / tot_count);

  //Finding mean moving range 
  let mR, mR_sum = 0, mean_mR, mR_array = [];
  
for (let i = 1; i < X.length; i++) {
  mR = (Math.abs(X[i] - X[i-1]));
  mR_array.push(+mR);
}
  
for(let i = 1; i < mR_array.length; i++)
{
  mR_sum += mR_array[i];
}
  mean_mR = (mR_sum / mR_array.length);
  
  let seq_dev = (mean_mR / 1.128);
  
  let upper_cl, lower_cl;
  lower_cl = Math.abs(process_mean - 3 * seq_dev);
  upper_cl = Math.abs(process_mean + 3 * seq_dev);


  mmRsd1Calc.push(process_mean, lower_cl, upper_cl, annual_target);

return mmRsd1Calc;
}
$(function () {
//bind event
$('#state').val('All States');

// $(".category a").click(function () {
//   var valCategory = $(this).text();
//   $(this).parents('.dropdown').find('.dropdown-toggle').html(valCategory + ' <span class="selectedCategory1"></span>');
// });

//trigger event
// if (choices.length <= 0)
//   $(".category a").first().trigger('click');

});