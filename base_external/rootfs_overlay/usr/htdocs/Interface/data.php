<?php
require_once 'database.php';

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $json = [];
    $sql = "SELECT * FROM data;";
    $result = $conn->query($sql);
    while($row = mysqli_fetch_assoc($result)){
        $json[] = $row;
    }
    echo json_encode($json);
}
