<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<%@ include file="connect.jsp" %>
    <%@page import ="java.util.*,java.text.SimpleDateFormat,java.util.Date,java.io.FileInputStream,java.io.FileOutputStream,java.io.PrintStream"%>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Send Trust</title>
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
.style1 {
	color: #0000FF;
	padding: 0;
	margin: 0;
	width: 100%;
	line-height: 0;
	clear: both;
}
.style4 {font-size: 24}
.style5 {padding:0; margin:0; width:100%; line-height:0; clear: both;}
.style6 {font-weight: bold; color: #FF00FF;}
.style8 {font-size: 24px}
-->
</style>
</head>
<body>
<div class="main style4">
  <div class="header">
    <div class="header_resize">
      <div class="logo style8">
         <h1><a href="index.html" class="style1"></a></h1>
      </div>
      <div class="searchform">
        <form id="formsearch" name="formsearch" method="post" action="#">
          
          <input name="editbox_search" class="editbox_search" id="editbox_search" maxlength="80" value="Search our ste:" type="text" />
          
          <input name="button_search" src="images/search.gif" class="button_search" type="image" />
        </form>
      </div>
      <div class="style5"></div>
      <div class="slider">
        <div id="coin-slider"> <a href="#"><img src="images/slide1.jpg" width="960" height="360" alt="" /></a> <a href="#"><img src="images/slide2.jpg" width="960" height="360" alt="" /></a> <a href="#"><img src="images/slide3.jpg" width="960" height="360" alt="" /></a> </div>
        <div class="style5"></div>
      </div>
      <div class="style5"></div>
      <div class="menu_nav">
        <ul>
          <li class="active"><a href="user_main.jsp">Home Page</a></li>
          <li  class="active"><a href="purchase.jsp">Purchase VM</a></li>
          <li class="active"><a href="sendfile.jsp">Upload File</a></li>
          <li class="active"><a href="Verify.jsp">Verify</a></li>
          <li class="active"><a href="index.html">Logout</a></li>
        </ul>
      </div>
      <div class="style5"></div>
    </div>
  </div>
  <div class="content">
    <div class="content_resize">
      <div class="mainbar">
        <div class="article">
        
          <div class="mainbar">
            <div class="article">
            <p>&nbsp;</p>
              <h2>Send Feedback to Cloud </h2>
              <p>&nbsp;</p>
              <br />
              <form action="SendTrust1.jsp" method="post"  name="form1">
  <table width="598" border="1" align="center">
    <tr>
      <td width="286"><strong>Select the Cloud:-  </strong></td>
      <td width="356"> <select name="select5">
            <option >--Select--</option>
           <option>CS1</option>
		    <option>CS2</option>
			<option>CS3</option>
			<option>CS4</option>
          </select>     </td>
    </tr>
    
    
    <tr>
      <td><strong>Enter Your Feedback:-</strong></td>
      <td><textarea name="t1"></textarea></td>
    </tr>
   
      
    <tr>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><div align="right">
        <input type="submit" name="Submit" value="Submit">
      </div></td>
      <td><input type="reset" name="Submit2" value="Reset"></td>
    </tr>
  </table>
</form>
            </div>
          </div>
        </div>
        <div class="article">
          <h2>&nbsp;</h2>
          <div class="style5"></div>
        </div>
      </div>
      <div class="sidebar">
        <div class="gadget">
          <h2 class="star">Sidebar Menu</h2>
          <div class="style1"></div>
          <ul class="sb_menu  style6">
          <li><a href="viewcloudrepu.jsp">Find Reputation</a></li>
            <li><a href="viewcloudtrust.jsp">Find Trust Worthy</a></li>
            <li><a href="viewcloudcost.jsp">Find Cost & Memory</a></li>
            <li><a href="SendTrust.jsp">Send Trustworthiness of Cloud</a></li>
            <li><a href="Delete.jsp">Delete</a></li>
            <li><a href="viewcloudfiles.jsp">View Cloud Files</a></li>
          </ul>
        </div>
      </div>
      <div class="style5"></div>
    </div>
  </div>
  <div class="fbg">
    <div class="fbg_resize">
      <div class="col c1">
        <h2>&nbsp;</h2>
        </div>
      <div class="col c2">
        <h2>&nbsp;</h2>
      </div>
      <div class="col c3">
        <h2>&nbsp;</h2>
      </div>
      <div class="style5"></div>
    </div>
  </div>
  <div class="footer">
    <div class="footer_resize">
      <div style="clear:both;"></div>
    </div>
  </div>
</div>
<div align=center></div>
</body>
</html>
