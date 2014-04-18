import cv2

class Menu:
	cam = cv2.VideoCapture(0)
	img=cam.read()[1]
	imgWindow="Start"
	def show(self):
		cv2.namedWindow(self.imgWindow)
		cv2.imshow(self.imgWindow,self.img)
		while True:
			key = cv2.waitKey(10)
			if key==13:
				cv2.destroyWindow(self.imgWindow)
				break
			elif key==27:
				cv2.destroyWindow(self.imgWindow)
				print "Game Aborted"
				exit()
			elif key==-1:
				continue
			else:
				print key

