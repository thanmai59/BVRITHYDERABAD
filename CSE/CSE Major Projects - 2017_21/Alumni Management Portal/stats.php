<?php
include 'header.php';
$table_name = "alumni";
$chart_title = "Companies";
if($_POST["yog"]){
    $yog = $_POST["yog"];
	$rows = get_results("SELECT DISTINCT company FROM $table_name WHERE yog=$yog",ARRAY_A);
} else {
	$rows = get_results("SELECT DISTINCT company FROM $table_name",ARRAY_A);
}

foreach ($rows as $row) {
    $company_name = $row["company"];
    $company .= "'".$company_name."',";
    $count = get_var("SELECT COUNT(company) FROM $table_name WHERE company='$company_name'");
    $salary .= "'".$count."',";
}
?>
<div style="background-color: white; padding: 10px;">
<form method="post">Year of Graduation: 
    <input type="text" name="yog" value="<?php echo $yog; ?>">
    <input type="submit">
    <a href=""><button type="button">Clear</button></a>
</form><hr>
<script src="https://www.chartjs.org/dist/2.9.3/Chart.min.js"></script>
<script src="https://www.chartjs.org/samples/latest/utils.js"></script>
<style>
canvas {
    -moz-user-select: none;
    -webkit-user-select: none;
    -ms-user-select: none;
}
</style>
<div id="container" style="width: 60%;">
    <canvas id="canvas"></canvas>
</div>
<script>
    var color = Chart.helpers.color;
    var barChartData = {
        labels: [<?php echo $company; ?>],
        datasets: [{
            label: "Selected",
            backgroundColor: "#91bbff88",
            borderColor: "#91bbff",
            borderWidth: 2,
            data: [<?php echo $salary; ?>],
        },]
    };
    window.onload = function() {
        var ctx = document.getElementById("canvas").getContext("2d");
        window.myBar = new Chart(ctx, {
            type: "bar",
            data: barChartData,
            options: {
                responsive: true,
                legend: {
                    position: "top",
                },
                title: {
                    display: true,
                    text: "<?php echo $chart_title; ?>"
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                },
            }
        });
    };
    var colorNames = Object.keys(window.chartColors);
</script>
</div>