<?php
// Function to get supported image files
function getImages($directory) {
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
    }
    return $files;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dark Theme Image Gallery</title>
    <style>
        body {
            background-color: #1a1a1a;
            color: #ffffff;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
        }

        .gallery-container {
            max-width: 1200px;
            margin: 0 auto;
        }

        h1 {
            text-align: center;
            color: #ffffff;
            margin-bottom: 30px;
        }

        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
            padding: 20px;
        }

        .gallery-item {
            position: relative;
            overflow: hidden;
            border-radius: 8px;
            background-color: #2d2d2d;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s ease;
        }

        .gallery-item:hover {
            transform: scale(1.02);
        }

        .gallery-item img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            display: block;
        }

        .image-caption {
            padding: 10px;
            background-color: rgba(0, 0, 0, 0.7);
            color: #ffffff;
            font-size: 0.9em;
            text-align: center;
        }

        @media (max-width: 768px) {
            .gallery {
                grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            }
        }
    </style>
</head>
<body>
    <div class="gallery-container">
        <h1>========== LS-AI-img-gen - Image Gallery ==========</h1>
        <div class="gallery">
            <?php
            // Specify your images directory
            $imageDirectory = 'images/';
            $images = getImages($imageDirectory);

            foreach ($images as $image) {
                echo '<div class="gallery-item">';
                echo '<img src="' . $imageDirectory . $image . '" alt="' . pathinfo($image, PATHINFO_FILENAME) . '">';
                echo '<div class="image-caption">' . pathinfo($image, PATHINFO_FILENAME) . '</div>';
                echo '</div>';
            }

            if (empty($images)) {
                echo '<p style="text-align: center; grid-column: 1/-1;">No images found in the gallery.</p>';
            }
            ?>
        </div>
    </div>
</body>
</html>