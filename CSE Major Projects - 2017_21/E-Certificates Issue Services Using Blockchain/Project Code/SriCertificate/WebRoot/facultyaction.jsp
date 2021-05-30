<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.Connection"%>
<%@page import="action.Database"%>
<%
    String uname = null;
    String email = request.getParameter("uname");
    String pass = request.getParameter("pass");
    Connection con = Database.getConnection();
    Statement st = con.createStatement();
    ResultSet rs = st.executeQuery("select * from faculty where email='" + email + "'");
    if (rs.next()) {
        uname = rs.getString("name");
        if (rs.getString("email").equals(email) && (rs.getString("pass").equals(pass))) {
            session.setAttribute("n1", uname);
            System.out.println(uname);
            session.setAttribute("v", email);
            System.out.println(email);
            System.out.println("Success");
            response.sendRedirect("fview.jsp?msg=Login Successfully");
        } else {
            System.out.println("Failed");
            response.sendRedirect("flogin.jsp?msgg=Incorrect Username or Password");
        }
    } else {
        System.out.println("Not Enter");
        response.sendRedirect("flogin.jsp?err=User does not exist");
    }
%>