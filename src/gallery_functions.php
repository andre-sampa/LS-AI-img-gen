<?php

function getImages($directory, $imageOrder = 'desc') {
    $allowedTypes = array('jpg', 'jpeg', 'png', 'gif');
    $files = array();

    if (is_dir($directory)) {
        $dirContent = scandir($directory);
        foreach ($dirContent as $file) {
            $extension = strtolower(pathinfo($file, PATHINFO_EXTENSION));
            if (in_array($extension, $allowedTypes)) {
                $files[] = $file;
            }
        }

       // Use strtolower for case-insensitive comparison
        $order = strtolower($imageOrder); // Normalize the input

        if ($order == 'desc') {
            rsort($files);
        } elseif ($order == 'asc') {
            sort($files);
        } // Add other sorting options if needed
    }
    return $files;
}

?>