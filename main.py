import cv2

image = cv2.imread("assets/assignment-001-given.jpg")

# Set variables for font, color and size for the text
text_position = (800, 180)
font = cv2.FONT_HERSHEY_SIMPLEX
font_size = 2
color = (0, 255, 0)
thickness = 5

(text_width, text_height), baseline = cv2.getTextSize("RAH972U", font, font_size, thickness)

overlay = image.copy()
alpha = 0.4  # Transparency

rectangle_start = (text_position[0] - 10, text_position[1] + 10)
rectangle_end = (text_position[0] + text_width + 10, text_position[1] - text_height - 10)
cv2.rectangle(overlay, rectangle_start, rectangle_end, (0, 0, 0), -1)

cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

cv2.putText(
    image,
    "RAH972U",
    text_position,
    font,
    font_size,
    color,
    thickness,
)

# Draw a green rectangle around the area of interest in the image
cv2.rectangle(image, (250, 200), (950, 920), (0, 255, 0), 8)

cv2.imshow("Result of the Image", image)

cv2.waitKey(0)

# create output image file
cv2.imwrite("assets/assignment-001-result.jpg", image)

cv2.destroyAllWindows()
