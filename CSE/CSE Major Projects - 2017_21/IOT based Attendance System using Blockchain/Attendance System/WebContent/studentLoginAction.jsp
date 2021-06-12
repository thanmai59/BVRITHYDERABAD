<%@page import="project.ConnectionProvider" %>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
pageEncoding="ISO-8859-1"%>
<%@page import="java.sql.*,java.util.*"%>
<%
String name=request.getParameter("name");
session.setAttribute("name",name);
String rollNo=request.getParameter("rollNo");
session.setAttribute("rollNo", rollNo);
Connection con = ConnectionProvider.getCon();
Statement st= con.createStatement();
ResultSet rs=st.executeQuery("select * from student where name='"+name+"' and rollNo='"+rollNo+"'");
try{
if(rs.next()){
if(rs.getString("rollNo").equals(rollNo)&&rs.getString("name").equals(name))
{
	response.sendRedirect("testHome.jsp");
}
}else{
	response.sendRedirect("errorStudentLogin.html");
}
}
catch (Exception e) {
e.printStackTrace();
}
%>