<%@page import="java.sql.Statement"%>
<%@page import="action.Database"%>
<%@page import="java.sql.Connection"%>
<%
    String rollno = request.getParameter("rollno");
    System.out.println("rollno " + rollno);
    String name = request.getParameter("name");
    System.out.println("name " + name);
     String pass = request.getParameter("pass");
    System.out.println("Pass " + pass);
    String email = request.getParameter("email");
    System.out.println("Email " + email);
   String course = request.getParameter("course");
    System.out.println("course " + course);
    String loc = request.getParameter("loc");
    System.out.println("Loc " + loc);
    String cno = request.getParameter("cno");
    System.out.println("Cno " + cno);
    String cgpa = request.getParameter("cgpa");
    System.out.println("cgpa" + cgpa);
    String sques1 = request.getParameter("sques1");
    System.out.println("sques1 " + sques1);
    String sques2 = request.getParameter("sques2");
    System.out.println("sques2 " + sques2);
    
    Connection con = Database.getConnection();
    Statement st = con.createStatement();
    int i = st.executeUpdate("insert into Student (rollno,name,pass,email,course,location,contactno,cgpa,status,sques1,sques2) values('"+rollno+"','"+name+"','"+pass+"','"+email+"','"+course+"','"+loc+"','"+cno+"','"+cgpa+"','completed','"+sques1+"','"+sques2+"')");
    if(i!=0)
    {
        response.sendRedirect("reg.jsp?msg=Student Registration Successfully");
    }
    else
    {
        response.sendRedirect("reg.jsp?msg=Registration Failed");
    }
%>