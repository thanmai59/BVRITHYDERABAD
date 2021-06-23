<?php
include 'header.php';
if ($_SESSION["role"]!='admin') {
    echo "<h3>You are not an ADMIN</h3>";
    exit;
}
$table_name = 'student';
if($_POST["action"]){
    $data["email"] = $_POST["email"];
    $data["password"] = $_POST["password"];
    $data["first_name"] = $_POST["first_name"];
    $data["last_name"] = $_POST["last_name"];
    $data["date_of_birth"] = $_POST["date_of_birth"];
    $data["address"] = $_POST["address"];
    $data["mobile_number"] = $_POST["mobile_number"];
    $data["yoj"] = $_POST["yoj"];
    $data["yog"] = $_POST["yog"];
    if($_POST["action"]=='Add'){
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
            <td>Email</td>
            <td><input type="email" name="email" required="">
            </td>
        </tr>
        <tr>
            <td>Password</td>
            <td><input type="password" name="password" required=""> <i class="ui large eye icon slash"></i>
                <script type="text/javascript">
                    var x = $(".eye.icon");
                    x.on("click",function(){
                        if (x.hasClass("slash")) {
                            x.removeClass("slash");
                            x.parent().children("input").attr("type","text");
                        } else {
                            x.addClass("slash");
                            x.parent().children("input").attr("type","password");
                        }
                    });
                </script>
            </td>
        </tr>
        <tr>
            <td>First Name</td>
            <td><input type="text" name="first_name">
            </td>
        </tr>
        <tr>
            <td>Last Name</td>
            <td><input type="text" name="last_name">
            </td>
        </tr>
        <tr>
            <td>Date Of Birth</td>
            <td><input type="date" name="date_of_birth">
            </td>
        </tr>
        <tr>
            <td>Address</td>
            <td><input type="text" name="address">
            </td>
        </tr>
        <tr>
            <td>Mobile Number</td>
            <td><input type="text" name="mobile_number" maxlength="10">
            </td>
        </tr>
        <tr>
            <td>Year of Joining</td>
            <td><input type="number" name="yoj" maxlength="4" min="2012" max="2050" autocomplete="off">
            </td>
        </tr>
        <tr>
            <td>Year of Graduation</td>
            <td><input type="number" name="yog" maxlength="4" min="2012" max="2050" autocomplete="off">
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
            
            $('input[name=email]').val('<?php echo $data["email"]; ?>');
            $('input[name=password]').val('<?php echo $data["password"]; ?>');
            $('input[name=first_name]').val('<?php echo $data["first_name"]; ?>');
            $('input[name=last_name]').val('<?php echo $data["last_name"]; ?>');
            $('input[name=date_of_birth]').val('<?php echo $data["date_of_birth"]; ?>');
            $('input[name=address]').val('<?php echo $data["address"]; ?>');
            $('input[name=mobile_number]').val('<?php echo $data["mobile_number"]; ?>');
            $('input[name=yoj]').val('<?php echo $data["yoj"]; ?>');
            $('input[name=yog]').val('<?php echo $data["yog"]; ?>');
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
                <th>Personal Details</th>
                <th>Address</th>
                <th>Year of Joining</th>
                <th>Year of Graduation</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            <?php
            $rows = get_results("SELECT * FROM $table_name ORDER BY id DESC");
            foreach($rows as $row){
                echo '<tr row-id="'.$row->id.'">';
                echo '<td><b>Email:</b> '.$row->email.'
                <br><b>Password:</b> '.$row->password.'
                <br><b>First name:</b> '.$row->first_name.'
                <br><b>Last name:</b> '.$row->last_name.'</td>';
                echo '<td><b>Date of birth:</b> '.$row->date_of_birth.'
                <br><b>Mobile number:</b> '.$row->mobile_number.'
                <br><b>Address:</b> '.$row->address.'</td>';
                echo '<td>'.$row->yoj.'</td>';
                echo '<td>'.$row->yog.'</td>';
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