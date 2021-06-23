<?php
include 'header.php';
$table_name = 'event';
if ($_SESSION["role"]!='student') {
    echo "<h3>You are not an ALUMINI</h3>";
    exit;
}
?>
<div style="overflow-x:auto">
<table id="myTable" class="ui unstackable celled table dataTable">
    <thead>
        <tr>
            <th>Event</th>
            <th>Poster</th>
            <th>Event Date</th>
            <th>Time</th>
            <th>Location</th>
            <th>Action</th>
        </tr>
    </thead>
    <tbody>
        <?php
        $rows = get_results("SELECT * FROM $table_name ORDER BY id DESC");
        foreach($rows as $row){
            echo '<tr row-id="'.$row->id.'">';
            echo '<td>'.$row->event.'</td>';
            $file_url = $row->poster;
            echo '<td>';
            if($file_url){
                echo '<a href="'.$file_url.'" target="_blank"><b>View<b></a>';
            }
            echo '</td>';
            echo '<td>'.$row->event_date.'</td>';
            echo '<td>'.$row->time.'</td>';
            echo '<td>'.$row->location.'</td>';
            echo '<td><a href="event_register.php" class="ui green button">Register</a></td>';
            echo '</tr>';
        }
        ?>
    </tbody>
</table>
</div>