<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<%@ include file="connect.jsp" %>
    <%@page import ="java.util.*,java.text.SimpleDateFormat,java.util.Date,java.io.FileInputStream,java.io.FileOutputStream,java.io.PrintStream"%>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Attacker</title>
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
	font-size: 24px;
	color: #FF0000;
}
-->
</style>
</head>
<body>
<div class="main">
  <div class="header">
    <div class="header_resize">
      <div class="logo">
        <h1><a href="index.html" class="style1">A Secure Searchable Encryption Framework for Privacy Critical Cloud Storage Services
</span></a></h1>
      </div>
      <div class="searchform">
        <form id="formsearch" name="formsearch" method="post" action="#">
          <span>
          <input name="editbox_search" class="editbox_search" id="editbox_search" maxlength="80" value="Search our ste:" type="text" />
          </span>
          <input name="button_search" src="images/search.gif" class="button_search" type="image" />
        </form>
      </div>
      <div class="clr"></div>
      <div class="slider">
        <div id="coin-slider"> <a href="#"><img src="images/slide1.jpg" width="960" height="360" alt="" /></a> <a href="#"><img src="images/slide2.jpg" width="960" height="360" alt="" /></a> <a href="#"><img src="images/slide3.jpg" width="960" height="360" alt="" /></a> </div>
        <div class="clr"></div>
      </div>
      <div class="clr"></div>
      <div class="menu_nav">
        <ul>
           
          
        </ul>
      </div>
      <div class="clr"></div>
    </div>
  </div>
  <div class="content">
    <div class="content_resize">
      <div class="mainbar">
        <div class="article">
        
          <div class="mainbar">
            <div class="article">
            <p>&nbsp;</p>
              <h2>Attack Cloud Files</h2>
              			  <br />
						  <form name="form1" method="post" action="attack33.jsp">
              
<%

	
	String s1="",s2="",s3="",s4="",s5="",s6="",s7="",s8,s9="",s10,s11,s12,s13;
	int i=0,j=0,k=0;

      	try 
	{
        
           String cname=request.getParameter("t1");  
		    String fname=request.getParameter("t2");      
		    String oname=request.getParameter("t3");  
           String uname=(String)application.getAttribute("uname");
      		 
      		
      		String query="select * from cfiles where cname='"+cname+"' and fname='"+fname+"' and oname='"+oname+"' "; 
           Statement st=connection.createStatement();
           ResultSet rs=st.executeQuery(query);
	if ( rs.next() )
	   {
			s2=rs.getString("ct");
		
		%>

  <table width="548" border="1" align="center">
    <tr>
      <td><span class="style10"> Cloud Name:- </span></td>
      <td><input type="text" name="t1" value="<%= cname %>"  readonly></td>
    </tr>
    <tr>
      <td><span class="style10"> File Name:- </span></td>
      <td><input type="text" name="t2" value="<%= fname %>" readonly></td>
    </tr>
     <tr>
      <td><span class="style10"> Owner Name:- </span></td>
      <td><input type="text" name="t3" value="<%= oname %>" readonly></td>
    </tr>
    <tr>
      <td><span class="style10">Change the File Content:-</span></td>
      <td><textarea name="textarea" id="textarea"  cols="50" rows="20"><%= s2 %></textarea></td>
    </tr>
    
    <tr>
      <td><div align="right">
        <input type="submit" name="Submit" value="Attack">
      </div></td>
      <td><input type="reset" name="Submit2" value="Reset"></td>
    </tr>
  </table>

<%
	   
	  }
	  else
	  {
		  out.println("FILE NOT FOUND IN CLOUD");
			
			
			%><p><a href="attack11.jsp">Back</a></p>



		<%
	  }
           connection.close();
          }
         
          catch(Exception e)
          {
            out.println(e.getMessage());
          }
%>

</form>
            </div>
          </div>
        </div>
        <div class="article">
          <h2>&nbsp;</h2>
          <div class="clr"></div>
        </div>
      </div>
      <div class="sidebar">
        <div class="gadget">
          <h2 class="star"><span>Sidebar</span> Menu</h2>
          <div class="clr"></div>
          <ul class="sb_menu">
            
          </ul>
        </div>
      </div>
      <div class="clr"></div>
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
      <div class="clr"></div>
    </div>
  </div>
  <div class="footer">
    <div class="footer_resize">
      <p class="lf">&copy;.</p>
      <div style="clear:both;"></div>
    </div>
  </div>
</div>
<div align=center></div>
</body>
</html>
