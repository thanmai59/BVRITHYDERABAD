<%@ page import="java.sql.*"%>
<%@page import="java.text.DateFormat"%>
<%@page import="java.util.*"%>
<%@page import="java.text.SimpleDateFormat"%>
<%@page import="java.util.Calendar" %>
<%@page import="action.Database"%>
<%@page import="java.io.InputStream"%>
<%@page import="java.io.FileInputStream"%>
<%@page import="java.io.File"%>
<%@page import="java.security.MessageDigest"%>
<%@page import="java.math.BigInteger"%>
<%@page import="java.security.Key"%>
<%@page import="javax.crypto.spec.SecretKeySpec"%>
<%@page import="javax.crypto.Cipher"%>
<%@page import="org.bouncycastle.util.encoders.Base64"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>


<% 


   

try {


 String lname =request.getParameter("lname");
System.out.println("+++++++++++++++++"+lname);
//String filedata =request.getParameter("fname");
 //System.out.println("+++++++++++++++++"+filedata);

  Connection cn = Database.getConnection();
 PreparedStatement pstmt = cn.prepareStatement("INSERT INTO  SAMPLELetter VALUES(?,?)");
 String f=request.getParameter("fname");
String path="E:\\sriproj\\SriCertiFicate\\WebRoot\\file\\";
String fil=path+f;

File file = new File(fil);
 FileInputStream fis=new FileInputStream(file);
 pstmt.setString(1,lname);
 pstmt.setBinaryStream(2,(InputStream)fis,(int)(file.length()));
int l=pstmt.executeUpdate();
response.sendRedirect("stuview.jsp");
 
 
 
 

} catch (Exception e) {
out.println("some technical problem");
} 

%> 