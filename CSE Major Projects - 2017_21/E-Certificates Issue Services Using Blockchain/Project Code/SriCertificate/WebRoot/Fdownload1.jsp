<%@ page import="java.sql.*, java.util.HashSet, java.util.ArrayList, java.util.Iterator, java.io.*"%>
<%@page import="action.Database"%>
<html>
<head>
<title></title>
<script language="JavaScript">

</script>
</head>

<body>
<%
Thread.sleep(2000);
%>		

<%

//System.out.println("id is "+id);    
  //String query = "select fname from SAMPLELetter where lname=?";
  	String sno = request.getParameter("sno");
  	System.out.println("sno " + sno);
    String query = "select lname from Studentrecletter where sno=?";
    Connection con = Database.getConnection();
  PreparedStatement pstmt=con.prepareStatement(query);
  pstmt.setString(1,sno);
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
 while (rs.next()){
  response.reset();
  response.setContentType("application/msword");
  response.addHeader("Content-Disposition","attachment; filename="+"sample.docx");
  // create the byte array from Blob
  Blob blb = rs.getBlob("lname");
  byte[] bdata = blb.getBytes(1, (int) blb.length());
  
  // get the response Output stream object to write the content of the file into header
  OutputStream output =  response.getOutputStream();
  output.write(bdata);
  output.close();
  // close the obejct of ResultSet
  rs.close();
  
  // close the connection object.. 
  con.close(); 
  }
  //else{}
%>
response.sendRedirect("fview.jsp");
</body>
</html>