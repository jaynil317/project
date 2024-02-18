

var ctx2 = document.getElementById('doughnut').getContext('2d');
var myChart2 = new Chart(ctx2, {
    type: 'doughnut',
    data: {
        labels: ['Criminal cases', 'Hit and Run cases','cber', 'Civil crimes','others'],

        datasets: [{
            label: 'Employees',
            data: [10, 15, 5,40 ,30],
            backgroundColor: [
                'rgba(41, 155, 99, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 165, 0, 1)',
                'rgba(120, 46, 139,1)',
                'rgba(255, 255, 0,1)'


            ],
            borderColor: [
                'rgba(41, 155, 99, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 165, 0, 1)',
                'rgba(120, 46, 139,1)',
                'rgba(255, 255, 0,1)'




            ],
            borderWidth: 1
        }]

    },
    options: {
        responsive: true
    }
});