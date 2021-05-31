<%@page import="project.ConnectionProvider" %>
<%@page import="java.sql.*"%>
<%@page import="java.io.FileInputStream"%>
<%@page import = "java.io.InputStream"%>
<%@page import="java.io.File"%>

<%
	String course = request.getParameter("course");
	String branch = request.getParameter("branch");
	String rollNo = request.getParameter("rollNo");
	String name = request.getParameter("name");
	String fatherName = request.getParameter("fatherName");
	String mobile = request.getParameter("mobile");

	try{

		Connection con = ConnectionProvider.getCon();
		System.out.println("Connection established......");

		Statement st = con.createStatement();
		st.executeUpdate("insert into student values('"+course+"', '"+branch+"', '"+rollNo+"', '"+name+"', '"+fatherName+"', '"+mobile+"')"); 
		
	    System.out.println("Record inserted......");
	    response.sendRedirect("adminHome.jsp");
	}catch (Exception e) {
        System.out.println(e);
    }
%>