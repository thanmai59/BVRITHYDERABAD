<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<%@page import ="java.util.*,java.security.Key,java.util.Random,javax.crypto.Cipher,javax.crypto.spec.SecretKeySpec,org.bouncycastle.util.encoders.Base64"%>
    <%@ page import="java.sql.*,java.util.Random,java.io.PrintStream,java.io.FileOutputStream,java.io.FileInputStream,java.security.DigestInputStream,java.math.BigInteger,java.security.MessageDigest,java.io.BufferedInputStream" %>
<%@ include file="connect.jsp" %>
<%@ page import="java.sql.*,java.util.Random,java.security.KeyPairGenerator,javax.crypto.Cipher,java.security.Key,java.security.KeyPair     "%>

    <%@page import ="java.util.*,java.text.SimpleDateFormat,java.util.Date,java.io.FileInputStream,java.io.FileOutputStream,java.io.PrintStream"%>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title></title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="css/style.css" rel="stylesheet" type="text/css" />
<link rel="stylesheet" type="text/css" href="css/coin-slider.css" />
<script type="text/javascript" src="js/cufon-yui.js"></script>
<script type="text/javascript" src="js/cufon-quicksand.js"></script>
<script type="text/javascript" src="js/jquery-1.4.2.min.js"></script>
<script type="text/javascript" src="js/script.js"></script>
<script type="text/javascript" src="js/coin-slider.min.js"></script>
<style type="text/css">
<!--
.style2 {font-size: 24}
.style3 {padding:0; margin:0; width:100%; line-height:0; clear: both;}
-->
</style>
</head>
<body>
<div class="main style2">
  <div class="header">
    <div class="header_resize">
      <div class="logo">
        <h1>&nbsp;</h1>
      </div>
      <div class="searchform">
        <form id="formsearch" name="formsearch" method="post" action="#">
          
          <input name="editbox_search" class="editbox_search" id="editbox_search" maxlength="80" value="Search our ste:" type="text" />
          
          <input name="button_search" src="images/search.gif" class="button_search" type="image" />
        </form>
      </div>
      <div class="style3"></div>
      <div class="slider">
        <div id="coin-slider"> <a href="#"><img src="images/slide1.jpg" width="960" height="360" alt="" /></a> <a href="#"><img src="images/slide2.jpg" width="960" height="360" alt="" /></a> <a href="#"><img src="images/slide3.jpg" width="960" height="360" alt="" /></a> </div>
        <div class="style3"></div>
      </div>
      <div class="style3"></div>
      <div class="menu_nav">
        <ul>
          <li class="active"><a href="user_main.jsp">Home Page</a></li>
          <li  class="active"><a href="purchase.jsp">Purchase VM</a></li>
          <li class="active"><a href="sendfile.jsp">Upload File</a></li>
          <li class="active"><a href="Verify.jsp">Verify</a></li>
          <li class="active"> <a href="index.html">Logout</a></li>
        </ul>
      </div>
      <div class="style3"></div>
    </div>
  </div>
  <div class="content">
    <div class="content_resize">
      <div class="mainbar">
        <div class="article">
        
          <div class="mainbar">
            <div class="article">
            <p>&nbsp;</p>
              <h2>Send Feedback to Cloud</h2>
              			  <br />
              <%
     
	     	String cname=request.getParameter("select5");
            String fname=request.getParameter("t1");
        
		
		try
		{
			SimpleDateFormat sdfDate = new SimpleDateFormat(
					"dd/MM/yyyy");
			SimpleDateFormat sdfTime = new SimpleDateFormat(
					"HH:mm:ss");

			Date now = new Date();

			String strDate = sdfDate.format(now);
			String strTime = sdfTime.format(now);
			String dt = strDate + "   " + strTime;
			
			Statement st=connection.createStatement();
			
			String uname=(String)application.getAttribute("uname");
			
			String query="select count(*) from feedback where oname='"+uname+"' and cname='"+cname+"' and dt='"+strDate+"' "; 
	           
	           ResultSet rs=st.executeQuery(query);
			
			if(rs.next())
			{
				int i=rs.getInt(1);
				
				if(i<=2)
				{
					st.executeUpdate(" insert into feedback (oname,cname,feedback,dt) values ('"+uname+"','"+cname+"','"+fname+"','"+strDate+"') ");
					st.executeUpdate(" insert into feedback1 (oname,cname,feedback,dt) values ('"+uname+"','"+cname+"','"+fname+"','"+strDate+"') ");
						out.println("FEEDBACK SENT SUCCESSFULLY");
					
					
					%><p><a href="SendTrust.jsp">Back</a></p>



				<%
				}
				if(i>2)
				{
					String ip_h = request.getRemoteAddr();  
					String host_h = request.getRemoteHost(); 
					
					st.executeUpdate(" insert into Attackers values ('"+uname+"','"+cname+"','Feedbacking about the Cloud','"+ip_h+"','"+host_h+"','"+dt+"') ");
					
					out.println("LIMIT FOR FEEDBACKING IS EXPIRED...!");
				
				
				%><p><a href="SendTrust.jsp">Back</a></p>



			<%
					
				}
				
			
			
			}
			else
			{
				st.executeUpdate(" insert into feedback (oname,cname,feedback,dt) values ('"+uname+"','"+cname+"','"+fname+"','"+strDate+"') ");
				st.executeUpdate(" insert into feedback1 (oname,cname,feedback,dt) values ('"+uname+"','"+cname+"','"+fname+"','"+strDate+"') ");
				out.println("FEEDBACK SENT SUCCESSFULLY");
			
			
			%><p><a href="SendTrust.jsp">Back</a></p>

		<%
			}

		 	}
	  
	catch(SQLException e)
        {
		out.print(e.getMessage());
	    }  
           %>
            </div>
          </div>
        </div>
        <div class="article">
          <h2>&nbsp;</h2>
          <div class="style3"></div>
        </div>
      </div>
      <div class="sidebar">
        <div class="gadget">
          <h2 class="star">Sidebar Menu</h2>
          <div class="style3"></div>
          <ul class="sb_menu">
           <li><a href="viewcloudrepu.jsp">Find Reputation</a></li>
            <li><a href="viewcloudtrust.jsp">Find Trust Worthy</a></li>
            <li><a href="viewcloudcost.jsp">Find Cost & Memory</a></li>
            <li><a href="SendTrust.jsp">Send Trustworthiness of Cloud</a></li>
            <li><a href="Delete.jsp">Delete</a></li>
            <li><a href="viewcloudfiles.jsp">View Cloud Files</a></li>
          </ul>
        </div>
      </div>
      <div class="style3"></div>
    </div>
  </div>
  <div class="fbg">
    <div class="fbg_resize">
      <div class="col c1">
        <h2>Image Gallery</h2>
        <a href="#"><img src="images/gal1.jpg" width="75" height="75" alt="" class="gal" /></a> <a href="#"><img src="images/gal2.jpg" width="75" height="75" alt="" class="gal" /></a> <a href="#"><img src="images/gal3.jpg" width="75" height="75" alt="" class="gal" /></a> <a href="#"><img src="images/gal4.jpg" width="75" height="75" alt="" class="gal" /></a> <a href="#"><img src="images/gal5.jpg" width="75" height="75" alt="" class="gal" /></a> <a href="#"><img src="images/gal6.jpg" width="75" height="75" alt="" class="gal" /></a> </div>
      <div class="col c2">
        <h2>Services Overview</h2>
        <p>Curabitur sed urna id nunc pulvinar semper. Nunc sit amet tortor sit amet lacus sagittis posuere cursus vitae nunc.Etiam venenatis, turpis at eleifend porta, nisl nulla bibendum justo.</p>
        <ul class="fbg_ul">
          <li><a href="#">Lorem ipsum dolor labore et dolore.</a></li>
          <li><a href="#">Excepteur officia deserunt.</a></li>
          <li><a href="#">Integer tellus ipsum tempor sed.</a></li>
        </ul>
      </div>
      <div class="col c3">
        <h2>Contact Us</h2>
        <p>Nullam quam lorem, tristique non vestibulum nec, consectetur in risus. Aliquam a quam vel leo gravida gravida eu porttitor dui.</p>
        <p class="contact_info"> Address: 1458 TemplateAccess, USA<br />
          Telephone: +123-1234-5678<br />
          FAX: +458-4578<br />
          Others: +301 - 0125 - 01258<br />
          E-mail: <a href="#">mail@yoursitename.com</a> </p>
      </div>
      <div class="style3"></div>
    </div>
  </div>
  <div class="footer">
    <div class="footer_resize">
      <p class="lf">&copy; Copyright <a href="#">MyWebSite</a>.</p>
      <p class="rf">Design by Dream <a href="http://www.dreamtemplate.com/">Web Templates</a></p>
      <div style="clear:both;"></div>
    </div>
  </div>
</div>
<div align=center>This template  downloaded form <a href='http://all-free-download.com/free-website-templates/'>free website templates</a></div>
</body>
</html>
