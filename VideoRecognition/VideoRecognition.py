import cv2
import numpy as np
import copy

FILE_LOCATION = r"sample_videos\y2mate_100e_trimmed2.mp4"

cap = cv2.VideoCapture(FILE_LOCATION)
fgbg = cv2.createBackgroundSubtractorMOG2(history=10, detectShadows=False)

# separate out orange colors
ORANGE_MIN = np.array([10, 50, 50], np.uint8)
ORANGE_MAX = np.array([20, 255, 255], np.uint8)

# set up blob detection
blob_params = cv2.SimpleBlobDetector_Params()
blob_params.filterByArea = True
blob_params.minArea = 100
blob_params.filterByColor = True
blob_params.blobColor = 255
blob_params.filterByInertia = False
blob_detector = cv2.SimpleBlobDetector_create(blob_params)

# set up text description
font = cv2.FONT_HERSHEY_PLAIN
top_left = (10, 10)
fontScale = 1
fontColor = (255,255,255)

# keep track of how many frames in a row we matched
frames_detected = 0

while(1):
    len_wait = 1
    ret, fgmask = cap.read()

    if not ret:
        cap.release()
        cv2.destroyAllWindows()
        break

    #reduce frame window to limit processing
    fgmask = fgmask[:, 960:, :]

    #convert to black/white
    fgmask = fgbg.apply(fgmask)
    #remove noise
    fgmask = cv2.medianBlur(fgmask, 7)    
    #fgmask = cv2.cvtColor(fgmask, cv2.COLOR_BGR2HSV)
    #fgmask = cv2.inRange(fgmask, ORANGE_MIN, ORANGE_MAX)

    # noise_removed = copy.deepcopy(fgmask)
    # cv2.fastNlMeansDenoising(fgmask, noise_removed, h=7)

    blob = blob_detector.detect(fgmask)

    print(fgmask.shape)
    # if blobs detected
    if len(blob) > 0:
        to_draw = cv2.drawKeypoints(fgmask, blob, None, (255,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        # wait for keyboard input
        len_wait = -1

        frames_detected += 1
    else:
        to_draw = cv2.putText(fgmask, 'No blob detected yet', top_left, font, fontScale, fontColor)
        frames_detected == 0

    if frames_detected > 3:
        # switch over to object tracking
        pass

    cv2.imshow('frame', to_draw)
    k = cv2.waitKey(len_wait) & 0xff
    if k == 27:
        cap.release()
        cv2.destroyAllWindows()
        break

