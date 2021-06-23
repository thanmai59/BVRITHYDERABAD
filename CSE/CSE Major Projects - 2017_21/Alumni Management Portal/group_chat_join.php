<?php
include 'header.php';
$table_name = 'group_chat';
if($_POST["action"]=='Join'){
    $id = $_POST["id"];
    $row = get_row("SELECT * FROM $table_name WHERE id = $id",ARRAY_A);
    $mem = unserialize($row[$role]);
    if (!in_array($user_id, $mem)) {
	    array_push($mem,$user_id);
	    $data[$role] = serialize($mem);
    	update($table_name,$data,array('id' => $id));
	    if(function_exists("redirect_to_same")){
	        redirect_to_same();
	    }
    }
    
}
if(1) {
    ?>
    <div style="overflow-x:auto">
    <table id="myTable" class="ui unstackable celled table dataTable">
        <thead>
            <tr>
                <th>Group Chat</th>
                <th>Student</th>
                <th>Alumni</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            <?php
        $rows = get_results("SELECT * FROM $table_name ORDER BY id DESC");
        $student_opts = get_results("SELECT id,first_name,last_name FROM student",OBJECT_K);
        $alumni_opts = get_results("SELECT id,first_name,last_name FROM alumni",OBJECT_K);
            foreach($rows as $row){
            	$members["student"] = unserialize($row->student);
            	$members["alumni"] = unserialize($row->alumni);
                echo '<tr row-id="'.$row->id.'">';
                echo '<td>'.$row->group_chat.'</td>';
	            echo '<td>';
                foreach ($members["student"] as $x) {
	                echo $student_opts[$x]->first_name.' ';
	                echo $student_opts[$x]->last_name.'<br>';
                }
	            echo '</td>';
	            echo '<td>';
                foreach ($members["alumni"] as $x) {
	                echo $alumni_opts[$x]->first_name.' ';
	                echo $alumni_opts[$x]->last_name.'<br>';
                }
	            echo '</td>';
            ?>
            <td>
                <?php
                if (in_array($user_id, $members[$role])) {
                	echo '<a href="chat.php?group='.$row->id.'" class="ui mini blue button">Open</a>';
                } else {
                	?>
	                <form method="post">
	                <input type="hidden" name="id" value="<?php echo $row->id; ?>">
	                <input type="submit" name="action" class="ui mini blue button" value="Join">
	                </form>
	                <?php
                }
                ?>
            </td>
            <?php
                echo '</tr>';
            }
            ?>
        </tbody>
    </table>
    </div>
    <?php
}