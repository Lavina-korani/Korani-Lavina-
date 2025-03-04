


import cv2

# Load the image
image_path = 'path_to_your_image.jpg'  # Update this with your image path
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image.")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the original image
    cv2.imshow('Original Image', image)

    # Display the grayscale image
    cv2.imshow('Grayscale Image', gray_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()