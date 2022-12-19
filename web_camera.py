import cv2 #импорт нужной библиотеки

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #распознование лиц и обЪектов

cap = cv2.VideoCapture(0) #подключаемся к камеры, указываем индекс

cap.set(cv2.CAP_PROP_FPS, 30) # Частота кадров
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600) # Ширина кадров 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # Высота кадров

while True:
    success, img = cap.read() #читаем картинку

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #цветной

    faces = face_cascade.detectMultiScale(img_gray, 1.1,19)
    cv2.namedWindow("web camera", cv2.WINDOW_NORMAL) #меняем размеры окна
    #рисуем квадраты вокруг лиц
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("web camera", img) #отображаем изображение в указанном окне
    if cv2.waitKey(10) == 27: #при нажатии клавиши esc, программа завершается
        break
cap.release() #закрываем окно, "освобождаем камеру"
cv2.destroyAllWindows()
