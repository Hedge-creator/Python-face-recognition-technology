#импорт необходимых библиотек
from mtcnn.mtcnn import MTCNN #библиотека ии
from matplotlib import pyplot # бибилиотека, нужная для вывода изображения на экран компьютера
from matplotlib.patches import Rectangle #также подключаем библиотеку, способную рисовать квадраты вокруг найдённых лиц
#задаём функцию для создания квадратов
def draw_image_with_boxes(image_path, result_list):
	data = pyplot.imread(image_path) #чтение полученного изображения
	pyplot.imshow(data) #построение картинки в pyplot
	ax = pyplot.gca()
	#нанесение квадратов на график
	for result in result_list:
		#узнаем координаты лиц
		x, y, width, height = result['box']
		#создаём форму
		rect = Rectangle((x, y), width, height, fill=False, color='aqua') #можно задать толщину линии и её цевт
		ax.add_patch(rect) #рисуем квадраты
	#вывод полученного графика
	pyplot.show()
 
image_path = 'img.jpg' #изначальное изображние
image = pyplot.imread(image_path) #загружаем изображение в график
#создаём детектор, используя веса
detector = MTCNN()
#распознование лиц
faces = detector.detect_faces(image) 
#вывод кол-ва лиц 
faces_detected = "Persons detected: " + format(len(faces))
print(faces_detected)
#отображение лиц на исходном изображении
draw_image_with_boxes(image_path, faces)
