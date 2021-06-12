<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.Connection"%>
<%@page import="action.Database"%>
<%@page import="java.sql.SQLException"%>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Word Co-extraction</title>
        <meta name="description" content="">
        <meta name="author" content="templatemo">
        <link href="css/style.css" rel="stylesheet">
        <link class="jsbin" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1/themes/base/jquery-ui.css" rel="stylesheet" type="text/css" />
        <script class="jsbin" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
        <script class="jsbin" src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.0/jquery-ui.min.js"></script>
    </head>
    <body>
        <script>
            function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#blah')
                    .attr('src', e.target.result)
                    .width(450)
                    .height(300);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }
            
        </script>
        <div id="container" class="container">
                <div style="width: 1200px;margin: 30px;color:lightgreen">
               <center><h1>E-Certificates Issues Services Using BlockChain</h1></center>
                </div>
            <div>
                <ul class="nav nav-justified">
                  <li class="active"><a href="stuview.jsp">Home</a></li>
                    <li><a href="studetails.jsp">Profile</a></li>
                    <li><a href="studentcer.jsp">ApplyCertificate</a></li>
                     <li><a href="studntviewcerdetails.jsp">ViewCertificateDetails</a></li>
                    <li><a href="studentrec.jsp">ApplyRecommendationLetter</a></li>
                 <li><a href="studntviewrecdetails.jsp">ViewRecommendationLetter</a></li>
                  <li><a href="SAMPLELETTER.jsp">SAMPLELetter</a></li>
                    <li><a href="index.jsp">Logout</a></li>
                </ul>
            </div><br />
            <div style="border: 1px solid white;border-radius: 20px;width: 500px;height: 400px;margin-left: 130px;">
                <center><h1 style="color: white">Student Apply Recommendation Letter Details</h1></center>
                <form action="SAMPLELETTERaction.jsp" method="post"  style="margin-left: 50px"> 
              
             <label style="font-size: 20px;color: white">LetterName</label>&nbsp;&nbsp;<input type="text" name="lname" style="width: 200px;height: 20px;font-size: 20px;margin-left: 17px"/><br /><br />
             <label style="font-size: 20px;color: white">Upload</label>&nbsp;&nbsp;&nbsp;&nbsp;<input type="file" name="fname" style="width: 200px;height: 20px;font-size: 20px;margin-left: 15px"/><br /><br />
                    <input type="submit" value="Add" style="width: 130px;height: 35px;margin-left: 80px;border-radius: 8px;font-size: 20px;background: white;margin-top: 10px"/>&nbsp;&nbsp;
                    <input type="reset" value="Reset" style="width: 130px;height: 35px;border-radius: 8px;font-size: 20px;background: white"/>
                </form>

            <div style="margin-left: 750px;margin-top: -350px;">
                <img id="blah" src="#" alt="" />
            </div>
        </div> <!-- /container -->
        <div>
            <p style="margin-left: 550px;color: red">&nbsp;<a href="" style="text-decoration: none;color: red"></a></p>
        </div>
    </body>
</html>