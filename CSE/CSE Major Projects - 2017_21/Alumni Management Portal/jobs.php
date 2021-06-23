<?php
include 'header.php';
$table_name = 'job';
if($_POST["action"]){
    $data["job"] = $_POST["job"];
    $data["company"] = $_POST["company"];
    $data["location"] = $_POST["location"];
    $data["salary"] = $_POST["salary"];
    $data["job_contact"] = $_POST["job_contact"];
    $data["link"] = $_POST["link"];
    if($_POST["action"]=='Add'){
        $data["alumni"] = $user_id;
        insert($table_name,$data);
        require 'send_mail.php';
        $students = get_results("SELECT email,first_name,last_name FROM student");
        foreach ($students as $student) {
            $mail->addAddress($student->email, $student->first_name.' '.$student->last_name);
        }
        $mail->isHTML(true);
        $mail->Subject = "New Job - ".$data["job"];
        $mail->Body = "<h2>Job Role: ".$data["job"]."</h2>";
        $mail->Body .= "<h2>Company: ".$data["company"]." - Salary: ".$data["salary"]."</h2>";
        $mail->Body .= "<h2>Location: ".$data["location"]."</h2>";
        $mail->Body .= "<h2>Contact for Job: ".$data["job_contact"]."</h2>";
        $mail->Body .= "<h2>Link: <a href='".$data["link"]."'>".$data["link"]."</a></h2>";

        $mail->AltBody = 'New Job - '.$data["job"].' Company: '.$data["company"].' Location: '.$data["location"].' Salary: '.$data["salary"].' Conact: '.$data["contact"].' Link: '.$data["link"];

        try {
            $mail->send();
            echo "Message has been sent successfully";
            if(function_exists("redirect_to_same")){
                redirect_to_same();
            }
        } catch (Exception $e) {
            echo "Mailer Error: " . $mail->ErrorInfo;
        }
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
            <td>Job</td>
            <td><input type="text" name="job">
            </td>
        </tr>
        <tr>
            <td>Company</td>
            <td><input type="text" name="company">
            </td>
        </tr>
        <tr>
            <td>Location</td>
            <td><input type="text" name="location">
            </td>
        </tr>
        <tr>
            <td>Salary</td>
            <td><input type="text" name="salary">
            </td>
        </tr>
        <tr>
            <td>Job Contact</td>
            <td><input type="text" name="job_contact">
            </td>
        </tr>
        <tr>
            <td>Job Link</td>
            <td><input type="text" name="link">
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
        $('input[name=job]').val('<?php echo $data["job"]; ?>');
        $('input[name=company]').val('<?php echo $data["company"]; ?>');
        $('input[name=location]').val('<?php echo $data["location"]; ?>');
        $('input[name=salary]').val('<?php echo $data["salary"]; ?>');
        $('input[name=job_contact]').val('<?php echo $data["job_contact"]; ?>');
        $('input[name=link]').val('<?php echo $data["link"]; ?>');
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
                <th>Job</th>
                <th>Company</th>
                <th>Location</th>
                <th>Salary</th>
                <th>Job Contact</th>
                <th>Link</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            <?php
            $rows = get_results("SELECT * FROM $table_name ORDER BY id DESC");
            foreach($rows as $row){
                echo '<tr row-id="'.$row->id.'">';
                echo '<td>'.$row->job.'</td>';
                echo '<td>'.$row->company.'</td>';
                echo '<td>'.$row->location.'</td>';
                echo '<td>'.$row->salary.'</td>';
                echo '<td>'.$row->job_contact.'</td>';
                echo '<td>';
                if ($row->link) {
                    echo '<a href="'.$row->link.'">Open Link</a>';                    
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

