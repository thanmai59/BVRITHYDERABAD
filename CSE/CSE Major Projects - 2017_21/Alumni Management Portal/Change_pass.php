<?php
include 'header.php';
include 'database.php';
session_start();
$_SESSION['type']=$_GET["type"];
$type=$_SESSION['type'];
if(isset($_POST['submit']))
{
       $email_id=$_POST['email'];
        $sql="SELECT * from $type where email ='$email_id'";
        $result=mysqli_query($conn,$sql);
        $resultchk=mysqli_num_rows($result);
        if($resultchk<1)
        
        {
            echo "This is not  a registered email id";
        }
        else{
        require 'send_mail.php';
        $OTP=rand(10000,99999);
        $_SESSION['OTP']=$OTP;
        $row=mysqli_fetch_assoc($result);
        $_SESSION['id']=$row['id'];
        
        $mail->addAddress($email_id);
        $mail->isHTML(true);
    
        $mail->Subject = "REQUEST TO CHANGE PASSWORD";
        $mail->Body = "<h2>Please don't share your OTP with anyone else</h2>";
        $mail->Body .= "<h2>OTP: ".$OTP."</h2>";
         $mail->AltBody = 'OTP - '.$OTP.' Don\'t share your otp with others';

        try {
            $mail->send();
           
        } catch (Exception $e) {
           // echo "Mailer Error: " . $mail->ErrorInfo;
        }
         echo("<script language=\"javascript\">"); 
                  
                 echo("location.href = \"http:/../alumini/verify_otp.php\"; " );
                      echo("</script>");
    }
 }   
?>
<div style="overflow-x:auto">
<form action="" method="post" id="main_form">
    <table class="ui blue celled table fixed collapsing unstackable sortable">
        <tr>
            <td>Email ID</td>
            <td><input type="email" name="email" required="">
            </td>
        </tr>
       
        <tr>
            <td><input type="hidden" name="role" value="student"></td>
            <td><input type="submit" name="submit" value="Send OTP" class="ui mini blue button"></td>
        </tr>
    </table>
</form>
</div>
