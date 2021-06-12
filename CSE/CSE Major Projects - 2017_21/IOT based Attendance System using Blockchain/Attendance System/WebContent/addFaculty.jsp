<%@page import="project.ConnectionProvider" %>
<%@page import="java.sql.*"%>
<%@page import="java.io.FileInputStream"%>
<%@page import = "java.io.InputStream"%>
<%@page import="java.io.File"%>

<%
	String empId = request.getParameter("empId");
	String empName = request.getParameter("empName");
	String department = request.getParameter("department");
	String mobile = request.getParameter("mobile");
	String designation = request.getParameter("designation");

	try{
		 
         
		Connection con = ConnectionProvider.getCon();
		System.out.println("Connection established......");

		Statement st = con.createStatement();
		st.executeUpdate("insert into faculty values('"+empId+"', '"+empName+"', '"+department+"', '"+mobile+"', '"+designation+"')"); 
		
	    System.out.println("Record inserted......");
	    response.sendRedirect("adminHome.jsp");
	}catch (Exception e) {
        System.out.println(e);
    }
%>