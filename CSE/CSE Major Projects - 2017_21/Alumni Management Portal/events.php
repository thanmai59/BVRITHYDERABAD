<?php
include 'header.php';
$table_name = 'event';
if($_POST["action"]){
    $data["event"] = $_POST["event"];
    if (isset($_FILES["poster"]) && $_POST["poster_pid"]==1) {
        $target_dir = "uploads/";
        $target_file = $target_dir .time()."_".basename($_FILES["poster"]["name"]);
        $uploadOk = 1;
        $imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);
        $check = getimagesize($_FILES["poster"]["tmp_name"]);
        if($check !== false) {
            echo "File is valid - " . $check["mime"] . ".";
            $uploadOk = 1;
        } else {
            echo "File is not valid.";
            $uploadOk = 0;
        }
        if (file_exists($target_file)) {
            echo "Sorry, file already exists.";
            $uploadOk = 0;
        }
        if ($_FILES["poster"]["size"] > 500000) {
            echo "Sorry, your file is too large.";
            $uploadOk = 0;
        }
        if ($uploadOk == 0) {
            echo "Sorry, your file was not uploaded.";
        } else {
            if (move_uploaded_file($_FILES["poster"]["tmp_name"], $target_file)) {
                echo "The file ". basename( $_FILES["poster"]["name"]). " has been
                uploaded.";
                $data["poster"] = $target_file;
            } else {
                echo "Sorry, there was an error uploading your file.";
            }
        }
    }
    $data["event_date"] = $_POST["event_date"];
    $data["time"] = $_POST["time"];
    $data["location"] = $_POST["location"];
    if($_POST["action"]=='Add'){
        insert($table_name,$data);
        require 'send_mail.php';
        $students = get_results("SELECT email,first_name,last_name FROM student");
        foreach ($students as $student) {
            $mail->addAddress($student->email, $student->first_name.' '.$student->last_name);
        }
        $alumni = get_results("SELECT email,first_name,last_name FROM alumni");
        foreach ($alumni as $alumni) {
            $mail->addAddress($alumni->email, $alumni->first_name.' '.$alumni->last_name);
        }

        $mail->isHTML(true);

        $mail->Subject = "New Event - ".$data["event"];
        $mail->Body = "<h2>Event Name: ".$data["event"]."</h2>";
        $mail->Body .= "<h2>Date: ".$data["event_date"]." - Time: ".$data["time"]."</h2>";
        $mail->Body .= "<h2>Location: ".$data["location"]."</h2>";

        $mail->AltBody = 'New event - '.$data["event"].' Date: '.$data["event"].' Location: '.$data["location"];

        try {
            $mail->send();
            echo "Message has been sent successfully";
            if(function_exists("redirect_to_same")){
                redirect_to_same();
            }
        } catch (Exception $e) {
            echo "Mailer Error: " . $mail->ErrorInfo;
        }
    } else if($_POST["action"]=='Add New' || $_POST["action"]=='Edit'){
    ?>
    <hr>
    <form method="POST" enctype="multipart/form-data">
        <h2 id="small_frm">Add New Here</h2>
        <input type="hidden" name="id">
        <table class="ui blue striped table collapsing">
        <tr>
            <td>Event</td>
            <td><input type="text" name="event">
            </td>
        </tr>
        <tr>
        <td>Poster</td>
        <td>
            <img id="img_poster" style="max-width: 250px">
            <a id="link_poster" href="#">View</a><br>
            <input type="file" name="poster" id="poster" onchange="readURL(this)">
            <input type="hidden" name="poster_pid" id="poster_pid" value="0" />
        </td>
        <script type="text/javascript">
            function readURL(input) {
              if (input.files && input.files[0]) {
                var reader = new FileReader();
                reader.onload = function(e) {
                  $('#img_poster').attr('src', e.target.result);
                }
                reader.readAsDataURL(input.files[0]);
              }
            }
            $("#poster").change(function() {
                readURL(this);
            $("#poster_pid").val("1");});
        </script>
        </tr>
        <tr>
            <td>Event Date</td>
            <td><input type="date" name="event_date">
            </td>
        </tr>
        <tr>
            <td>Time</td>
            <td><input type="text" name="time">
            </td>
        </tr>
        <tr>
            <td>Location</td>
            <td><input type="text" name="location">
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
        $('input[name=event]').val('<?php echo $data["event"]; ?>');
        <?php
        $file_url = $data["poster"];
        ?>
        $('#img_poster').attr('src','<?php echo $file_url; ?>');
        $("#link_poster").attr("href","<?php echo $file_url; ?>");
        $("#link_poster").attr("target","_blank");
        $('input[name=poster]').val('<?php echo $data["poster"]; ?>');
        $('input[name=event_date]').val('<?php echo $data["event_date"]; ?>');
        $('input[name=time]').val('<?php echo $data["time"]; ?>');
        $('input[name=location]').val('<?php echo $data["location"]; ?>');
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
                <th>Event</th>
                <th>Poster</th>
                <th>Event Date</th>
                <th>Time</th>
                <th>Location</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            <?php
            $rows = get_results("SELECT * FROM $table_name ORDER BY id DESC");
            foreach($rows as $row){
                echo '<tr row-id="'.$row->id.'">';
                echo '<td>'.$row->event.'</td>';
                $file_url = $row->poster;
                echo '<td>';
                if($file_url){
                    echo '<a href="'.$file_url.'" target="_blank"><b>View<b></a>';
                }
                echo '</td>';
                echo '<td>'.$row->event_date.'</td>';
                echo '<td>'.$row->time.'</td>';
                echo '<td>'.$row->location.'</td>';
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