import pyglet, cv2 
from gameScorer import gameScorer
from gamePlayer import gamePlayer
from gameTrack import gameTrack
from gameController import gameController
from gamePainter import gamePainter
from datetime import datetime
import numpy as np

class Game:
	player=None
	songFile=None
	moves=[]
	limit=1
	score=0

	def initiate(self):
		self.player=gamePlayer()
		#playerName=raw_input("Enter Player Name:")
		playerName="Abhijit"
		self.player.set(playerName)

		track=gameTrack()
		#track.printAll()
		#trackChoice=raw_input("Enter Track Choice:")
		trackChoice="gangnam"
		track.set(trackChoice)

		self.songFile=track.songFile
		self.moves=track.moves

	def checkGame(self):
		if self.songFile!=None and self.player.id!=None and len(self.moves)!=0:
			return True
		else:
			return False

	def isOver(self,start):
		if (datetime.now()-start).total_seconds()+self.limit>self.moves[-1][1]:
			#if number of seconds passed are more than time completion of the last move
			return True
		else:
			return False


	def play(self):
		if self.checkGame()!=True:
			print "Try Again"
			exit()
		moves=self.moves
		songFile=self.songFile
		limit=self.limit
		score=self.score
		#Create a window
		imgWindow="Now Playing: PyDDR"
		cv2.namedWindow(imgWindow)

		# Read three images first (for difference calculation):
		cam = cv2.VideoCapture(0)

		t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
		t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
		img=cam.read()[1]

		#Initial flipping for mirror effect
		img = cv2.flip(img,1)
		t_plus = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

		#Flip remaining
		t_minus = cv2.flip(t_minus,1)
		t = cv2.flip(t,1)

		#Calculation of width and height using numpy
		width = np.size(img, 1)
		height = np.size(img, 0)

		start=datetime.now()

		#Play music
		song = pyglet.media.load(songFile)
		song.play()
		
		#Creating objects
		scorer=gameScorer()
		controller=gameController()
		painter=gamePainter()

		while True:
			#print moves
			moves,dirs=controller.detectMoves(start,limit,moves,t_minus,t,t_plus)
			score=scorer.getScore(moves)
			#print moves
			img=painter.paint(img,moves,dirs,score,start,limit)

			cv2.imshow(imgWindow,img)
			
			# Read next image
			t_minus = t
			t = t_plus
			img=cam.read()[1]
			
			#Continuous flipping for mirror effect
			img = cv2.flip(img,1)
			t_plus = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
			key = cv2.waitKey(10)
			
			if key == 27 or self.isOver(start)==True:
				cv2.destroyWindow(imgWindow)
				break

		print "Game Over. Your score was: " + str(score)