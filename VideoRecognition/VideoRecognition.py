import cv2
import numpy as np
import copy

FILE_LOCATION = r"sample_videos\y2mate_100e_trimmed2.mp4"

cap = cv2.VideoCapture(FILE_LOCATION)
fgbg = cv2.createBackgroundSubtractorMOG2(history=10, detectShadows=False)

# set up blob detection
blob_params = cv2.SimpleBlobDetector_Params()
blob_params.filterByArea = True
blob_params.minArea = 100000
blob_params.maxArea = 100000000
blob_params.filterByColor = True
blob_params.minThreshold = 200
blob_params.maxThreshold = 255
blob_params.filterByInertia = False
blob_detector = cv2.SimpleBlobDetector_create()

# set up text description
font = cv2.FONT_HERSHEY_PLAIN
top_left = (10, 10)
fontScale = 1
fontColor = (255,255,255)

while(1):
    len_wait = 1
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    # noise_removed = copy.deepcopy(fgmask)
    # cv2.fastNlMeansDenoising(fgmask, noise_removed, h=7)

    blob = blob_detector.detect(fgmask)

    # if blobs detected
    if len(blob) > 0:
        to_draw = cv2.drawKeypoints(fgmask, blob, None, (255,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        len_wait = -1
    else:
        to_draw = cv2.putText(fgmask, 'No blob detected yet', top_left, font, fontScale, fontColor)

    cv2.imshow('frame', to_draw)
    k = cv2.waitKey(len_wait) & 0xff
    if k == 27:
        cap.release()
        cv2.destroyAllWindows()
        break