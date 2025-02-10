<?php
    include 'gallery_functions.php';
    $imageDirectory = 'images/';
    $imageOrder = 'asc';
    $images = getImages($imageDirectory, $imageOrder); // 'asc' or 'desc'
    include 'gallery_content.php';

?>
