<?php
include 'header.php';
if (isset($error)) {
    echo '<h2 style="color:red">'.$error.'</h2>';
}
if (isset($user_id)) {
    $role_name = $_SESSION["role"];
    $details = get_row("SELECT first_name,last_name from $role_name where id=$user_id");
    echo '<h2>You are logged in as '.$details->first_name.' '.$details->last_name.'</h2>';
    if ($_POST["action"]) {
        // save extra meta details
        $data["first_name"] = $_POST["first_name"];
        $data["last_name"] = $_POST["last_name"];
        $data["date_of_birth"] = $_POST["date_of_birth"];
        $data["address"] = $_POST["address"];
        $data["mobile_number"] = $_POST["mobile_number"];
        $data["yoj"] = $_POST["yoj"];
        $data["yog"] = $_POST["yog"];
        update($table_name,$data,array("id"=>$user_id));
        redirect_to_same();
    }
} else {
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
            <td><textarea name="address" rows="4"></textarea>
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
            <td><input type="hidden" name="role" value="student"></td>
            <td><input type="submit" name="action" value="Register" class="ui mini blue button"></td>
        </tr>
    </table>
</form>
</div>
    <?php
    if (!isset($user_id)) {
        echo '<br><p>Already have account? <a href="alumni_login.php">Login Here</a></p>';
    }
}