import cv2

cap = cv2.VideoCapture('Video_data/19.mp4')
while True:

    ret, frame = cap.read()
    frame = cv2.resize(frame, (1200, 800))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print(fps)
    cv2.imshow("Window", frame)
    if cv2.waitKey(1) == 27:
        break
    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite("base_img_cap.jpg", frame)
        print('Saved')
cv2.destroyAllWindows()
