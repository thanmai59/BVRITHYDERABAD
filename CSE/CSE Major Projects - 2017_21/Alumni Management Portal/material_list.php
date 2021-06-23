<?php
include 'header.php';
$table_name = 'material';
?>
<div style="overflow-x:auto">
<table id="myTable" class="ui unstackable celled table dataTable">
    <thead>
        <tr>
            <th>Material</th>
            <th>File</th>
            <th>Alumni</th>
            <th>Action</th>
        </tr>
    </thead>
    <tbody>
        <?php
        $rows = get_results("SELECT * FROM $table_name ORDER BY id DESC");
        $alumni_opts = get_results("SELECT id,first_name,last_name FROM alumni",OBJECT_K);
        foreach($rows as $row){
            echo '<tr row-id="'.$row->id.'">';
            echo '<td>'.$row->material.'</td>';
            echo '<td><a href="'.$row->file.'" target="_blank"></td>';
            echo '<td>'.$alumni_opts[$row->alumni]->first_name.' '.$alumni_opts[$row->alumni]->last_name.'</td>';
            echo '</tr>';
        }
        ?>
    </tbody>
</table>
</div>