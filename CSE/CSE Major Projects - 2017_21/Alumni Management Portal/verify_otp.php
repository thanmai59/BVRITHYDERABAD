<?php
include 'header.php';
include 'database.php';
session_start();

if(isset($_POST['submit']))
{
       $otp=$_POST['otp'];

       $pass=$_POST['pass'];
       $confrim_pass=$_POST['pass2'];
       $type=$_SESSION['type'];
       $id=$_SESSION['id'];
       if ($otp==$_SESSION['OTP']){
       if ($pass==$confrim_pass){
           $sql="UPDATE $type SET  `password` = '$pass' WHERE id = $id;"; 
          mysqli_query($conn,$sql);
           echo("<script language=\"javascript\">"); 
                            echo("alert('Password changed');" ); 
                           echo("top.location.href = \"http:../alumini/index.php\"; " );
                            echo("</script>");
       }   
       else{
        echo "New Password and Confrim password doesn't match";
       }
       }
       else
       {
        echo"INVALID OTP";
       }
    
 }   
?>
<div style="overflow-x:auto">
<form action="" method="post" id="main_form">
    <table class="ui blue celled table fixed collapsing unstackable sortable">
        <tr>
            <td>OTP</td>
            <td><input type="tetx" name="otp" required="">
            <td>NEW PASSWORD</td>
            <td><input type="PASSWORD" name="pass" required="">
            <td>Confrim PASSWORD</td>
            <td><input type="PASSWORD" name="pass2" required="">
            
            </td>
        </tr>
       
        <tr>
            <td><input type="hidden" name="role" value="student"></td>
            <td><input type="submit" name="submit" value="Change Password" class="ui mini blue button"></td>
        </tr>
    </table>
</form>
</div>
