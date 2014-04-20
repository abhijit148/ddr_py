import cv2
import datetime
from gamePainter import gamePainter
from gameController import gameController

class Check:
	def isValid(self):
		cam = cv2.VideoCapture(0)
		imgWindow="Player Check"
		cv2.namedWindow(imgWindow)
		directions=['ne','nw','se','sw']
		limit=1
		painter=gamePainter()
		controller=gameController()

		# Read three images first (for difference calculation):
		t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
		t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
		img=cam.read()[1]

		#Initial flipping for mirror effect
		img = cv2.flip(img,1)
		t_plus = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

		number_of_times=0

		while number_of_times<2:
			for dir in directions:
				start=datetime.datetime.now()
				moves=[(dir,0,False)]
				while True:
					now=datetime.datetime.now()

					if now>start+datetime.timedelta(0,limit):
						start=now

					moves,dirs=controller.detectMoves(start,limit,moves,t_minus,t,t_plus)
					img=painter.paint(img,moves,dirs,"",start,limit)

					cv2.imshow(imgWindow,img)

					if moves[0][2]==True:
						break

					# Read next image
					t_minus = t
					t = t_plus
					img=cam.read()[1]

					#Continuous flipping for mirror effect
					img = cv2.flip(img,1)
					t_plus = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

					key = cv2.waitKey(10)
				
					if key == 27:
						cv2.destroyWindow(imgWindow)
						exit()

			number_of_times=number_of_times+1

		cv2.destroyWindow(imgWindow)