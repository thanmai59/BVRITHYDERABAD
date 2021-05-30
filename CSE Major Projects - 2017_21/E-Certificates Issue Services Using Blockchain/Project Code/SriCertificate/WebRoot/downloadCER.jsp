<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@page import="action.Database"%>
<%@page import="java.sql.Connection"%>
<%@page import="java.sql.PreparedStatement"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Blob"%>
<%@page import="java.io.OutputStream"%>
<%@page import="java.io.InputStream"%>
<%@page import="java.io.FileInputStream"%>
<%@page import="java.io.File"%>
<%@page import="java.security.MessageDigest"%>
<%@page import="java.math.BigInteger"%>
<%@page import="java.security.Key"%>
<%@page import="javax.crypto.spec.SecretKeySpec"%>
<%@page import="javax.crypto.Cipher"%>
<%@page import="org.bouncycastle.util.encoders.Base64"%>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title></title>
</head>
<body>


<%
//session.removeAttribute("resumeBlob");
//String id=(String)session.getAttribute("rollno");



String roll=request.getParameter("rollno").toString();
String keyWord = "5765586965748666502846";

			keyWord = keyWord.substring(0, 16);
			byte[] keyValue = keyWord.getBytes();
			Key key = new SecretKeySpec(keyValue, "AES");
			Cipher c = Cipher.getInstance("AES");
			c.init(Cipher.ENCRYPT_MODE, key);
			 roll = new String(Base64.encode(roll.getBytes()));
System.out.println("roll is "+roll);    
  String query = "select fname  from certificate where rollno=?";
  Connection con =Database.getConnection();
  PreparedStatement pstmt=con.prepareStatement(query);
  pstmt.setString(1,roll);
  ResultSet rs=pstmt.executeQuery();
 
  
  // clear the response header information.
                         
  // check the file type and set the header contentType accordingly..   
   /*if(rs.getString(2)==".txt")
  {
      response.setContentType("application/octet-stream");
  }
  else if(rs.getString(2)==".pdf")
  {
      response.setContentType("application/pdf");
  }
 else if((rs.getString(2)==".doc")||rs.getString(2)==".docx")
  {
      response.setContentType("application/msword");
  }
  else if((rs.getString(2)==".xls")||(rs.getString(2)==".xlsx"))
  {
      response.setContentType("application/vnd.ms-excel");
  }*/
  // add header information to response object
 if (rs.next()){
  response.reset();
  response.setContentType("application/pdf");
  response.addHeader("Content-Disposition","attachment; filename="+"123.pdf");
  // create the byte array from Blob
  Blob blb = rs.getBlob(1);
  byte[] bdata = blb.getBytes(1, (int) blb.length());
  
  // get the response Output stream object to write the content of the file into header
  OutputStream output =  response.getOutputStream();
  output.write(bdata);
  output.close();
  // close the obejct of ResultSet
  //rs.close();
  
  // close the connection object.. 
  //con.close(); 
  }
  else{response.sendRedirect("stuview.jsp");}
%>

</body>
</html>
</body>
</html>