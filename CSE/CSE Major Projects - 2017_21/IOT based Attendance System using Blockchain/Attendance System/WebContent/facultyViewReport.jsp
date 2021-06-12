<%@page import="project.ConnectionProvider" %>
<%@page import="java.sql.*" %>

<%
try{
	String rollNo = request.getParameter("rollNo");
	Connection con = ConnectionProvider.getCon();
	Statement st = con.createStatement();
	ResultSet rst = st.executeQuery("select * from student where student.rollNo='"+rollNo+"'");
	if(rst.next())
	{
%>


<title><%=rst.getString(4)%> Report</title>
<body>
<img src="./images/vishnuLogo.png"  align="left"width="100" height="100">


    
  <hr class="new1">
<style>
table{
  width:100%;
  table-layout: fixed;
}
th{
  padding: 20px 15px;
  text-align: left;
  font-weight: 500;
  font-size: 12px;
  color: #fff;
  text-transform: uppercase;
 border: 2px solid rgba(255,255,255,0.3);
}


/* demo styles */

@import url(https://fonts.googleapis.com/css?family=Roboto:400,500,300,700);
body{
  background: -webkit-linear-gradient(left, #c938fa, #2dd2d2);
  background: linear-gradient(to right, #c938fa, #2dd2d2);
  font-family: 'Roboto', sans-serif;
}

</style>
  <!--for demo wrap-->
  <div class="tbl-header">
    <table cellpadding="0" cellspacing="0" border="0">
      <thead>
        <tr>
          <th>institution Name: BVRITH</th>
          <th>Course Name: <%=rst.getString(1) %></th>
          <th>Branch Name: <%=rst.getString(2) %></th>
          <th><center>RollNo: <%=rst.getString(3) %></center></th>
        </tr>
      </thead>
      <thead>
        <tr>
          <th>Name: <%=rst.getString(4) %></th>
          <th>Father Name:<%=rst.getString(5) %></th>
          <th>Mobile:<%=rst.getString(6) %></th>
          <th><a titlt="print screen" alt="print screen" onclick="window.print();" target="_blank" style="cursor:pointer;"><center><img src="./images/print.png"></center></a></th>
        </tr>
      </thead>
    </table>
  </div>
<style>
html {
  font-family:arial;
  font-size: 25px;
}

td {
  border: 2px solid #726E6D;
  padding: 15px;
  color:black;
  text-align:center;
}

thead{
  font-weight:bold;
  text-align:center;
  background: #625D5D;
  color:white;
}

table {
  border-collapse: collapse;
}

.footer {
  text-align:right;
  font-weight:bold;
}

tbody >tr:nth-child(odd) {
  background: #D1D0CE;
}

</style>
<head>
  <hr class="new1">
</head>
<body>
  <table>
  <%
	} else{
		response.sendRedirect("errorDgiOneView.html");
	}
	ResultSet rst1 = st.executeQuery("SELECT COUNT(*), rollNo FROM attendance where attendance.rollNo='"+rollNo+"'");
	if(rst1.next()){
		
	
  %>
    <thead>
      <tr>
        
        <td rowspan="2">Total Held</td>
        <td rowspan="2">Classes Attended</td>
        <td rowspan="2">Percentage</td>
        
      </tr>
     
    </thead>
    <tbody>
      <tr>
        
        
        <td>35</td>
        <td><%=rst1.getString(1) %></td>
        <td><%int res = Integer.parseInt(rst1.getString(1)); out.println((res*100)/10); %></td>
      </tr>  
    </tbody>
    
  </table>
  
  <br/>
  <br/>
  
   <a href="facultyHome.jsp">Back</a> 
</body>

<%
	}else{
		response.sendRedirect("errorDgiOneView.html");
	}
	} catch(Exception e){}

%>