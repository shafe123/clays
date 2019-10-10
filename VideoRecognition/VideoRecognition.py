import cv2

FILE_LOCATION = r"sample_videos\y2mate_100e_trimmed2.mp4"

cap = cv2.VideoCapture(FILE_LOCATION)
fgbg = cv2.createBackgroundSubtractorMOG2(history=10, detectShadows=False)

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        cap.release()
        cv2.destroyAllWindows()
        break