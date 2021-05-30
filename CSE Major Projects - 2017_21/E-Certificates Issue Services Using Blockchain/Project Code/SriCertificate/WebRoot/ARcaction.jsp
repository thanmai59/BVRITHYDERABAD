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
<%@ page import="action.Block"%>
<%@ page import="java.util.*"%>
<%@page import="action.Cloud"%>
<%@page import="java.io.FileWriter"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>


<% 


   ArrayList<Block> blockchain = new ArrayList<Block>();

try {

String[] initialValues = {"Block"};
Block blockb = new Block(initialValues, 19998988);
blockchain.add(blockb);
System.out.println("Block is" + blockchain.toString());
//System.out.println("arraylist " + blockchain);

String rollno=request.getParameter("rollno");
System.out.println("rollno"+rollno);
 //String lname =request.getParameter("lname");
//System.out.println("+++++++++++++++++"+lname);
 //String Description =request.getParameter("Description");
 //System.out.println("+++++++++++++++++"+Description);


String keyWord = "5765586965748666502846";

			keyWord = keyWord.substring(0, 16);
			byte[] keyValue = keyWord.getBytes();
			Key key = new SecretKeySpec(keyValue, "AES");
			Cipher c = Cipher.getInstance("AES");
			c.init(Cipher.ENCRYPT_MODE, key);
			 rollno = new String(Base64.encode(rollno.getBytes()));
			//  lname = new String(Base64.encode(lname.getBytes()));
   //Description = new String(Base64.encode(Description.getBytes()));

    System.out.println("After Encrypt : " + rollno );

    


 String filedata =request.getParameter("fname");
   System.out.println("+++++++++++++++++"+filedata);
MessageDigest md = MessageDigest.getInstance("SHA1");
		System.out.println("===**************=>"+md.digest());
		BigInteger bi1 = new BigInteger(md.digest());
		Random rr = new Random();
	  String str = String.valueOf(rr.nextInt(10)) + String.valueOf(rr.nextInt(10));
System.out.println("==>"+str);
		String spl1 = bi1.toString();
		String hash = bi1.toString(16);
		System.out.println("====>"+hash);
  String hkey=hash+str;
  System.out.println("====>"+hkey);
       Connection cn = Database.getConnection();
 PreparedStatement pstmt = cn.prepareStatement("INSERT INTO  CERTIFICATE VALUES(?,?,?)");
 
 
 String f=request.getParameter("fname");
String path="E:\\sriproj\\SriCertiFicate\\WebRoot\\file\\";
String fil=path+f;

File file = new File(fil);
 FileInputStream fis=new FileInputStream(file);
  FileWriter fw = new FileWriter(file);
  fw.write(f);
  fw.close();
pstmt.setString(1,rollno);
 //pstmt.setString(2,lname);
 //pstmt.setString(3,Description);
 new Cloud().upload(file, f);
 pstmt.setBinaryStream(2,(InputStream)fis,(int)(file.length()));
out.println("Generated hash Value is"+hash);
 pstmt.setString(3,hkey);
int l=pstmt.executeUpdate();
System.out.println("Generated hash Value is"+hkey);
   response.sendRedirect("adviewdetails.jsp");
 
 
 
 //response.sendRedirect("hhome.jsp");

} catch (Exception e) {
out.println("some technical problem");
} 

%> 