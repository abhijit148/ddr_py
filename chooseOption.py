import cv2
import numpy

class Menu:

	def show(self):
		imgWindow="Start"
		dancer={
			101:"images/dancer-up.jpg",
			100:"images/dancer-down.jpg",
			119:"images/dancer-ne.jpg",
			113:"images/dancer-nw.jpg",
			115:"images/dancer-se.jpg",
			97:"images/dancer-sw.jpg",
			32:"images/dancer-noMove.jpg"
		}

		intro={
		113:"images/present1.jpg",
		119:"images/present2.jpg",
		97:"images/present3.jpg",
		115:"images/present4.jpg",
		32:"images/present.jpg",
		}
		img=cv2.imread(intro[32])
		cv2.namedWindow(imgWindow)
		cv2.imshow(imgWindow,img)
		current_set=intro
		count=0
		while True:

			key = cv2.waitKey(10)
			#key=-1
			if key==13:
				current_set=dancer
				img=cv2.imread(current_set[32])
			elif key==27:
				cv2.destroyWindow(imgWindow)
				print "Game Aborted"
				exit()
			elif key==-1:
				pass
			elif key in [113,119,97,115,101,100,32]:
				img=cv2.imread(current_set[key])
			else:
				print key

			noMove=cv2.imread(dancer[32])
			crouch=cv2.imread("images/dancer-crouch.jpg")

			if numpy.array_equal(img,noMove) or numpy.array_equal(img,crouch):
				if count%8>=0 and count%8<=3:
					img=crouch
				else:
					img=noMove


			count+=1

			cv2.imshow(imgWindow,img)

