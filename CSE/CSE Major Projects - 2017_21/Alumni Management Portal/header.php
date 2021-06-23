<?php
include 'functions.php';
include 'database.php';
?>
<!DOCTYPE html>
<html>
<head>
    <title><?php 
    $file = end(explode("/",$_SERVER["PHP_SELF"]));
    $file_name = substr($file, 0, -4);
    $file_name = ucwords(str_replace("_", " ", $file_name));
    echo $file_name; ?></title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.4.1/semantic.css">
    <script type="text/javascript" src="https://code.jquery.com/jquery-3.4.1.js"></script>
</head>
<body>
    <div id="color-overlay"></div>
<header>
<div class="topnav" id="myTopnav">
    <a href="index.php">Home</a>
    <?php
    if (isset($user_id)){
        if($_SESSION["role"]=='admin'){
            ?>
            <a href="alumni_list.php">Alumni List</a>
            <a href="students_list.php">Students List</a>
            <a href="events.php">Events</a>
            <a href="event_register_list.php">Event Register List</a>
            <a href="group_chats.php">Group Chats</a>
            <a href="alumni_reports.php">Alumni Reports</a>
            <a href="student_reports.php">Student Reports</a>
            <a href="stats.php">Stats</a>
            <?php
        } else if ($_SESSION["role"]=='alumni'){
            ?>
            <a href="alumni_profile.php">Alumni Profile</a>
            <a href="jobs.php">Jobs</a>
            <a href="materials.php">Materials</a>
            <a href="group_chat_join.php">Group Chat Join</a>
            <?php
        } else if ($_SESSION["role"]=='student'){
            ?>
            <a href="student_profile.php">Student Profile</a>
            <a href="jobs_list.php">Jobs List</a>
            <a href="events_list.php">Events List</a>
             <a href="alumni_reports.php">Alumni Reports</a>
            <a href="group_chat_join.php">Group Chat Join</a>
            <?php
        }
        ?>
        <a href="?logout=yes">Logout</a>
        <?php
    } else {
        ?>
        <a href="admin_login.php">Admin</a>
        <a href="alumni_login.php">Alumni</a>
        <a href="student_login.php">Student</a>
        <?php
    }
    ?>
    <a href="javascript:void(0);" class="icon" onclick="myFunction()">
    <i class="fa fa-bars"></i>
    </a>
</div>
<script>
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}
</script>
<style>
body {
    position: relative;
    font-family: Arial, Helvetica, sans-serif;
    background-image: url('bg2.jpg');
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    background-color: #ffebeb;
    background-attachment: fixed;
}
a{
    color: blue;
    font-weight: bold;
}
#color-overlay {
    position: fixed;
    width: 100%;
    height: 100%;
    z-index: -5;
    background-color: white;
    opacity: 0.5;
}
main{
    margin: auto;
    padding: 20px;
}
.topnav {
    overflow: hidden;
    background-color: #333;
}
.topnav a {
    float: left;
    display: block;
    color: #f2f2f2;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    font-size: 17px;
}
.topnav a:hover {
    background-color: #ddd;
    color: black;
}
.topnav a.active {
    background-color: #4CAF50;
    color: white;
}
.topnav .icon {
    display: none;
}
@media screen and (max-width: 600px) {
    .topnav a:not(:first-child) {display: none;}
    .topnav a.icon {
    float: right;
    display: block;
    }
}
@media screen and (max-width: 600px) {
    .topnav.responsive {position: relative;}
    .topnav.responsive .icon {
        position: absolute;
        right: 0;
        top: 0;
    }
    .topnav.responsive a {
        float: none;
        display: block;
        text-align: left;
    }
}
td select, td input{
    height: 30px;
}
a[href="<?php echo $file ?>"]{
    background-color: #7a7a7d;
}
</style>
</header>
<main>
<?php
if ($file_name!='Index') {
    echo '<h1>'.$file_name.'</h1>';
}
