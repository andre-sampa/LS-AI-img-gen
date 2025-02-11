<?php
    include 'src/gallery_functions.php';
    $imageDirectory = 'images/';
    $imageOrder = 'desc';
    $images = getImages($imageDirectory, $imageOrder); // 'asc' or 'desc'
    include 'src/gallery_content.php';

?>
