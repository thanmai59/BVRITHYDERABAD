<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.Connection"%>
<%@page import="action.Database"%>
<!-- <!DOCTYPE html>
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
                <center><h1>E-Certificates Issues Services Using BlockChain</h1></center>
            </div>
            <div>
                <ul class="nav nav-justified">-->
 <!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title></title>
        <meta name="description" content="">
        <meta name="author" content="templatemo">
        
        <link href="css/academic.css" rel = "stylesheet"/> 
       
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
                   
                   <li><a href="ahome.jsp">Home</a></li>
                  <li><a href="adviewdetails.jsp">ViewStudentCertificateDetails</a></li>
                    <li><a href="index.jsp">Logout</a></li>
               </ul>
            </div><br />
            <div class="abstract" style="width:60%;margin-left:20%"><br><br>
                <center><h1 style="color: white;margin-top: -10px">StudentCertificate Details</h1></center><br/>
                <br><table style="margin-left: 280px;margin-top: -20px">
                    <tr>
                    <!--
                        <th style="background-color: blue">Rollno</th>
                        <th style="background-color: blue">Name</th>
                        <th style="background-color: blue">Emailid</th>
                        <th style="background-color: blue">UserType</th>
                        <th style="background-color: blue">CourseName</th>
                      <th style="background-color: blue">Description</th>
                       
               <th style="background-color: blue">UploadCertificate</th>
                -->
                    </tr>
                    <tr><!--
                        <%
                            try {
                                Connection con = Database.getConnection();
                                Statement st = con.createStatement();
                                ResultSet rs = st.executeQuery("select * from studentcertificate");
                                while (rs.next()) {%>
                          <td><%=rs.getString("rollno")%></td>
                        <td><%=rs.getString("name")%></td>
                        <td><%=rs.getString("emailid")%></td>
                        <td><%=rs.getString("UserType")%></td>
                        <td><%=rs.getString("cName")%></td>
                        <td><%=rs.getString("DEscription")%></td>
                        
                       
                  <td> <a href="aCeraccept.jsp?id=<%=rs.getString("rollno")%>" style="width:60px;height:45px;">UploadHere</a></td> 
                    
                    </tr>
                    <% }
                        } catch (Exception e) {
                            e.printStackTrace();
                            System.out.println("Admin viewcerti details Page" + e.getMessage());
                        }
                    %>
                --></table>
                
                
               <center>
                <br/>
                        <div style="height: 300px;color: white">
                        <h2>Certificate Details</h2>
                         <form action="ARcaction.jsp" method="post"  style="margin-left: 50px"> 
                 <label style="font-size: 20px;color: white"></label>&nbsp;&nbsp;<input type="hidden" name="rollno"  value=null style="width: 200px;height: 20px;font-size: 20px;margin-left: 17px"/><br /><br />
                
                     <label style="font-size: 20px;color: white">Upload</label>&nbsp;&nbsp;&nbsp;&nbsp;<input type="file" name="fname" style="width: 200px;height: 30px;font-size: 20px;margin-left: 15px"/><br /><br />
                    <input type="submit" value="submit" style="width: 130px;height: 35px;margin-left: 80px;border-radius: 8px;font-size: 20px;background: white;margin-top: 10px"/>&nbsp;&nbsp;
                    <input type="reset" value="Reset" style="width: 130px;height: 35px;border-radius: 8px;font-size: 20px;background: white"/>
                </form>
                 </div>
                </center>
                
            </div>
        </div> <!-- /container -->
        <div>
            <p style="margin-left: 550px;color: red">&nbsp;<a href="" style="text-decoration: none;color: red"></a></p>
        </div>
    </body>
</html>