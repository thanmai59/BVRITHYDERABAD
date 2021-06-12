<%@page import="java.sql.Statement"%>
<%@page import="action.Database"%>
<%@page import="java.sql.Connection"%>
<%

    String name = request.getParameter("name");
    System.out.println("name " + name);
     String pass = request.getParameter("pass");
    System.out.println("Pass " + pass);
    String email = request.getParameter("email");
    System.out.println("Email " + email);
  
    String loc = request.getParameter("loc");
    System.out.println("Loc " + loc);
    String cno = request.getParameter("cno");
    System.out.println("Cno " + cno);

    String sques1 = request.getParameter("sques1");
    System.out.println("sques1 " + sques1);
    String sques2 = request.getParameter("sques2");
    System.out.println("sques2 " + sques2);
    
    Connection con = Database.getConnection();
    Statement st = con.createStatement();
    int i = st.executeUpdate("insert into Faculty (name,pass,email,location,contactno,sques1,sques2) values('"+name+"','"+pass+"','"+email+"','"+loc+"','"+cno+"','"+sques1+"','"+sques2+"')");
    if(i!=0)
    {
        response.sendRedirect("facultyreg.jsp?msg=Faculty Registration Successfully");
    }
    else
    {
        response.sendRedirect("facultyreg.jsp?msg=Registration Failed");
    }
%>