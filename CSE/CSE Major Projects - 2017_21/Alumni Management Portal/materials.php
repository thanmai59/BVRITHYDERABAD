<?php
include 'header.php';
$table_name = 'material';
if($_POST["action"]){
    $data["material"] = $_POST["material"];
    if (isset($_POST["file_pid"]) && $_POST["file_pid"]==0) {
        $target_dir = "uploads/";
        $target_file = $target_dir .time()."_".basename($_FILES["file"]["name"]);
        $uploadOk = 1;
        $imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);
        if(isset($_POST["action"])) {
            $check = getimagesize($_FILES["file"]["tmp_name"]);
            if($check !== false) {
                echo "File is valid - " . $check["mime"] . ".";
                $uploadOk = 1;
            } else {
                echo "File is not valid.";
                $uploadOk = 0;
            }
        }
        if (file_exists($target_file)) {
            echo "Sorry, file already exists.";
            $uploadOk = 0;
        }
        if ($_FILES["file"]["size"] > 500000) {
            echo "Sorry, your file is too large.";
            $uploadOk = 0;
        }
        if ($uploadOk == 0) {
            echo "Sorry, your file was not uploaded.";
        } else {
            if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
                echo "The file ". basename( $_FILES["file"]["name"]). " has been
                uploaded.";
                $data["file"] = $target_file;
            } else {
                echo "Sorry, there was an error uploading your file.";
            }
        }
    } else {
        $data["file"] = $_POST["file"];
    }
    if($_POST["action"]=='Add'){
        $data["alumni"] = $user_id;
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
            <td>Material</td>
            <td><input type="text" name="material">
            </td>
        </tr>
        <tr>
        <td>File</td>
        <td>
            <input type="file" name="file" id="file">
            <input type="hidden" name="file_pid" id="file_pid" value="0" />
        </td>
        </tr>
            <tr>
                <td></td>
                <td><input type="submit" name="action" value="Add" class="ui mini blue button"></td>
            </tr>
        </table>
        </form>
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
        $('input[name=material]').val('<?php echo $data["material"]; ?>');
        <?php
        $file_url = $data["file"];
        ?>
        $("#link_file").attr("href","<?php echo $file_url; ?>");
        $("#link_file").attr("target","_blank");
    </script>
        <?php
    }
    if($_POST["action"]=='Save'){
        $id = $_POST["id"];
        update($table_name,$data,array('id' => $id,'alumni'=>$user_id));
        if(function_exists("redirect_to_same")){
            redirect_to_same();
        }
    }
    if($_POST["action"]=='Delete'){
        $id = $_POST["id"];
        delete($table_name,array('id' => $id,'alumni'=>$user_id));
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
                <th>Material</th>
                <th>File</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            <?php
            $rows = get_results("SELECT * FROM $table_name where alumni=$user_id ORDER BY id DESC");
            foreach($rows as $row){
                echo '<tr row-id="'.$row->id.'">';
                echo '<td>'.$row->material.'</td>';
                $file_url = $row->file;
                echo '<td>';
                if($file_url){
                    echo '<a href="'.$file_url.'" target="_blank"><b>View<b></a>';
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