<?php
include 'database.php';
include 'functions.php';
if ($_POST["message"]) {
	if ($user_id==$_POST["user_id"]) {
		$data[$role] = $user_id;
		$data["message"] = $_POST["message"];
		$data["group_chat"] = $_POST["group_chat"];
		insert('message',$data);
		echo $_POST["message"];
	}
}