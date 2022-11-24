var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx,{
    type: 'pie',
    data: {
        labels: ["A型", "O型", "B型", "AB型"],
        datasets:[{
            backgroundColor: [
                "#BB5179",
                "#FAFF67",
                "#58A27C",
                "#3C00FF"
            ],
            data: [38, 31, 21, 10]
        }]
    },
    options: {
        title: {
            display: true,
            text: '血液型 割合'
        }
    }
});