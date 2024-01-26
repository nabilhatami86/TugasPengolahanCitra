import cv2
import numpy as np

def enhance_old_photo(input_path, output_path):
    # Read the image
    image = cv2.imread(input_path)

    # Apply a simple contrast and brightness adjustment
    alpha = 1.5  # Contrast control (1.0 means no change)
    beta = 30    # Brightness control (0 means no change)

    enhanced_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    # Save the enhanced image
    cv2.imwrite(output_path, enhanced_image)

    # Display the original and enhanced images (optional)
    cv2.imshow('Original Image', image)
    cv2.imshow('Enhanced Image', enhanced_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
old_photo_path = "text.jpg"
enhanced_photo_path = "enhanced_text.jpg"

enhance_old_photo(old_photo_path, enhanced_photo_path)
