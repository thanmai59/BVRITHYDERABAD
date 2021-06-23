<?php
include 'header.php';
$table_name = 'job';
?>
<div style="overflow-x:auto">
<table id="myTable" class="ui unstackable celled table dataTable">
    <thead>
        <tr>
            <th>Job</th>
            <th>Company</th>
            <th>Location</th>
            <th>Salary</th>
            <th>Job Contact</th>
            <th>Link</th>
            <th>Alumni</th>
        </tr>
    </thead>
    <tbody>
        <?php
        $rows = get_results("SELECT * FROM $table_name ORDER BY id DESC");
        $alumni_opts = get_results("SELECT id,first_name,last_name FROM alumni",OBJECT_K);
        foreach($rows as $row){
            echo '<tr row-id="'.$row->id.'">';
            echo '<td>'.$row->job.'</td>';
            echo '<td>'.$row->company.'</td>';
            echo '<td>'.$row->location.'</td>';
            echo '<td>'.$row->salary.'</td>';
            echo '<td>'.$row->job_contact.'</td>';
            echo '<td>';
                if ($row->link) {
                    echo '<a href="'.$row->link.'">Open Link</a>';                    
                }
                echo '</td>';
            echo '<td>'.$alumni_opts[$row->alumni]->first_name.' '.$alumni_opts[$row->alumni]->last_name.'</td>';
            echo '</tr>';
        }
        ?>
    </tbody>
</table>
</div>