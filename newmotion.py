from imutils.video import VideoStream
import imutils
import cv2
import time
# Reading video data from the video source
vs = VideoStream(src=0).start()
time.sleep(2.0)
# initializing the first frame of the video by None
firstFrame = None
# start time
start = time.time()
# loop over the frames of the video
while True:
    # readind the current frame
    frame = vs.read()
    # if the frame cannot be grabbed break
    if frame is None:
        break
    #resize the frame , convert to grayscale and blur it
    #   - Resizing the frame
    frame = imutils.resize(frame,width=700)
    #   - Converting to gray scale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #   - Blurring it
    gray = cv2.GaussianBlur(gray,(21,21),0)
    # if the first frame is None initialize it with converted frame
    # or time difference is greater than 15 sec
    if firstFrame is None or time.time()-start > 15:
        start = time.time()
        firstFrame = gray
    # compute the absolute difference between current frame and previous frame
    frameDelta = cv2.absdiff(firstFrame,gray)
    # grayscaling the image
    thresh = cv2.threshold(frameDelta,25,255,cv2.THRESH_BINARY)[1]
    # dilate the threshold image to fill the holes, then find contours on threshold image
    # dilate -> widning the object
    # contours -> boundary
    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    #loop over the contours
    for c in cnts:
        # if contour is too small ignore it
        if cv2.contourArea(c) < 500:
            continue
        # compute the bounding box for the contour and draw it to the frame
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # showing the frames
    cv2.imshow("Motion Detection", frame)
    cv2.imshow("Thresh", thresh)
    cv2.imshow("Frame Delta", frameDelta)
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key is pressed, break from the lop
    if key == ord("q"):
        break
# cleanup the camera and close any open windows
vs.stop()
cv2.destroyAllWindows()
