import cv2

class Menu:
	def show(self):
		cam = cv2.VideoCapture(0)
		imgWindow="Start"
		img=cam.read()[1]
		cv2.namedWindow(imgWindow)
		cv2.imshow(imgWindow,img)
		while True:
			key = cv2.waitKey(10)
			if key==13:
				cv2.destroyWindow(imgWindow)
				break
			elif key==27:
				cv2.destroyWindow(imgWindow)
				print "Game Aborted"
				exit()
			elif key==-1:
				continue
			else:
				print key

