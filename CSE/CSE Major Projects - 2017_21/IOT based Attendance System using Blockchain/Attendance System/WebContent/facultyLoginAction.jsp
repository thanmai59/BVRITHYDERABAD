<%@page import="project.ConnectionProvider" %>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
pageEncoding="ISO-8859-1"%>
<%@page import="java.sql.*,java.util.*"%>
<%
String empId=request.getParameter("empId");
session.setAttribute("empId",empId);
String empName=request.getParameter("empName");
session.setAttribute("empName", empName);
Connection con = ConnectionProvider.getCon();
Statement st= con.createStatement();
ResultSet rs=st.executeQuery("select * from faculty where empName='"+empName+"' and empId='"+empId+"'");
try{
if(rs.next()){
if(rs.getString("empName").equals(empName)&&rs.getString("empId").equals(empId))
{
	response.sendRedirect("facultyHome.jsp");
}
}else{
	response.sendRedirect("errorFacultyLogin.html");
}
}
catch (Exception e) {
e.printStackTrace();
}
%>