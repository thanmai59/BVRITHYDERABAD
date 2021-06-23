<?php
include 'database.php';
?>
<!DOCTYPE html>
<html>
<head>
	
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Alumni Management System</title>
	<style type="text/css">
		.content{
			max-width: 950px;
			text-align:center;
			margin: auto;
			font-family: Arial;
		}
		.forms{
			margin: auto;
			padding: 20px;
			margin-top: 50px;
			max-width: 500px;
			background-color: #ff69b4bd;
			border: 2px solid green;
		}
		.forms a{
			background-color: #ff69b4;
			display: block;
			height: 15px;
			margin: 10px;
			border: 2px solid brown;
			padding: 20px;
			text-decoration: none;
			font-weight: bold;
			font-size: 22px;
		}
		.forms a:hover{
			background-color: pink;
			color: black;
		}
		.forms img{
			border-radius: 5px;
		}
	</style>
</head>
<body>
	<div id="color-overlay"></div>
	<div class="content">
		<div class="forms">
			<img src="logo.jpg">
			<br>
			<a href="admin_login.php">ADMIN LOGIN</a>
			<a href="alumni_login.php">ALUMINI LOGIN</a>
			<a href="student_login.php">STUDENT LOGIN</a>
		</div>
	</div>
</body>
<style type="text/css">
body {
    position: relative;
    padding: 10px;
    font-family: Arial, Helvetica, sans-serif;
    background-image: url('bg2.jpg');
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    background-color: #ffebeb;
    background-attachment: fixed;
}
</style>
</html>

<?php
