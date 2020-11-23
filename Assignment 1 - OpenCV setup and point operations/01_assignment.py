# import the opencv library
import cv2
import time
import numpy as np

# define a video capture object
vid = cv2.VideoCapture(0)

# used to record the time when we processed last frame
prev_frame_time = 0

# used to record the time at which we processed current frame
new_frame_time = 0

fps_1 = fps_2 = fps_3 = iteration = 0

while (True):

    iteration += 1


    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # font which we will be using to display FPS
    font = cv2.FONT_HERSHEY_SIMPLEX

    # time when we finish processing for this frame
    new_frame_time = time.time()

    # Calculating the fps

    # fps will be number of frame processed in given time frame
    # since their will be most of time error of 0.001 second
    # we will be subtracting it to get more accurate result
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time

    # converting the fps into integer
    fps = int(fps)

    if iteration == 1:
        fps_1 = fps
    elif iteration == 2:
        fps_2 = fps
    elif iteration == 3:
        fps_3 = fps
        iteration = 0

    fps_avg = (fps_1 + fps_2 + fps_3) / 3

    fps_avg = int(fps_avg)

    # converting the fps to string so that we can display it on frame
    # by using putText function
    fps_avg = str(fps_avg)

    # puting the FPS count on the frame
    cv2.putText(frame, fps_avg, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)
    

    # convert image to grayscale
    orig = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # apply a Gaussian blur to the image then find the brightest
    # region
    gray = cv2.GaussianBlur(gray, (1, 1), 0)

    # perform a naive attempt to find the (x, y) coordinates of
    # the area of the image with the largest intensity value
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    cv2.circle(frame, maxLoc, 5, (255, 0, 0), 2)

    maxLoc = str(maxLoc)
    # puting the Location on the frame
    cv2.putText(frame, maxLoc, (7, 450), font, 1, (255, 0, 0), 1, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Webcam', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
