// new Chart(document.getElementById("myChart"), {
//     type: 'line',
//     data: {
//         labels: ["Test1", "Test2", "Test3", "Test4", "Test5"],

//         datasets: [{
//             data: [240, 180, 300, 267, 155],
//             label: "Physics",
//             borderColor: "#3e95cd",
//             hoverBorderWidth: 2,
//             hoverBorderColor: "#fff",
//             fontSize: 25,

//             fill: false
//         }, {
//             data: [140, 280, 200, 167, 255],
//             label: "Mathematics",
//             borderColor: "#8e5ea2",
//             hoverBorderWidth: 2,
//             hoverBorderColor: "#fff",
//             fontSize: 25,
//             fill: false
//         }, {
//             data: [195, 227, 360, 198, 148],
//             label: "Chemistry",
//             borderColor: "#3cba9f",
//             hoverBorderWidth: 2,
//             hoverBorderColor: "#fff",
//             fontSize: 25,
//             fill: false
//         },
//         ]
//     },

//     options: {
//         responsive: true,
//         maintainAspectRatio: false,
//         title: {
//             display: true,
//             text: 'PERFORMANCE TRENDS REPORT',
//             fontSize: 25,
//             fontColor: "#1c1c1c"
//         }
//     }
// });
// Area Chart Example
var ctx = document.getElementById("myChart");
var myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        datasets: [{
            label: "Earnings",
            lineTension: 0.3,
            backgroundColor: "rgba(78, 115, 223, 0.05)",
            borderColor: "rgba(78, 115, 223, 1)",
            pointRadius: 3,
            pointBackgroundColor: "rgba(78, 115, 223, 1)",
            pointBorderColor: "rgba(78, 115, 223, 1)",
            pointHoverRadius: 3,
            pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
            pointHoverBorderColor: "rgba(78, 115, 223, 1)",
            pointHitRadius: 10,
            pointBorderWidth: 2,
            data: [0, 10000, 5000, 15000, 10000, 20000, 15000, 25000, 20000, 30000, 25000, 40000],
        }],
    },
    options: {
        maintainAspectRatio: false,
        layout: {
            padding: {
                left: 10,
                right: 25,
                top: 25,
                bottom: 0
            }
        },
        scales: {
            xAxes: [{
                time: {
                    unit: 'date'
                },
                gridLines: {
                    display: false,
                    drawBorder: false
                },
                ticks: {
                    maxTicksLimit: 7
                }
            }],
            yAxes: [{
                ticks: {
                    maxTicksLimit: 5,
                    padding: 10,
                    // Include a dollar sign in the ticks
                    callback: function (value, index, values) {
                        return '$' + number_format(value);
                    }
                },
                gridLines: {
                    color: "rgb(234, 236, 244)",
                    zeroLineColor: "rgb(234, 236, 244)",
                    drawBorder: false,
                    borderDash: [2],
                    zeroLineBorderDash: [2]
                }
            }],
        },
        legend: {
            display: false
        },
        tooltips: {
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            titleMarginBottom: 10,
            titleFontColor: '#6e707e',
            titleFontSize: 14,
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: false,
            intersect: false,
            mode: 'index',
            caretPadding: 10,
            callbacks: {
                label: function (tooltipItem, chart) {
                    var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
                    return datasetLabel + ': $' + number_format(tooltipItem.yLabel);
                }
            }
        }
    }
});