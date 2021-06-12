<%@include file="header.html"%>
<!DOCTYPE html>
<html>
<title>Admin</title>
<body>
<img src="./images/vishnuLogo.png"  align="left"width="100" height="100">

  <div class="w3-bar w3-black">
    <button class="w3-bar-item w3-button tablink w3-red" onclick="openCity(event,'London')">Add New Student</button>
    <button class="w3-bar-item w3-button tablink" onclick="openCity(event,'Paris')">Add Faculty</button>
    <button class="w3-bar-item w3-button tablink" onclick="openCity(event,'Tokyo')">Student List</button>
     <button class="w3-bar-item w3-button tablink" onclick="openCity(event,'Tokyo1')">Student Time Records</button>
     <a href="index.html" class="w3-bar-item w3-button tablink">Logout</a>
  </div>
  
  <div id="London" class="w3-container w3-border city">
  <br>
   <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel="dns-prefetch" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css?family=Raleway:300,400,600" rel="stylesheet" type="text/css">
    <link rel="icon" href="Favicon.png">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">

</head>
<body>
<main class="my-form">
    <div class="cotainer">
        <div class="row justify-content-center">
            <div class="col-md-8">
                    <div class="card">
                        <div class="card-header">Add New Students</div>
                        <div class="card-body">
                            <form name="my-form"  onsubmit="return validform()" action="addNewStudent.jsp" method="post">
                                <div class="form-group row">
                                    <label for="full_name" class="col-md-4 col-form-label text-md-right">Course Name</label>
                                    <div class="col-md-6">
                                        <input type="text"  class="form-control" name="course">
                                    </div>
                                </div>

                                <div class="form-group row">
                                    <label for="email_address" class="col-md-4 col-form-label text-md-right">Branch Name</label>
                                    <div class="col-md-6">
                                        <input type="text"  class="form-control" name="branch">
                                    </div>
                                </div>

                                <div class="form-group row">
                                    <label for="user_name" class="col-md-4 col-form-label text-md-right">Roll Number</label>
                                    <div class="col-md-6">
                                        <input type="text" class="form-control" name="rollNo">
                                    </div>
                                </div>

                                <div class="form-group row">
                                    <label for="phone_number" class="col-md-4 col-form-label text-md-right">Name</label>
                                    <div class="col-md-6">
                                        <input type="text"  class="form-control" name="name">
                                    </div>
                                </div>

                                <div class="form-group row">
                                    <label for="present_address" class="col-md-4 col-form-label text-md-right">Father Name</label>
                                    <div class="col-md-6">
                                        <input type="text"  class="form-control" name="fatherName">
                                    </div>
                                </div>

                                <div class="form-group row">
                                    <label for="permanent_address" class="col-md-4 col-form-label text-md-right">Mobile</label>
                                    <div class="col-md-6">
                                        <input type="text" class="form-control" name="mobile">
                                    </div>
                                </div>
                                


                                    <div class="col-md-6 offset-md-4">
                                        <button type="submit" class="btn btn-primary">
                                        Save
                                        </button>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
            </div>
        </div>
    </div>
</main>

<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
</body>
  </div>

  <div id="Paris" class="w3-container w3-border city" style="display:none">
  <br>
  <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<!------ Include the above in your HEAD tag ---------->

<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Fonts -->
    <link rel="dns-prefetch" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css?family=Raleway:300,400,600" rel="stylesheet" type="text/css">



    <link rel="icon" href="Favicon.png">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">

</head>
<body>



<main class="my-form">
    <div class="cotainer">
        <div class="row justify-content-center">
            <div class="col-md-8">
                    <div class="card">
                        <div class="card-header">Add Faculty</div>
                        <div class="card-body">
                            <form name="my-form" onsubmit="return validform()" action="addFaculty.jsp" method="post">
                                <div class="form-group row">
                                    <label for="full_name" class="col-md-4 col-form-label text-md-right">Employee Id</label>
                                    <div class="col-md-6">
                                        <input type="text"class="form-control" name="empId">
                                    </div>
                                </div>

                                <div class="form-group row">
                                    <label for="email_address" class="col-md-4 col-form-label text-md-right">Name</label>
                                    <div class="col-md-6">
                                        <input type="text"  class="form-control" name="empName">
                                    </div>
                                </div>

                                <div class="form-group row">
                                    <label for="user_name" class="col-md-4 col-form-label text-md-right">Department</label>
                                    <div class="col-md-6">
                                        <input type="text"  class="form-control" name="department">
                                    </div>
                                </div>

                                <div class="form-group row">
                                    <label for="phone_number" class="col-md-4 col-form-label text-md-right">Mobile</label>
                                    <div class="col-md-6">
                                        <input type="text"  class="form-control" name="mobile">
                                    </div>
                                </div>

                                <div class="form-group row">
                                    <label for="present_address" class="col-md-4 col-form-label text-md-right">Designation</label>
                                    <div class="col-md-6">
                                        <input type="text"  class="form-control" name="designation">
                                    </div>
                                </div>

                
                                    <div class="col-md-6 offset-md-4">
                                        <button type="submit" class="btn btn-primary">
                                       Save
                                        </button>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
            </div>
        </div>
        <br>
    </div>

</main>

<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
</body>
</html> 
  </div>

  <div id="Tokyo" class="w3-container w3-border city" style="display:none">
  
<section>
  <!--for demo wrap-->
  <div class="tbl-header">
    <table cellpadding="0" cellspacing="0" border="0">
      <thead>
        <tr>
         <th>Course Name</th>
          <th>Branch Name</th>
          <th>Roll Number</th>
          <th>Name</th>
          <th>Father Name</th>
          <th>Mobile</th>
        </tr>
      </thead>
    </table>
  </div>
  <div class="tbl-content">
    <table cellpadding="0" cellspacing="0" border="0">
      <tbody>
         <%@page import="project.ConnectionProvider" %>
<%@page import="java.sql.*"%>
<%
	try{
		Connection con = ConnectionProvider.getCon();
		Statement st = con.createStatement();
		ResultSet rst = st.executeQuery("select * from student");
		while(rst.next()){
			%>
    
        <tr>
          <td><%=rst.getString(1) %></td>
          <td><%=rst.getString(2) %></td>
          <td><%=rst.getString(3) %></td>
          <td><%=rst.getString(4) %></td>
          <td><%=rst.getString(5) %></td>
          <td><%=rst.getString(6) %></td>
        </tr>

      </tbody>
      <%}
		}catch(Exception e){}
		%>
    </table>
  </div>
</section>
</div>
<div id="Tokyo1" class="w3-container w3-border city" style="display:none">
   
<section>
  <!--for demo wrap-->
  <div class="tbl-header">
    <table cellpadding="0" cellspacing="0" border="0">
      <thead>
        <tr>
          <th>Roll Number</th>
          <th>Date</th>
          <th>Time</th>
        
          
        </tr>
      </thead>
    </table>
  </div>
  <div class="tbl-content">
    <table cellpadding="0" cellspacing="0" border="0">
      <tbody>
      <%@page import="project.ConnectionProvider" %>
<%@page import="java.sql.*"%>
<%
	try{
		Connection con = ConnectionProvider.getCon();
		Statement st = con.createStatement();
		ResultSet rst = st.executeQuery("select * from attendance");
		while(rst.next()){
			%>
        <tr>
           <td><%=rst.getString(1) %></td>
          <td><%=rst.getString(2) %></td>
          <td><%=rst.getString(3) %></td>
          
        </tr>
      </tbody>
      <%}}catch(Exception e){} %>
    </table>
  </div>
</section>


</body>
</html>