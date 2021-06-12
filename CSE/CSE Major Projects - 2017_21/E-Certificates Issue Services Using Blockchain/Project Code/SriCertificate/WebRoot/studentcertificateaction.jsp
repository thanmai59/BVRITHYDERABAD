<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.PreparedStatement"%>
<%@page import="java.sql.Connection"%>
<%@page import="action.Database"%>
 <% 
 try {
                            Connection cn = Database.getConnection();
                            PreparedStatement ps = cn.prepareStatement("insert into StudentCertificate(rollno, name,emailid, usertype,cname, Description,status)values(?,?,?,?,?,?,?)");
                            ps.setString(1,request.getParameter("rollno"));
                            ps.setString(2,request.getParameter("name"));
                            ps.setString(3, request.getParameter("email"));
                            ps.setString(4,request.getParameter("utype"));
                            ps.setString(5,request.getParameter("cname"));
                            ps.setString(6,request.getParameter("Description"));
                            ps.setString(7,"No");
                         
                            int i = ps.executeUpdate();
                            if (i == 1) {
                                response.sendRedirect("studentcer.jsp?msg=StudentAppliedCertificate Successfully");
                            } else {
                                response.sendRedirect("studentcer.jsp?msgg=StudentAppliedCertificate Failed");
                            }
                            cn.close();

                        } catch (Exception e) {
                            System.out.println(e.toString());
                        }
                        %>