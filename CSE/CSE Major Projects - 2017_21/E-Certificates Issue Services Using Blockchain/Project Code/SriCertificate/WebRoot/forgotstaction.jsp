<%@page import="java.sql.Statement"%>
<%@page import="action.Database"%>
<%@page import="java.sql.Connection"%>
<%@page import="java.sql.PreparedStatement"%>
<%
   String pass = request.getParameter("pass");
    System.out.println("Pass " + pass);
    String email = request.getParameter("email");
    System.out.println("Email " + email);

    String sques1 = request.getParameter("sques1");
    System.out.println("sques1 " + sques1);
    String sques2 = request.getParameter("sques2");
    System.out.println("sques2 " + sques2);
    
    Connection con = Database.getConnection();
    PreparedStatement pst = con.prepareStatement("Update Student set pass=? where sques1=? and sques2=? , email=?");
    pst.setString(1,pass);
    pst.setString(2,sques1);
    pst.setString(3,sques2);
    pst.setString(4,email);
    int i = pst.executeUpdate();
    if(i!=0)
    {
        response.sendRedirect("forgotstu.jsp?msg= Student Password Updated");
    }
    else
    {
        response.sendRedirect("forgotstu.jsp?msg=Pasword Updation Failed");
    }
%>