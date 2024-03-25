import cv2

cap = cv2.VideoCapture("01_OpenCVIntro/video_okuma_izleme/antalya.mp4")

while True:
    ret, frame = cap.read()

    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)##--> Function for change color
    frame=cv2.flip(frame, 1)
    cv2.imshow("Antalya",frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()