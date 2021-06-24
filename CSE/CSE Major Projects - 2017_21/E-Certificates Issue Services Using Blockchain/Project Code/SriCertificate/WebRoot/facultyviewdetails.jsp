<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.Connection"%>
<%@page import="action.Database"%>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>gallery</title>
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
                <ul class="nav nav-justified">
               <li class="active"><a href="sview.jsp">Home</a></li>
                  <li><a href="sdetails.jsp">Profile</a></li>
                    <li><a href="staffleave.jsp">AddLeave</a></li>
                    <li><a href="staffviewdetails.jsp">ViewLeaveDetails</a></li>
                 
                    <li><a href="index.jsp">Logout</a></li>
                </ul>
            </div><br />
            <div class="abstract" style="background: "><br><br>
                <center><h1 style="color: white;margin-top: -10px">Leave Details</h1></center>
                <br><table style="margin-left: 280px;margin-top: -20px">
                    <tr>
                        <th style="background-color: blue">LeaveFrom</th>
                        <th style="background-color: blue">LeaveTo</th>
                        <th style="background-color: blue">Emailid</th>
                        <th style="background-color: blue">UserType</th>
                        <th style="background-color: blue">LeaveName</th>
                      
                        <th style="background-color: blue">Description</th>
                        <th style="background-color: blue">Status</th>
                         <th style="background-color: blue">NumberOfDays</th>
                    </tr>
                    <tr>
                        <%
                            try {
                                Connection con = Database.getConnection();
                                Statement st = con.createStatement();
                                ResultSet rs = st.executeQuery("select * from StaffLeave");
                                while (rs.next()) {%>
                        <td><%=rs.getString("LeaveFrom")%></td>
                        <td><%=rs.getString("LeaveTo")%></td>
                        <td><%=rs.getString("emailid")%></td>
                        <td><%=rs.getString("UserType")%></td>
                        <td><%=rs.getString("LName")%></td>
                        <td><%=rs.getString("DEscription")%></td>
                        <td><%=rs.getString("Status")%></td>
                        <td><%=rs.getInt("Validity")%></td>
                                           <!--<td> <img src="view_re.jsp?id=<%=rs.getString("cname")%>" style="width:60px;height:45px;"></img></td> 
                    -->
                    </tr>
                    <% }
                        } catch (Exception e) {
                            e.printStackTrace();
                            System.out.println("Admin viewcrime details Page" + e.getMessage());
                        }
                    %>
                </table>
            </div>
        </div> <!-- /container -->
        <div>
            <p style="margin-left: 550px;color: red">Copyright © 2021&nbsp;<a href="" style="text-decoration: none;color: red"></a></p>
        </div>
    </body>
</html>