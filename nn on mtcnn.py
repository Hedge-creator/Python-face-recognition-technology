from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
from matplotlib.patches import Rectangle

def draw_image_with_boxes(image_path, result_list):
	data = pyplot.imread(image_path)
	pyplot.imshow(data)
	ax = pyplot.gca()
	for result in result_list:
		x, y, width, height = result['box']
		rect = Rectangle((x, y), width, height, fill=False, color='aqua')
		ax.add_patch(rect)
	pyplot.show()
 
image_path = 'img.jpg'
image = pyplot.imread(image_path)	
detector = MTCNN()
faces = detector.detect_faces(image)
faces_detected = "Persons detected: " + format(len(faces))
print(faces_detected) #вывод кол-ва лиц 
draw_image_with_boxes(image_path, faces)
