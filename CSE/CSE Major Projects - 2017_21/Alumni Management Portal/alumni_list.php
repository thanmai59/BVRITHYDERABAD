<?php
include 'header.php';
$table_name = 'alumni';
if($_POST["action"]){
    $data["email"] = $_POST["email"];
    $data["password"] = $_POST["password"];
    $data["first_name"] = $_POST["first_name"];
    $data["last_name"] = $_POST["last_name"];
    $data["date_of_birth"] = $_POST["date_of_birth"];
    $data["address"] = $_POST["address"];
    $data["mobile_number"] = $_POST["mobile_number"];
    $data["yoj"] = $_POST["yoj"];
    $data["yog"] = $_POST["yog"];
    $data["present_status"] = $_POST["present_status"];
    $data["job_acquired"] = $_POST["job_acquired"];
    $data["company"] = $_POST["company"];
    $data["college"] = $_POST["college"];
    $data["course"] = $_POST["course"];
    $data["country"] = $_POST["country"];
    $data["job_location"] = $_POST["job_location"];
    $data["designation"] = $_POST["designation"];
    $data["field_or_technology"] = $_POST["field_or_technology"];
    $data["annual_salary"] = $_POST["annual_salary"];
    $data["higher_studies1"] = $_POST["higher_studies1"];
    $data["higher_studies2"] = $_POST["higher_studies2"];

    $data["other_higher_studies"] = $_POST["other_higher_studies"];
    $data["current_job"] = $_POST["current_job"];
    $data["current_company"] = $_POST["current_company"];
    $data["current_job_location"] = $_POST["current_job_location"];
    $data["current_designation"] = $_POST["current_designation"];
    $data["current_field_or_technology"] = $_POST["current_field_or_technology"];
    $data["current_annual_salary"] = $_POST["current_annual_salary"];
    if($_POST["action"]=='Add'){
        insert($table_name,$data);
        if(function_exists("redirect_to_same")){
            redirect_to_same();
        }
    } else if($_POST["action"]=='Add New' || $_POST["action"]=='Edit'){
    ?>
    <hr>
    <form method="POST" enctype="multipart/form-data">
        <h2 id="small_frm">Add New Here</h2>
        <input type="hidden" name="id">
        <table class="ui blue striped table collapsing">
        <tr>
            <td>Email</td>
            <td><input type="email" name="email" required="">
            </td>
        </tr>
        <tr>
            <td>Password</td>
            <td><input type="password" name="password" required=""> <i class="ui large eye icon slash"></i>
                <script type="text/javascript">
                    var x = $(".eye.icon");
                    x.on("click",function(){
                        if (x.hasClass("slash")) {
                            x.removeClass("slash");
                            x.parent().children("input").attr("type","text");
                        } else {
                            x.addClass("slash");
                            x.parent().children("input").attr("type","password");
                        }
                    });
                </script>
            </td>
        </tr>
        <tr>
            <td>First Name</td>
            <td><input type="text" name="first_name">
            </td>
        </tr>
        <tr>
            <td>Last Name</td>
            <td><input type="text" name="last_name">
            </td>
        </tr>
        <tr>
            <td>Date Of Birth</td>
            <td><input type="date" name="date_of_birth">
            </td>
        </tr>
        <tr>
            <td>Address</td>
            <td><input type="text" name="address">
            </td>
        </tr>
        <tr>
            <td>Mobile Number</td>
            <td><input type="text" name="mobile_number" maxlength="10">
            </td>
        </tr>
        <tr>
            <td>Year of Joining</td>
            <td><input type="number" name="yoj" maxlength="4" min="2012" max="2050" autocomplete="off">
            </td>
        </tr>
        <tr>
            <td>Year of Graduation</td>
            <td><input type="number" name="yog" maxlength="4" min="2012" max="2050" autocomplete="off">
            </td>
        </tr>
        <tr>
        <td>Placed through Campus</td>
        <td><select  name="job_acquired">
                <option value="Campus Placement">Yes</option>
                <option value="No">No</option>
            </select>
        </td>
        </tr>
        <tr class="campus_no">
            <td>Select One Option</td>
            <td><select name="present_status">
                <option value="Higher Studies">Higher Studies</option>
                <option value="Off Campus Job">Off Campus Job</option>
            </select>
            </td>
        </tr>
        <tr class="job">
            <td>Company</td>
            <td><input type="text" name="company">
            </td>
        </tr>
        <tr class="job">
            <td>Job Location</td>
            <td><input type="text" name="job_location">
            </td>
        </tr>
        <tr class="job">
            <td>Designation</td>
            <td><input type="text" name="designation">
            </td>
        </tr>
        <tr class="job">
            <td>Field Or Technology</td>
            <td><input type="text" name="field_or_technology">
            </td>
        </tr>
        <tr class="job">
            <td>Annual Salary Package</td>
            <td><input type="text" name="annual_salary">
            </td>
        </tr>
        <tr class="higher">
            <td>College</td>
            <td><input type="text" name="college">
            </td>
        </tr>
        <tr class="higher">
            <td>Course</td>
            <td><input type="text" name="course">
            </td>
        </tr>
        <tr class="higher">
            <td>Country</td>
            <td><input type="text" name="country">
            </td>
        </tr>
        <tr>
            <td>Other Higher Studies</td>
            <td>
                <select name="other_higher_studies">
                    <option value="Same as Above">Same as Above</option>
                    <option value="New">New</option>
                </select>
            </td>
        </tr>
        <tr class="other_higher">
            <td>Higher Studies 1</td>
            <td><input type="text" name="higher_studies1">
            </td>
        </tr>
        <tr class="other_higher">
            <td>Higher Studies 2</td>
            <td><input type="text" name="higher_studies2">
            </td>
        </tr>
        <tr>
            <td>Current Job Location</td>
            <td>
                <select name="current_job">
                    <option value="Same as Above">Same as Above</option>
                    <option value="New">New</option>
                </select>
            </td>
        </tr>
        <tr class="current_job">
            <td>Company</td>
            <td><input type="text" name="current_company">
            </td>
        </tr>
        <tr class="current_job">
            <td>Job Location</td>
            <td><input type="text" name="current_job_location">
            </td>
        </tr>
        <tr class="current_job">
            <td>Designation</td>
            <td><input type="text" name="current_designation">
            </td>
        </tr>
        <tr class="current_job">
            <td>Field Or Technology</td>
            <td><input type="text" name="current_field_or_technology">
            </td>
        </tr>
        <tr class="current_job">
            <td>Annual Salary Package</td>
            <td><input type="text" name="current_annual_salary">
            </td>
        </tr>
        
            <tr>
                <td></td>
                <td><input type="submit" name="action" value="Add" class="ui mini blue button"></td>
            </tr>
        </table>
        </form>
        <?php
    }
    if($_POST["action"]=='Edit'){
        $id = $_POST["id"];
        $row = get_row("SELECT * FROM $table_name WHERE id = $id",ARRAY_A);
        $data = $row;
        ?>
        <script type="text/javascript">
            $('input[name=action]').val('Save');
            $('input[name=id]').val('<?php echo $_POST["id"]; ?>');
            $('#small_frm').html('Edit Here');
        </script>
    <script type="text/javascript">
        $('input[name=email]').val('<?php echo $data["email"]; ?>');
        $('input[name=password]').val('<?php echo $data["password"]; ?>');
        $('input[name=first_name]').val('<?php echo $data["first_name"]; ?>');
        $('input[name=last_name]').val('<?php echo $data["last_name"]; ?>');
        $('input[name=date_of_birth]').val('<?php echo $data["date_of_birth"]; ?>');
        $('input[name=address]').val('<?php echo $data["address"]; ?>');
        $('input[name=mobile_number]').val('<?php echo $data["mobile_number"]; ?>');
        $('input[name=yoj]').val('<?php echo $data["yoj"]; ?>');
        $('input[name=yog]').val('<?php echo $data["yog"]; ?>');
        $('select[name=present_status]').val('<?php echo $data["present_status"]; ?>');
        $('select[name=job_acquired]').val('<?php echo $data["job_acquired"]; ?>');
        $('input[name=company]').val('<?php echo $data["company"]; ?>');
        $('input[name=college]').val('<?php echo $data["college"]; ?>');
        $('input[name=course]').val('<?php echo $data["course"]; ?>');
        $('input[name=country]').val('<?php echo $data["country"]; ?>');
        $('input[name=job_location]').val('<?php echo $data["job_location"]; ?>');
        $('input[name=designation]').val('<?php echo $data["designation"]; ?>');
        $('input[name=field_or_technology]').val('<?php echo $data["field_or_technology"]; ?>');

        $('input[name=annual_salary]').val('<?php echo $data["annual_salary"]; ?>');
        $('input[name=higher_studies1]').val('<?php echo $data["higher_studies1"]; ?>');
        $('input[name=higher_studies2]').val('<?php echo $data["higher_studies2"]; ?>');

        $('select[name=other_higher_studies]').val('<?php echo $data["other_higher_studies"]; ?>');
        $('select[name=current_job]').val('<?php echo $data["current_job"]; ?>');
        $('input[name=current_company]').val('<?php echo $data["current_company"]; ?>');
        $('input[name=current_job_location]').val('<?php echo $data["current_job_location"]; ?>');
        $('input[name=current_designation]').val('<?php echo $data["current_designation"]; ?>');
        $('input[name=current_field_or_technology]').val('<?php echo $data["current_field_or_technology"]; ?>');
        $('input[name=current_annual_salary]').val('<?php echo $data["current_annual_salary"]; ?>');

    </script>
    <script type="text/javascript">
        var j = $('select[name=job_acquired]');
        var k = $('select[name=present_status]');
        j.on('change',function(){
            if (j.val()=='Campus Placement') {
                $('.job').show();
                $('.campus_no').hide();
                $('.higher').hide();
            } else {
                $('.job').hide();
                $('.campus_no').show();
                $('.higher').hide();
            }
            k.val('');
        });
        k.on('change',function(){
            if (k.val()=='Higher Studies') {
                $('.job').hide();
                $('.higher').show();
            } else {
                $('.job').show();
                $('.higher').hide();
            }
        });
        if (j.val()=='Campus Placement') {
            $('.job').show();
            $('.campus_no').hide();
            $('.higher').hide();
        } else if (k.val()=='Off Campus Job') {
            $('.job').show();
            $('.higher').hide();
            $('.campus_no').show();
        } else if (k.val()=='Higher Studies') {
            $('.job').hide();
            $('.higher').show();
            $('.campus_no').show();
        }

        var l = $('select[name=other_higher_studies]');
        var m = $('select[name=current_job]');
        function runl(){
            if (l.val()=='New') {
                $('.other_higher').show();
            } else {
                $('.other_higher').hide();
            }
        }
        l.on('change',runl);
        runl();
        function runm(){
            if (m.val()=='New') {
                $('.current_job').show();
            } else {
                $('.current_job').hide();
            }
        }
        m.on('change',runm);
        runm();
    </script>
        <?php
    }
    if($_POST["action"]=='Save'){
        $id = $_POST["id"];
        update($table_name,$data,array('id' => $id));
        if(function_exists("redirect_to_same")){
            redirect_to_same();
        }
    }
    if($_POST["action"]=='Delete'){
        $id = $_POST["id"];
        delete($table_name,array('id' => $id));
        if(function_exists("redirect_to_same")){
            redirect_to_same();
        }
    }
} 
if(($_POST["action"]!='Edit') && $_POST["action"]!='Add New') {
    ?>
    <form method="POST"><input type="submit" name="action" value="Add New" class="ui green button"></form><br>
    <div style="overflow-x:auto">
    <table id="myTable" class="ui unstackable fixed striped table dataTable">
        <thead>
            <tr>
                <th>Personal Details</th>
                <th>Address</th>
                <th>Year</th>
                <th colspan="3">Details</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            <?php
            $rows = get_results("SELECT * FROM $table_name ORDER BY id DESC");
            foreach($rows as $row){
                echo '<tr row-id="'.$row->id.'">';
                echo '<td><b>Email:</b> '.$row->email.'
                <br><b>Password:</b> '.$row->password.'
                <br><b>First name:</b> '.$row->first_name.'
                <br><b>Last name:</b> '.$row->last_name.'</td>';
                echo '<td><b>Date of birth:</b> '.$row->date_of_birth.'
                <br><b>Mobile number:</b> '.$row->mobile_number.'
                <br><b>Address:</b> '.$row->address.'</td>';
                echo '<td>Joining: '.$row->yoj.'
                <br>Graduation: '.$row->yog.'</td>';
                if ($row->job_acquired=='Campus Placement') {
                    echo '<td><b>Job: </b>'.$row->job_acquired.'
                    <br><b>Company: </b>'.$row->company.'
                    <br><b>Job location: </b>'.$row->job_location.'
                    <br><b>Designation: </b>'.$row->designation.'
                    <br><b>Field/technology: </b>'.$row->field_or_technology.'
                    <br><b>Annual Salary: </b>'.$row->annual_salary.'</td>';
                } else if ($row->job_acquired=='No') {
                    if ($row->present_status=='Higher Studies'){
                        echo '<td>Higher Studies: 
                        <br>College: '.$row->college.'
                        <br>Course: '.$row->course.'
                        <br>Country: '.$row->country.'</td>';
                    } else if ($row->present_status=='Off Campus Job') {
                        echo '<td><b>Job:</b> '.$row->present_status.'
                        <br><b>Company:</b> '.$row->company.'
                        <br><b>Job location:</b> '.$row->job_location.'
                        <br><b>Designation:</b> '.$row->designation.'
                        <br><b>Field/technology:</b> '.$row->field_or_technology.'
                        <br><b>Annual Salary:</b> '.$row->annual_salary.'</td>';
                    }
                }
                if ($row->other_higher_studies=='New') {
                        echo '<td><b>Other Higher Studies</b>
                        <br>1: '.$row->higher_studies1.'
                        <br>2: '.$row->higher_studies2.'</td>';
                } else {
                    echo "<td></td>";
                }
                if ($row->current_job=='New') {
                        echo '<td><b>Current Job:</b>
                        <br><b>Company:</b> '.$row->current_company.'
                        <br><b>Job location:</b> '.$row->current_job_location.'
                        <br><b>Designation:</b> '.$row->current_designation.'
                        <br><b>Field/technology:</b> '.$row->current_field_or_technology.'
                        <br><b>Annual Salary:</b> '.$row->current_annual_salary.'</td>';
                } else {
                    echo "<td></td>";
                }
                
            ?>
            <td>
                <form method="post">
                <input type="hidden" name="id" value="<?php echo $row->id; ?>">
                <input type="submit" name="action" class="ui mini blue button" value="Edit">
                <input type="submit" name="action" class="ui mini red button" value="Delete">
                </form>
            </td>
            <?php
                echo '</tr>';
            }
            ?>
        </tbody>
    </table>
    </div>
    <?php
}