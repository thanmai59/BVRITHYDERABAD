<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.Connection"%>
<%@page import="action.Database"%>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title></title>
        <meta name="description" content="">
        <meta name="author" content="templatemo">
        <link href="css/studentcer.css" rel="stylesheet">
    </head>
    <body>
        <!-- <div id="container" class="container">
            <div style="width: 1200px;margin: 30px;color: white">
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
        
            <div>
                <ul>          
           <li class="active"><a href="stuview.jsp">Home</a></li>
                    <li><a href="studetails.jsp">Profile</a></li>
                    <li><a href="studentcer.jsp">ApplyCertificate</a></li>
                     <li><a href="studntviewcerdetails.jsp">ViewCertificateDetails</a></li>
                    <li><a href="studentrec.jsp">ApplyRecommendationLetter</a></li>
                 <li><a href="studntviewrecdetails.jsp">ViewRecommendationLetter</a></li>
                    <li><a href="index.jsp">Logout</a></li>  
                </ul>
            </div><br />
            <div class="abstract" style="background: ;margin-left:2%;"><br><br>
                <center><h1 style="color: white;margin-top: -10px">Certificate Details</h1></center><br/>
                <br><table style="margin-left: 35%;margin-top: -20px">
                    <tr>
                        <!-- <th style="background-color: blue">Rollno</th>
                        <th style="background-color: blue">Name</th>
                        <th style="background-color: blue">Emailid</th>
                        <th style="background-color: blue">UserType</th> -->
                        <th style="background-color: blue">CertiFicateName</th>
                      
                        <th style="background-color: blue">Description</th>
                        <th style="background-color: blue">Download</th>
                        
                    </tr>
                    <tr>
                        <%
                            try {
                                Connection con = Database.getConnection();
                                Statement st = con.createStatement();
                                ResultSet rs = st.executeQuery("select * from StudentCertificate");
                                while (rs.next()) {%>
                        <!-- <td><%=rs.getString("rollno")%></td>
                        <td style="color:white;"><%=rs.getString("name")%></td>
                        <td style="color:white;"><%=rs.getString("emailid")%></td>
                        <td style="color:white;"><%=rs.getString("UserType")%></td> -->
                        <td style="color:white;"><%=rs.getString("cName")%></td>
                        <td style="color:white;"><%=rs.getString("DEscription")%></td>
                        <!--
                        <td style="color:white;"><%=rs.getString("Status")%></td>
                       
                        -->
                    <td> <a href="downloadCER.jsp?rollno=<%=rs.getString("rollno")%>" style="width:60px;height:45px;">Download</a></td> 
                    </tr>
                    <% }
                        } catch (Exception e) {
                            e.printStackTrace();
                            System.out.println("leave details Page" + e.getMessage());
                        }
                    %>
                </table>
            </div>
        </div> <!-- /container -->
        <div>
            <p style="margin-left: 550px;color: red">&nbsp;<a href="" style="text-decoration: none;color: red"></a></p>
        </div>
    </body>
</html>