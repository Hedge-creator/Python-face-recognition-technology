#импорт библиотек
from mtcnn.mtcnn import MTCNN 
from matplotlib import pyplot 
from matplotlib.patches import Rectangle 
#функция для создания квадратов
def draw_image_with_boxes(image_path, result_list):
	data = pyplot.imread(image_path) #чтение изображения
	pyplot.imshow(data) #построение картинки в pyplot
	ax = pyplot.gca()
	#нанесение квадратов на график
	for result in result_list:
		#координаты лиц
		x, y, width, height = result['box']
		#форма фигуры
		rect = Rectangle((x, y), width, height, fill=False, color='aqua') #можно задать толщину линии и её цвет
		ax.add_patch(rect) #рисование квадратов
	#вывод полученного графика
	pyplot.show()
 
image_path = 'img2.jpg' #изначальное изображние
image = pyplot.imread(image_path) #загруженное изображение в график
#создание детектора с использованием весов
detector = MTCNN()
#распознование лиц
faces = detector.detect_faces(image) 
#вывод кол-ва лиц 
faces_detected = "Persons detected: " + format(len(faces))
print(faces_detected)
#отображение лиц на исходном изображении
draw_image_with_boxes(image_path, faces)
