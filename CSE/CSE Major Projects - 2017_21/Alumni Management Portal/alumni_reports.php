<?php
include 'header.php';
$table_name = 'alumni';
if($_POST["yog"]){
    $yog = $_POST["yog"];
    $rows = get_results("SELECT * FROM $table_name WHERE yog=$yog");
} else {
    $rows = get_results("SELECT * FROM $table_name");
}
?>
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/v/dt/jszip-2.5.0/dt-1.10.20/b-1.6.1/b-colvis-1.6.1/b-flash-1.6.1/b-html5-1.6.1/b-print-1.6.1/cr-1.5.2/sp-1.0.1/datatables.min.css"/>
<script type="text/javascript" src="https://code.jquery.com/jquery-3.4.1.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.36/pdfmake.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.36/vfs_fonts.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/v/dt/jszip-2.5.0/dt-1.10.20/b-1.6.1/b-colvis-1.6.1/b-flash-1.6.1/b-html5-1.6.1/b-print-1.6.1/cr-1.5.2/sp-1.0.1/datatables.min.js"></script>
<form method="post">Year of Graduation: 
    <input type="text" name="yog" value="<?php echo $yog; ?>">
    <input type="submit">
    <a href=""><button type="button">Clear</button></a>
</form><hr>
<div style="overflow-x:auto">
    Export: 
    <table id="myTable" class="ui unstackable celled table dataTable">
        <thead>
            <tr>
                <th>Email</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Year of Graduation</th>
                <th>Present Status</th>
            </tr>
        </thead>
        <tbody>
            <?php
            foreach($rows as $row){
                echo '<tr row-id="'.$row->id.'">';
                echo '<td>'.$row->email.'</td>';
                echo '<td>'.$row->first_name.'</td>';
                echo '<td>'.$row->last_name.'</td>';
                echo '<td>'.$row->yog.'</td>';
                echo '<td>'.$row->present_status.'</td>';
            
                echo '</tr>';
            }
            ?>
        </tbody>
    </table>
    <script type="text/javascript">
    $(document).ready(function() {
        $("#myTable").DataTable( {
            dom: "Bfrtip",
            buttons: [
                "excel", "pdf"
            ],
             "pageLength": 50
        } );
    } );
    </script>
</div>