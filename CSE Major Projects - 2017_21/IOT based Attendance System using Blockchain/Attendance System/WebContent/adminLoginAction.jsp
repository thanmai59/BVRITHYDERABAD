<% 
String userId = request.getParameter("username");
String pwd = request.getParameter("password");

if(userId.equalsIgnoreCase("admin") && pwd.equalsIgnoreCase("admin")){
	response.sendRedirect("adminHome.jsp");
} else {
	response.sendRedirect("errorAdminLogin.html");
}

%>