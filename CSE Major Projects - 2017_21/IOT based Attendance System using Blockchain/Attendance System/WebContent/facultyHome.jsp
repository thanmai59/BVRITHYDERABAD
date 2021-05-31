<%@include file="header.html"%>
<!DOCTYPE html>
<html>
<title>Faculty Home</title>
<body>
<img src="./images/vishnuLogo.png"  align="left"width="100" height="100">

  <div class="w3-bar w3-black">
    <button class="w3-bar-item w3-button tablink w3-red" onclick="openCity(event,'London')">View StudentReport</button>
    <button class="w3-bar-item w3-button tablink" onclick="openCity(event,'Tokyo')">Student List</button>
     <button class="w3-bar-item w3-button tablink" onclick="openCity(event,'Tokyo1')">View Attendance</button>
     <a href="logoutAction.jsp" class="w3-bar-item w3-button tablink">Logout</a>
  </div>
  
  <div id="London" class="w3-container w3-border city">
  <br>
   <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<!------ Include the above in your HEAD tag ---------->

<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Fonts -->
    <link rel="dns-prefetch" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css?family=Raleway:300,400,600" rel="stylesheet" type="text/css">



    <link rel="icon" href="Favicon.png">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
</head>
<body>
	<jsp:include page="reportFacultyPage.html"/>

  
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
</body>
</html> 
  </div>

  <div id="Tokyo" class="w3-container w3-border city" style="display:none">
  
<section>
  <!--for demo wrap-->
  <div class="tbl-header">
    <table cellpadding="0" cellspacing="0" border="0">
      <thead>
        <tr>
         <th>Course Name</th>
          <th>Branch Name</th>
          <th>Roll Number</th>
          <th>Name</th>
          <th>Father Name</th>
          <th>Mobile</th>
        </tr>
      </thead>
    </table>
  </div>
  <div class="tbl-content">
    <table cellpadding="0" cellspacing="0" border="0">
      <tbody>
         <%@page import="project.ConnectionProvider" %>
<%@page import="java.sql.*"%>
<%
	try{
		Connection con = ConnectionProvider.getCon();
		Statement st = con.createStatement();
		ResultSet rst = st.executeQuery("select * from student");
		while(rst.next()){
			%>
    
        <tr>
          <td><%=rst.getString(1) %></td>
          <td><%=rst.getString(2) %></td>
          <td><%=rst.getString(3) %></td>
          <td><%=rst.getString(4) %></td>
          <td><%=rst.getString(5) %></td>
          <td><%=rst.getString(6) %></td>
        </tr>

      </tbody>
      <%}
		}catch(Exception e){}
		%>
    </table>
  </div>
</section>
</div>                  
                        
   
<div id="Tokyo1" class="w3-container w3-border city" style="display:none">
   
<section>
  <!--for demo wrap-->
  <div class="tbl-header">
    <table cellpadding="0" cellspacing="0" border="0">
      <thead>
        <tr>
          <th>Roll Number</th>
          <th>Date</th>
          <th>Time</th>
        
          
        </tr>
      </thead>
    </table>
  </div>
  <div class="tbl-content">
    <table cellpadding="0" cellspacing="0" border="0">
      <tbody>
      <%@page import="project.ConnectionProvider" %>
<%@page import="java.sql.*"%>
<%
	try{
		Connection con = ConnectionProvider.getCon();
		Statement st = con.createStatement();
		ResultSet rst = st.executeQuery("select * from attendance");
		while(rst.next()){
			%>
        <tr>
           <td><%=rst.getString(1) %></td>
          <td><%=rst.getString(2) %></td>
          <td><%=rst.getString(3) %></td>
          
        </tr>
      </tbody>
      <%}}catch(Exception e){} %>
    </table>
  </div>
</section>


</body>
</html>