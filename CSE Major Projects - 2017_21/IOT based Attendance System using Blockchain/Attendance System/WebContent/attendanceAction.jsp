<%@page import="project.ConnectionProvider" %>
<%@page import="com.blockchain.*" %>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
pageEncoding="ISO-8859-1"%>
<%@page import="java.sql.*,java.util.*"%>
<%
try{
	String rollNo = request.getParameter("rollNo");
	Connection con = ConnectionProvider.getCon();
	java.util.Date date=new java.util.Date();
	java.sql.Date sqlDate=new java.sql.Date(date.getTime());
	java.sql.Timestamp sqlTime=new java.sql.Timestamp(date.getTime());
	PreparedStatement ps=con.prepareStatement("insert into attendance (rollNo,day,record) values(?,?,?)");
	ps.setString(1, rollNo);
	ps.setDate(2,sqlDate);
	ps.setTimestamp(3,sqlTime);
	ps.executeUpdate();
	System.out.println("Attendance recorded..");
	
	String res = rollNo + " : " + sqlDate + " , " + sqlTime;
	
	//Blockchain.addBlock(new Block("Genesis", "0"));
	
	Blockchain.addBlock(new Block(res,Blockchain.chain.get(Blockchain.chain.size()-1).hash));
	System.out.println("\nThe blockchain: ");
	Blockchain.displayChain();
	
	response.sendRedirect("testHome.jsp");
}catch(Exception e){
	e.printStackTrace();
}
%>