<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.Connection"%>
<%@page import="action.Database"%>
<!--  <!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title></title>
        <meta name="description" content="">
        <meta name="author" content="templatemo">
        <link href="css/style.css" rel="stylesheet">
    </head>
    <body>
        <div id="container" class="container">
            <div style="width: 1200px;margin: 30px;color: lightgreen">
                <center><h1>E-Certificates Issue Services Using BlockChain</h1></center>
            </div>
            <div> 
                <ul class="nav nav-justified">-->
 <!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    
     <link rel="stylesheet" href="css/certificate.css"/>
     <link rel="stylesheet" href="css/academic.css"/>
     
   
    <title>BVRITH Student Services</title>
  </head>
  <body>
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
	 <div>
             <ul>                
     <li class="active"><a href="fview.jsp">Home</a></li>
                    <li><a href="fdetails.jsp">Profile</a></li>
                    <li><a href="fviewRecdetails.jsp">ViewRecommendationLetterDetails</a></li>
                    <li><a href="index.jsp">Logout</a></li>
               
                </ul>
            </div><br />
            <!--
            <%
                String name = null, email = null, loc = null, cno = null;
                String n = session.getAttribute("n1").toString();
                
                String s = session.getAttribute("v").toString();
                System.out.println("Name " + n+"   "+s);
                Connection con = Database.getConnection();
                Statement st = con.createStatement();
                ResultSet rs = st.executeQuery("select * from Faculty where email='" + s + "'");
                if (rs.next()== true) {
                    name = rs.getString("name");
                    System.out.println("Name " + name);
                    email = rs.getString("email");
                    System.out.println("Email " + email);
                    loc = rs.getString("location");
                    System.out.println("Location " + loc);
                    cno = rs.getString("contactno");
                    System.out.println("Contact No  " + cno);
                }
            %>
            -->
            <div style="border:1px solid white;width: 600px;height: 400px;margin-left: 320px;background-color: grey;border-radius: 50px;"><br /><br />
                <center>
                        <div style="height: 300px;color: white">s
                        <h1>RecommendationLetter Details</h1><br/>
                         <form action="FRecaction.jsp" method="post"  style="margin-left: 50px"> 
                 <label style="font-size: 20px;color: white"></label>&nbsp;&nbsp;<input type="hidden" name="rollno"  value=<%= request.getParameter("rollno")%> style="width: 200px;height: 20px;font-size: 20px;margin-left: 17px"/><br /><br />
                  <label style="font-size: 20px;color: white"></label>&nbsp;&nbsp;<input type="hidden"     value=<%= request.getParameter("cName")%> name="lname" style="width: 200px;height: 20px;font-size: 20px;margin-left: 17px"/><br /><br />
                     <label style="font-size: 20px;color: white"></label><input type ="hidden"  value=<%= request.getParameter("DEscription")%> textarea rows="2" cols="3" name="Description" style="width: 200px;height: 20px;font-size: 20px;margin-left: 18px"></textarea><br />
                     <label style="font-size: 20px;color: white">Upload</label>&nbsp;&nbsp;&nbsp;&nbsp;<input type="file" name="fname" style="width: 200px;height: 30px;font-size: 20px;margin-right: 25%"/><br /><br />
                    <input type="submit" value="submit" style="width: 130px;height: 35px;border-radius: 8px;font-size: 20px;background: white;margin-top: 10px"/>&nbsp;&nbsp;
                    <input type="reset" value="Reset" style="width: 130px;height: 35px;border-radius: 8px;font-size: 20px;background: white"/>
                </form>
                 </div>
                </center>
            </div>
        </div> <!-- /container -->
        <div>
            <p style="margin-left: 650px;color: red">&nbsp;<a href="" style="text-decoration: none;color: red"></a></p>
        </div>
    </body>
</html>