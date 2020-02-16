import cv2
video = cv2.VideoCapture(0)# this variable does'nt store any value , it sends the current position in front of camera
face_1 = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    '''''
    this command don't read the image which is stored in video it send the command to video variable to access the current image
    in front of camera , every time it runs it gets the current position 
    '''''
    c, f = video.read()
    gra = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    for x, y, w, h in face_1.detectMultiScale(gra, scaleFactor=1.05, minNeighbors=10):
        cv2.rectangle(f, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imshow("yoyo", f)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
