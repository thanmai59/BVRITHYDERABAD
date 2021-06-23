<?php
error_reporting(E_ERROR | E_PARSE);
session_start();
include 'config.php';
$conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
if ($conn->connect_error) {
    die("Connection failed: ".$conn->connect_error);
}
date_default_timezone_set("Asia/Kolkata");
if ($_POST["action"]=="Login") {
    $email = $_POST["email"];
    $table_name = $_POST["role"];
    $sql = "SELECT * FROM $table_name WHERE email = '$email'";
    $result = $conn->query($sql);
    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            if ($row["password"] == $_POST["password"]){
                $_SESSION["user_id"] = $row["id"];
                $_SESSION["role"] = $table_name;
            } else {
                $error = "Password wrong!!";
            }
        }
    } else {
        $error = "No user found!!";
    }
}
if ($_POST["action"]=="Register") {
    $email = $_POST["email"];
    $table_name = $_POST["role"];
    $sql = "SELECT * FROM $table_name WHERE email = '$email'";
    $result = $conn->query($sql);
    $error = "SQL Error occured!!";
    if ($result->num_rows > 0) {
        $error = "User already exists!!";
    } else if ($table_name=='student' || $table_name=='alumni') {
        $data["email"] = $email;
        $data["password"] = $_POST["password"];
        $id = insert($table_name,$data);
        if($id){
            $_SESSION["user_id"] = $id;
            $_SESSION["role"] = $table_name;
            $error = "Registration successfull.";
        }
    }
}
if($_GET["logout"]=="yes"){
    session_destroy();
    header("Location: index.php");
}
if (isset($_SESSION["user_id"])) {
    $user_id = $_SESSION["user_id"];
    $role = $_SESSION["role"];
}