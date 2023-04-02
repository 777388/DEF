import cv2

# Define a recursive function to process video frames
def process_frame(cap):
    # Read a frame from the video stream
    ret, frame = cap.read()

    # Check if frame was successfully read
    if not ret:
        return

    # Get dimensions of frame
    height, width, _ = frame.shape

    # Loop over each row of pixels from top to bottom
    for y in range(height - 1):
        for x in range(width):
            # Set current pixel to value of next pixel in the column
            frame[y, x] = frame[y + 1, x]

    # Display the processed frame
    cv2.imshow('Pixel Cascade', frame)

    # Call the function recursively to process the next frame
    process_frame(cap)

# Capture video from Chromebook camera
cap = cv2.VideoCapture(0)

# Call the recursive function to start processing video frames
process_frame(cap)

# Release video capture resources and close window
cap.release()
cv2.destroyAllWindows()
