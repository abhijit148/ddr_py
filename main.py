import cv2
import numpy as np
from datetime import datetime

#implemented separately in same folder
import arrows
import movement
from tracks import gangnam

import pyglet

#The song moves data
songFile,moves=gangnam.songFile,gangnam.moves
song = pyglet.media.load(songFile)
song.play()
#pyglet.app.run()

#Create a window
imgWindow="Image from Camera"
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

#Other initialization variables
start=datetime.now()
score=0
limit=1

while True:
  
  dirsCompleted=movement.actions(t_minus,t,t_plus)
  img=arrows.setScreen(img,dirsCompleted)

  #Printing out the scores
  cv2.putText(img, str(score),(width/2,height/9) , cv2.FONT_HERSHEY_PLAIN, 2.0, color=(0,0,0), thickness=2)
  completed,notCompleted=movement.completed(moves,start,dirsCompleted,limit)
  img=arrows.drawMoves(img,notCompleted,start,limit)

  #Calculating score and ensuring non-repetition of completed moves
  score+=25*len(completed)
  for move in completed:
    moves.remove(move)

  cv2.imshow(imgWindow,img)

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
    break

print "Goodbye"