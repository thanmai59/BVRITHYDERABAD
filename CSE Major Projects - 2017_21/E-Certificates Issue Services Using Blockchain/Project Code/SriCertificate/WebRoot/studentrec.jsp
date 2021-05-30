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
        <title></title>
        <meta name="description" content="">
        <meta name="author" content="templatemo">
         <link href="css/studentcer.css" rel="stylesheet">
         <link href="css/regform.css" rel="stylesheet">
       <!-- <link class="jsbin" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1/themes/base/jquery-ui.css" rel="stylesheet" type="text/css" />-->
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
       <!--   <div id="container" class="container">
                <div style="width: 1200px;margin: 30px;color:white">
               <center><h1>E-Certificates Issue Services Using BlockChain</h1></center>
                </div>
            <div>
                <ul class="nav nav-justified">-->
      <div class="wrapper col1">
        <div id="header">
            <div id="logo">
                <table style="text-align: center;">
                    <tr>
                        <td><img src="https://www.noticebard.com/wp-content/uploads/2018/03/b-v-raju.png"
                            style="height: 100px; width: 100px;" alt=""></td>
                        <td>
                            <h1 style="margin-left:190px;font-size:35px">
                                <a href="#">BVRIT HYDERABAD College of Engineering For Women</a>
                            </h1> <br><span id="project">E-Certificates Issue Services Using BlockChain</span>
                        </td>
                    </tr>
                </table>
            </div>
            <br class="clear" />
        </div>
    </div>
        
         <div class="wrapper col2">
        <div id="topbar">
            <div id="topnav">
                <ul>    
                  <li class="active"><a href="stuview.jsp">Home</a></li>
                    <li><a href="studetails.jsp">Profile</a></li>
                    <li><a href="studentcer.jsp">ApplyCertificate</a></li>
                     <li><a href="studntviewcerdetails.jsp">ViewCertificateDetails</a></li>
                    <li><a href="studentrec.jsp">ApplyRecommendationLetter</a></li>
                 <li><a href="studntviewrecdetails.jsp">ViewRecommendationLetter</a></li>
                    <li><a href="index.jsp">Logout</a></li>
                </ul>
            </div>
            </div>
            </div>
            <br />
            <!--<div style="border: 1px solid white;border-radius: 20px;width: 600px;height: 500px;margin-left: 30%; background-color:grey;">
                <br>
                <center><h1 style="color: white">Student Apply Recommendation Letter Details</h1></center><br>
                <form action="studentRECaction.jsp" method="post"  style="margin-left: 50px"> 
                 <label style="font-size: 20px;color: white">RollNo</label>&nbsp;&nbsp;<input type="text" name="rollno" style="width: 200px;height: 20px;font-size: 20px;margin-left: 17px"/><br /><br />
                    <label style="font-size: 20px;color: white">Name</label>&nbsp;&nbsp;<input type="text" name="name" style="width: 200px;height: 20px;font-size: 20px;margin-left: 18px"/><br /><br />
                    <label style="font-size: 20px;color: white">emailid</label>&nbsp;&nbsp;<input type="email" name="email" style="width: 200px;height: 20px;font-size: 20px;margin-left:19px"/><br /><br />-->
                    <div class="container">
    <div class="title">Student Apply Recommendation Letter</div>
    <div class="content">
      <form action="studentRECaction.jsp" method="post"> 
        <div class="user-details">
          <div class="input-box">
            <span class="details">Roll no</span>
            <input type="text" placeholder="Enter Roll Number" name="rollno" required>
          </div>
          <div class="input-box">
            <span class="details">Name</span>
            <input type="text" placeholder="Enter your name" name="name"  required>
          </div>
          <div class="input-box">
            <span class="details">Email Id</span>
            <input type="text" placeholder="Enter your email" name="email" required>
          </div>
                   
                   <%
                            try {
                                Connection con = Database.getConnection();
                                Statement st = con.createStatement();
                                ResultSet rs = st.executeQuery("select * from Faculty");
                                
                                
                                
                        %>
                   
                    <!--<label style="font-size: 20px;color: white">SelectFaculty</label>&nbsp;&nbsp;
                    <select name="utype" style="width: 200px;height: 30px;font-size: 20px">-->
                     <div class="input-box">
            <span class="details">Select Faculty</span>
            <select name="utype" required style="width:200px;height:30px">
            
                    <%
                            while (rs.next())
                            {
                        String name=rs.getString("name");
                     %>
                        <option value="<%=name%>"><%=name%></option>
                        <%} %>
                       </select>
                       <%}
                       catch(SQLException se){
                       }
                       
                        %>
                        </div> 
                       <!-- <br /><br />
                    <label style="font-size: 20px;color: white">LetterName</label>&nbsp;&nbsp;<input type="text" name="cname" style="width: 200px;height: 20px;font-size: 20px;margin-left: 17px"/><br /><br />
                    <label style="font-size: 20px;color: white">DESCRIPTION</label><textarea rows="2" cols="3" name="Description" style="width: 200px;height: 20px;font-size: 20px;margin-left: 18px"></textarea><br />
                    <input type="submit" value="Add" style="width: 130px;height: 35px;margin-left: 80px;border-radius: 8px;font-size: 20px;background: white;margin-top: 10px"/>&nbsp;&nbsp;
                    <input type="reset" value="Reset" style="width: 130px;height: 35px;border-radius: 8px;font-size: 20px;background: white"/>-->
                  <div class="input-box">
            <span class="details">Letter Name</span>
            <input type="text" placeholder="letter for?" name="cname" required>
          </div>  
          <div class="input-box">
            <span class="details">Sample Letter</span>
            <input type="file" name="fname" required>
          </div> 
          <div class="input-box">
            <span class="details">Description</span>
            <textarea rows="3" cols="40" name="Description" required></textarea>
          </div>  
           <input type="submit" class="button" value="Add"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <input type="Reset" class="button" value="Reset" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          
      </form>
    </div>
  </div>
                </form>
            </div>
        </div>

            <div style="margin-left: 750px;margin-top: -350px;">
                <img id="blah" src="#" alt="" />
            </div>
        </div> <!-- /container -->
        <div>
            <p style="margin-left: 550px;color: red">&nbsp;<a href="" style="text-decoration: none;color: red"></a></p>
        </div>
    </body>
</html>