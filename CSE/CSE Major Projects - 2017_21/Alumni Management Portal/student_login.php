<?php
include 'header.php';
if (isset($error)) {
    echo '<h2 style="color:red">'.$error.'</h2>';
} elseif (isset($user_id)) {
    $role_name = $_SESSION["role"];
    $details = get_row("SELECT first_name,last_name from $role_name where id=$user_id");
    echo '<h2>You are logged in as '.$details->first_name.' '.$details->last_name.'</h2>';
    echo '<a href="?logout=yes">Click here to logout</a>';
    if ($_POST["action"]) {
        redirect_to_same();
    }
} else {
?>
<div style="overflow-x:auto">
<form action="" method="post" id="main_form">
    <table class="ui blue celled table fixed collapsing unstackable sortable">
        <tr>
            <td>User Email</td>
            <td><input type="email" name="email" required="">
            </td>
        </tr>
        <tr>
            <td>Password</td>
            <td><input type="password" name="password" required="">
            </td>
        </tr>
        <tr>
            <td><input type="hidden" name="role" value="student"></td>
            <td><input type="submit" name="action" value="Login" class="ui mini blue button"></td>
        </tr>
    </table>
</form>
</div>
<br><p>New User? <a href="student_register.php">Register Here</a></p>
<br><p>Forgot Password? <a href="Change_pass.php?type=student">Change Password</a></p>

    <?php
}