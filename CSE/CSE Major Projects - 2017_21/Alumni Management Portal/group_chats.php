<?php
include 'header.php';
$table_name = 'group_chat';
if($_POST["action"]){
    $data["group_chat"] = $_POST["group_chat"];
    if($_POST["action"]=='Add'){
        $data["student"] = serialize(array());
        $data["alumni"] = serialize(array());
        insert($table_name,$data);
        if(function_exists("redirect_to_same")){
            redirect_to_same();
        }
    } else if($_POST["action"]=='Add New' || $_POST["action"]=='Edit'){
    ?>
    <hr>
    <form method="POST" enctype="multipart/form-data">
        <h2 id="small_frm">Add New Here</h2>
        <input type="hidden" name="id">
        <table class="ui blue striped table collapsing">
        <tr>
            <td>Group Chat</td>
            <td><input type="text" name="group_chat">
            </td>
        </tr>
        
            <tr>
                <td></td>
                <td><input type="submit" name="action" value="Add" class="ui mini blue button"></td>
            </tr>
        </table>
        </form>
        <style type="text/css">
            .ui.dropdown{
                width: 100% !important;
            }
        </style>
        <?php
    }
    if($_POST["action"]=='Edit'){
        $id = $_POST["id"];
        $row = get_row("SELECT * FROM $table_name WHERE id = $id",ARRAY_A);
        $data = $row;
        ?>
        <script type="text/javascript">
            $('input[name=action]').val('Save');
            $('input[name=id]').val('<?php echo $_POST["id"]; ?>');
            $('#small_frm').html('Edit Here');
        </script>
    <script type="text/javascript">
        $('input[name=group_chat]').val('<?php echo $data["group_chat"]; ?>');
    </script>
        <?php
    }
    if($_POST["action"]=='Save'){
        $id = $_POST["id"];
        update($table_name,$data,array('id' => $id));
        if(function_exists("redirect_to_same")){
            redirect_to_same();
        }
    }
    if($_POST["action"]=='Delete'){
        $id = $_POST["id"];
        delete($table_name,array('id' => $id));
        if(function_exists("redirect_to_same")){
            redirect_to_same();
        }
    }
} 
if(($_POST["action"]!='Edit') && $_POST["action"]!='Add New') {
    ?>
    <form method="POST"><input type="submit" name="action" value="Add New" class="ui green button"></form><br>
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
            	$student = unserialize($row->student);
                $alumni = unserialize($row->alumni);
                echo '<tr row-id="'.$row->id.'">';
                echo '<td>'.$row->group_chat.'</td>';
	            echo '<td>';
                foreach ($student as $x) {
	                echo $student_opts[$x]->first_name.' ';
	                echo $student_opts[$x]->last_name.'<br>';
                }
	            echo '</td>';
	            echo '<td>';
                foreach ($alumni as $x) {
	                echo $alumni_opts[$x]->first_name.' ';
	                echo $alumni_opts[$x]->last_name.'<br>';
                }
	            echo '</td>';
            ?>
            <td>
                <form method="post">
                <input type="hidden" name="id" value="<?php echo $row->id; ?>">
                <input type="submit" name="action" class="ui mini blue button" value="Edit">
                <input type="submit" name="action" class="ui mini red button" value="Delete">
                </form>
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