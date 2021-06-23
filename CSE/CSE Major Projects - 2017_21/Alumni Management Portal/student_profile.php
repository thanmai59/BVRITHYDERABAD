<?php
include 'header.php';
$table_name = 'student';
if (isset($user_id) && $role=='student') {
    if ($_POST["action"]) {
        // save extra meta details
        $data["email"] = $_POST["email"];
        $data["password"] = $_POST["password"];
        $data["first_name"] = $_POST["first_name"];
        $data["last_name"] = $_POST["last_name"];
        $data["date_of_birth"] = $_POST["date_of_birth"];
        $data["address"] = $_POST["address"];
        $data["mobile_number"] = $_POST["mobile_number"];
        $data["yoj"] = $_POST["yoj"];
        $data["yog"] = $_POST["yog"];
        $data["present_status"] = $_POST["present_status"];
        $data["job_acquired"] = $_POST["job_acquired"];
        $data["company"] = $_POST["company"];
        $data["college"] = $_POST["college"];
        $data["course"] = $_POST["course"];
        $data["country"] = $_POST["country"];
        $data["job_location"] = $_POST["job_location"];
        $data["designation"] = $_POST["designation"];
        $data["field_or_technology"] = $_POST["field_or_technology"];
        update($table_name,$data,array("id"=>$user_id));
        redirect_to_same();
    }
$data = get_row("SELECT * FROM student WHERE id = $user_id",ARRAY_A);
?>
<div style="overflow-x:auto">
<form action="" method="post" id="main_form">
    <table class="ui blue celled table fixed collapsing unstackable sortable">
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
            <td><textarea name="address" rows="4"><?php echo $data["address"]; ?></textarea>
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
            <td><input type="submit" name="action" value="Save" class="ui mini blue button"></td>
        </tr>
    </table>
</form>
<style type="text/css">
.higher{
    display: none;
}
</style>
<?php
?>
<script type="text/javascript">
    $('input[name=email]').val('<?php echo $data["email"]; ?>');
    $('input[name=password]').val('<?php echo $data["password"]; ?>');
    $('input[name=first_name]').val('<?php echo $data["first_name"]; ?>');
    $('input[name=last_name]').val('<?php echo $data["last_name"]; ?>');
    $('input[name=date_of_birth]').val('<?php echo $data["date_of_birth"]; ?>');
    $('input[name=mobile_number]').val('<?php echo $data["mobile_number"]; ?>');
    $('input[name=yoj]').val('<?php echo $data["yoj"]; ?>');
    $('input[name=yog]').val('<?php echo $data["yog"]; ?>');
</script>

</div>
    <?php
}