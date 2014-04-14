from motionDetector import motionDetector
import numpy as np
import cv2
import datetime

class gameController:

	def detectMoves(self,start,limit,moves,t_minus,t,t_plus):
		movesNow=[]
		dirs=self.actions(t_minus,t,t_plus)
		toPerform=self.movesInTime(moves,start,limit)
		for move in moves:
			dir,timing,completed=move
			if dir in dirs and dir in [m[0] for m in toPerform]:
				completed=True
			movesNow.append((dir,timing,completed))
		return movesNow,dirs

	def movesInTime(self,moves,start,limit):
		toPerform=[]
		current=datetime.datetime.now()
		for move in moves:
			dir,timing,completed=move
			if current>start+datetime.timedelta(0,timing)+datetime.timedelta(0,2*limit/3) and current<start+datetime.timedelta(0,timing)+datetime.timedelta(0,limit):
				toPerform.append(move)
		return toPerform

	def actions(self,t_minus,t,t_plus):
		directions=['nw','ne','se','sw']
		width = np.size(t, 1)
		height = np.size(t, 0)
		coords={
			"nw":(0,50,0,50),
			"ne":(0,50,width-50,width),
			"sw":(height-50,height,0,50),
			"se":(height-50,height,width-50,width) 
		}
		actions=[]
		for dir in directions:
			y1,y2,x1,x2=coords[dir]
			detector=motionDetector(t_minus[y1:y2, x1:x2], t[y1:y2, x1:x2], t_plus[y1:y2, x1:x2])
			diff=detector.detect()
			if cv2.countNonZero(diff) > 1500:
				actions.append(dir)
		return actions
