

<% session.removeAttribute("name");
session.removeAttribute("rollNo");
session.removeAttribute("empId");
session.removeAttribute("empName");
session.invalidate();

response.sendRedirect("index.html");
%>