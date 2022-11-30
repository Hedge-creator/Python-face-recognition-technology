import cv2 #импорт библиотеки
def viewImage(image, name_of_window): #функция для вывода изображения
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = 'img.jpg' #изображение.расширение
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #распознование лиц и обЪектов
image = cv2.imread(image_path) #чтение
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #цветное
faces = face_cascade.detectMultiScale( 
    gray,
    scaleFactor= 1.1,
    minNeighbors= 5,
    minSize=(10, 10)
)
faces_detected = "Persons detected: " + format(len(faces))
print(faces_detected) #вывод кол-ва лиц 
# Рисуем квадраты вокруг лиц
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
viewImage(image,faces_detected) 
