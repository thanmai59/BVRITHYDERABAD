<?php
include 'header.php';
if (!$role=='alumni' && !$role=='student') {
	echo "<h2>Please login with alu</h2>";
	exit;
}
if ($_GET["group"]) {
$group = $_GET["group"];
if (!$_GET["full_chat"]) {
	$limit20 = ' LIMIT 20';
} else {
	$full_chat = " - Full Chat History";
}
$msgs = get_results("SELECT * FROM message WHERE group_chat=$group ORDER BY id DESC $limit20",ARRAY_A);
krsort($msgs);
$s = get_results("SELECT id,first_name,last_name FROM student",OBJECT_K);
$a = get_results("SELECT id,first_name,last_name FROM alumni",OBJECT_K);
$sender = get_row("SELECT first_name,last_name from $role where id=$user_id",ARRAY_A);
$sender_name = $sender["first_name"].' '.$sender["last_name"];
}
?>
<div class="main">
	<h2>Group Chat - EEE<?php echo $full_chat; ?></h2>
	<div id="chat_box">
		<table id="chat_table">
			<?php
			foreach ($msgs as $m) {
				$author = $m["alumni"] ? $a[$m["alumni"]]->first_name.' '.$a[$m["alumni"]]->last_name : $s[$m["student"]]->first_name.' '.$s[$m["student"]]->last_name;
				$ath_role = $m["alumni"] ? 'alumni' : 'student';
				?>
				<tr><td class="msg_row">
						<div class="msg_div u<?php echo $ath_role.$m[$ath_role]; ?>">
							<div class="author"><?php echo $author; ?></div>
							<div class="message"><?php echo $m["message"]; ?></div>
						</div>
					</td>
				</tr>
				<?php 
			} ?>
		</table>
	</div>
	<hr>
	<table>
		<tr>
			<td style="width: 100%">
				<div class="input">
					<input type="text" name="" style="width: 100%" id="input">
				</div>
			</td>
			<td>
				<button class="ui green button" onclick="run()">SEND</button>
			</td>
		</tr>
	</table>
	<script type="text/javascript">
		$("#input").keypress(function(event) {
            if (event.keyCode === 13) {
                run();
            }
        });
		function run(){
			var values = {
				'user_id' : <?php echo $user_id; ?>,
				'message' : document.getElementById('input').value,
				'group_chat' : <?php echo $group; ?>
			};
			$('#input').val('');
			$.ajax({
		        url: "ajax.php",
		        type: "post",
		        data: values ,
		        success: function (response) {
		        	if (response) {
			        	$('#chat_table').append('<tr><td class="msg_row">'+
							'<div class="msg_div u<?php echo $role.$user_id; ?>">'+
								'<div class="author"><?php echo $sender_name; ?></div>'+
								'<div class="message">'+response+'</div></div></td></tr>');
		        	}
		        },
		        error: function(jqXHR, textStatus, errorThrown) {
		           console.log(textStatus, errorThrown);
		        }
		    });
		    scrollchattobottom();
		}
		function scrollchattobottom() {
			var div = document.getElementById("chat_box");
        	$('#chat_box').animate({
		      scrollTop: div.scrollHeight
		   }, 1000);
		}
		scrollchattobottom();
	</script>
</div>
<center>
<?php
if (!$_GET["full_chat"]) {
	echo '<a href="?group='.$group.'&full_chat=1">FULL CHAT HISTORY</a>';
}
?>
</center>
<style type="text/css">
	.main{
		max-width: 800px;
		margin: auto;
		border: 3px solid green;
		border-radius: 15px;
		padding: 10px;
	}
	#chat_box{ 
		overflow-y: auto;
		height: 60vh;
	}
	#chat_table{ width: 100%; }
	.alumni{
		color: blue;
	}
	.student{
		color: red;
	}
	.author{
		font-weight: bold;
		display: inline-block;
		padding: 5px;
		margin: 0;
		font-style: italic;
	}
	.msg_div{
		padding: 5px;
		border: 1px solid black;
		border-radius: 5px;
		background-color: white;
		display: inline-block;
		max-width: 80%;
		margin: 2px;
		clear: both;
	}
	.u<?php echo $role.$user_id; ?>{
		float: right;
		text-align: right;
	}
	h1{
		display: none;
	}
</style>