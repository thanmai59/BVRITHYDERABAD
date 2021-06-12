<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.PreparedStatement"%>
<%@page import="java.sql.Connection"%>
<%@page import="action.Database"%>
<%@page import="java.io.File"%>
<%@page import="java.io.InputStream"%>
<%@page import="java.io.FileInputStream"%>
 <% 
 try {
                            Connection cn = Database.getConnection();
                            PreparedStatement ps = cn.prepareStatement("insert into Studentrecletter(rollno, name,emailid, usertype,cname, Description,status, lname)values(?,?,?,?,?,?,?,?)");
                            ps.setString(1,request.getParameter("rollno"));
                            ps.setString(2,request.getParameter("name"));
                            ps.setString(3, request.getParameter("email"));
                            ps.setString(4,request.getParameter("utype"));
                            ps.setString(5,request.getParameter("cname"));
                            ps.setString(6,request.getParameter("Description"));
                            ps.setString(7,"No");
                            
 String f=request.getParameter("fname");
String path="E:\\sriproj\\SriCertiFicate\\WebRoot\\file\\";
String fil=path+f;

File file = new File(fil);
 FileInputStream fis=new FileInputStream(file);
 ps.setBinaryStream(8,(InputStream)fis,(int)(file.length()));
                            
                         
                            int i = ps.executeUpdate();
                            if (i == 1) {
                                response.sendRedirect("studentrec.jsp?msg=StudentAppliedRecletter Successfully");
                            } else {
                                response.sendRedirect("studentrec.jsp?msgg=StudentAppliedRecletter Failed");
                            }
                            cn.close();

                        } catch (Exception e) {
                            System.out.println(e.toString());
                        }
                        %>