<%@ page import="java.sql.*"%>



<% 
Connection con = null;
PreparedStatement stmt2 = null;
String emailid=request.getParameter("id");
System.out.println("status"+emailid);

String fname=request.getParameter("fname");
System.out.println("status"+fname);
try {


Class.forName("com.mysql.jdbc.Driver");
con = DriverManager.getConnection("jdbc:mysql://localhost:3306/sricertificate","root","root");
 stmt2 = con.prepareStatement("Update studentcertificate set status=?  where emailid=?  ");
 stmt2.setString(1,"Yes");
 stmt2.setString(2,emailid);
 stmt2.setString(3,fname);
 int l=stmt2.executeUpdate();
 if(l!=0){
 response.sendRedirect("ahome.jsp");
 }
 else {
out.println("someproblem");
}
} catch (Exception e) {

} 

%> 