<?php
include 'header.php';
$table_name = 'alumni';
if (isset($user_id) && $role=='alumni') {
    if ($_POST["action"]) {
        // save extra meta details
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
        update($table_name,$data,array("id"=>$user_id));
        redirect_to_same();
    }
$data = get_row("SELECT * FROM alumni WHERE id = $user_id",ARRAY_A);
?>
<div style="overflow-x:auto">
<form action="" method="post" id="main_form">
    <table class="ui blue celled table fixed collapsing unstackable sortable">
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
            <td><textarea name="address" rows="4"><?php echo $data["address"]; ?></textarea>
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
                    <option>Same as Above</option>
                    <option>New</option>
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
                    <option>Same as Above</option>
                    <option>New</option>
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
            <td><input type="submit" name="action" value="Save" class="ui mini blue button"></td>
        </tr>
    </table>
</form>
<style type="text/css">
.higher{
    display: none;
}
</style>
<?php
?>
<script type="text/javascript">
    $('input[name=email]').val('<?php echo $data["email"]; ?>');
    $('input[name=password]').val('<?php echo $data["password"]; ?>');
    $('input[name=first_name]').val('<?php echo $data["first_name"]; ?>');
    $('input[name=last_name]').val('<?php echo $data["last_name"]; ?>');
    $('input[name=date_of_birth]').val('<?php echo $data["date_of_birth"]; ?>');
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
</div>
    <?php
}