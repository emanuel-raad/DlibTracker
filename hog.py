import cv2
import dlib

cap = cv2.VideoCapture(1)
detector = dlib.simple_object_detector("detector.svm")
cv2.namedWindow('window')
green = (0, 255, 0)

print cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

while True:
    _, frame = cap.read()
    dets = detector(frame)

    if len(dets) > 0:
        for d in dets:
            center = (d.center().x, d.center().y)
            width = d.width()/2
            cv2.circle(frame, center, width, green, 2)
    cv2.imshow('window', frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
