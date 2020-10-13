
const cart_bar = document.getElementById('chart-algorithm').getContext('2d');
let gradient_color = cart_bar.createLinearGradient(0, 0, 0, 500);

gradient_color.addColorStop(0, "rgba(178, 10, 44,1)");
gradient_color.addColorStop(1, " rgba(255, 251, 213,0.4)");
let algorithm_chart = new Chart(cart_bar, {
    type: 'horizontalBar',
    maxBarThickness: 1,
    data: {
        labels: ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash', 'C#', 'PHP'],
        datasets: [{
            data: [67.7, 63, 54, 44, 40, 33, 31, 26],
            backgroundColor: [
                'rgba(46, 157, 231,1)',
                'rgba(46, 157, 231,1)',
                'rgba(46, 157, 231,1)',
                'rgba(46, 157, 231,1)',
                'rgba(46, 157, 231,1)',
                'rgba(46, 157, 231,1)',
                'rgba(46, 157, 231,1)',
                'rgba(46, 157, 231,1)'

            ]

        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    fontColor: 'white'
                },
                barPercentage: 0.4,
            }],
            xAxes: [{
                ticks: {
                    fontColor: "white   ",
                    beginAtZero: true
                }
            }]
        },
        title: {

            display: true,
            text: 'Most Popular Technologies 2020',
            fontSize: 18,
            lineHeight: 1.2,
            fontColor: 'white',
            fontFamily: 'Poppins'

        },
        animation: {
            duration: 1000,
            easeing: 'easeInBack'
        },
        legend: {
            display: false,
            labels: {
                color: 'white'
            }
        }
    }
});