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
            <div style="width: 1200px;margin: 30px;color: white">
                <center><h1>E-Certificates Issue Services Using BlockChain</h1></center>
            </div>
            <div>
                <ul class="nav nav-justified">-->
 <!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    
     
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
            <div class="abstract" style="background: ;margin-left:2%;"><br><br>
                <center><h1 style="color: white;margin-top: -10px">Recommendation Letter Details</h1></center><br/>
                <br><table style="margin-left: 4%;margin-top: -20px">
                  <tr>
                        <th style="background-color: blue">Rollno</th>
                        <th style="background-color: blue">Name</th>
                        <th style="background-color: blue">Emailid</th>
                        <!-- <th style="background-color: blue">UserType</th> -->
                        <th style="background-color: blue">LetterName</th>
                      	<th style="background-color: blue">Download sample</th>
                        <th style="background-color: blue">Description</th>
                        <!-- <th style="background-color: blue">Status</th> -->
                        
                    
                         <th style="background-color: blue">UploadLetter</th>
                    </tr>
                    <tr>
                        <%
                         String n = session.getAttribute("n1").toString();
                
                String s = session.getAttribute("v").toString();
                System.out.println("Name " + n+"   "+s);
                            try {
                                Connection con = Database.getConnection();
                                Statement st = con.createStatement();
                                ResultSet rs = st.executeQuery("select *from StudentRecLetter where usertype='"+n+"'");
                               // st.setString(1,n);
                                while (rs.next()) {%>
             			<td style="color:white;"><%=rs.getString("rollno")%></td>
                        <td style="color:white;"><%=rs.getString("name")%></td>
                        <td style="color:white;"><%=rs.getString("emailid")%></td>
                        <!-- <td><%=rs.getString("UserType")%></td> -->
                        <td style="color:white;"><%=rs.getString("cName")%></td>
                        <td style="color:white;"> <a href="Fdownload1.jsp?id=<%=rs.getString("DEscription")%>&sno=<%=rs.getString("sno")%>&emailid=<%=rs.getString("emailid")%>" style="width:60px;height:45px;">Download sample</a></td> 
                        <td style="color:white;"><%=rs.getString("DEscription")%></td>
                        <!-- <td><%=rs.getString("Status")%></td> -->
                        <!--
                        <td> <a href="FLetteraccept.jsp?id=<%=rs.getString("emailid")%>&rollno=<%=rs.getString("rollno")%>&fname=<%=rs.getString("Usertype")%>" style="width:60px;height:45px;">AcceptLetter</a></td> 
                    
                     -->
                     <td style="color:white;"> <a href="FRupload.jsp?id=<%=rs.getString("DEscription")%>&rollno=<%=rs.getString("rollno")%>&fname=<%=rs.getString("cName")%>" style="width:60px;height:45px;">Upload</a></td> 
                   
                    </tr>
                    <% }
                        } catch (Exception e) {
                            e.printStackTrace();
                            System.out.println("student details Page" + e.getMessage());
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