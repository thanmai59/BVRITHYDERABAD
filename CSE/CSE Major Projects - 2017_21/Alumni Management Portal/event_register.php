<?php
include 'header.php';
$table_name = 'event_register';
if($_POST["action"]){
    $data["event"] = $_POST["event"];
    $data["team_count"] = $_POST["team_count"];
    $data["team_names"] = $_POST["team_names"];
    if($_POST["action"]=='Add'){
        $data["student"] = $user_id;
        insert($table_name,$data);
        if(function_exists("redirect_to_same")){
            redirect_to_same();
        }
    } else if($_POST["action"]=='Apply for New Event' || $_POST["action"]=='Edit'){
        if($_POST["action"]=='Edit'){
            $id = $_POST["id"];
            $data = get_row("SELECT * FROM $table_name WHERE id = $id and student=$user_id",ARRAY_A);
        }
    ?>
    <hr>
    <form method="POST" enctype="multipart/form-data">
        <h2 id="small_frm">Apply for New Event Here</h2>
        <input type="hidden" name="id">
        <table class="ui blue striped table collapsing">
        <tr>
        <td>Event</td>
        <?php
        $event_opts = get_results("SELECT id,event FROM event",ARRAY_A);
        ?>
        <td><select name="event">
            <?php
            foreach ($event_opts as $key) { 
                echo '<option value="'.$key["id"].'">'.$key["event"].'</option>';
            }
            ?>
            </select>
        </td>
        </tr>
        <tr>
            <td>Team Count</td>
            <td><input type="number" name="team_count">
            </td>
        </tr>
        <tr>
            <td>Team Member Names</td>
            <td><textarea name="team_names" rows="5"><?php echo $data["team_names"]; ?></textarea>
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
        ?>
        <script type="text/javascript">
            $('input[name=action]').val('Save');
            $('input[name=id]').val('<?php echo $_POST["id"]; ?>');
            $('#small_frm').html('Edit Here');
        </script>
    <script type="text/javascript">
        $('select[name=event]').val('<?php echo $data["event"]; ?>');
        $('input[name=team_count]').val('<?php echo $data["team_count"]; ?>');
    </script>
        <?php
    }
    if($_POST["action"]=='Save'){
        $id = $_POST["id"];
        update($table_name,$data,array('id' => $id, 'student'=>$user_id));
        if(function_exists("redirect_to_same")){
            redirect_to_same();
        }
    }
    if($_POST["action"]=='Delete'){
        $id = $_POST["id"];
        delete($table_name,array('id' => $id, 'student'=>$user_id));
        if(function_exists("redirect_to_same")){
            redirect_to_same();
        }
    }
} 
if(($_POST["action"]!='Edit') && $_POST["action"]!='Apply for New Event') {
    ?>
    <form method="POST"><input type="submit" name="action" value="Apply for New Event" class="ui green button"></form><br>
    <div style="overflow-x:auto">
    <table id="myTable" class="ui unstackable celled table dataTable">
        <thead>
            <tr>
                <th>Event</th>
                <th>Team Count</th>
                <th>Team Names</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            <?php
            $rows = get_results("SELECT * FROM $table_name ORDER BY id DESC");
            $event_opts = get_results("SELECT id,event FROM event",OBJECT_K);
            foreach($rows as $row){
                echo '<tr row-id="'.$row->id.'">';
                echo '<td>'.$event_opts[$row->event]->event.'</td>';
                echo '<td>'.$row->team_count.'</td>';
                echo '<td><pre>'.$row->team_names.'</pre></td>';
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