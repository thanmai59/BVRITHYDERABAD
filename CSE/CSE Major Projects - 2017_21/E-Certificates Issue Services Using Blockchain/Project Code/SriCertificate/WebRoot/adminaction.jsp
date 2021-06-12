<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.Connection"%>
<%@page import="action.Database"%>
<%
    String uname = "Admin";
    String email = request.getParameter("aname");
    String pass = request.getParameter("apass");
   if (email.equals("admin@gmail.com") && pass.equals("admin")) {
            session.setAttribute("n1", uname);
            System.out.println(uname);
            session.setAttribute("v", email);
            System.out.println(email);
            System.out.println("Success");
            response.sendRedirect("ahome.jsp?Login Successfully");
        } else {
            System.out.println("Failed");
            response.sendRedirect("alogin.jsp?Login Failed");
       
    } 
%>



















