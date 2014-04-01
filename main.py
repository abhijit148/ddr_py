import cv2
import numpy as np
import arrows
from datetime import datetime

def diffImg(t0, t1, t2):
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)

cam = cv2.VideoCapture(0)

imgWindow="Image from Camera"
cv2.namedWindow(imgWindow)

# Read three images first:
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
img=cam.read()[1]
t_plus = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#Calculation of width and height using numpy
width = np.size(img, 1)
height = np.size(img, 0)

#The moves data
moves=[("nw",1.5),
  ("ne",3.5),
  ("sw",6),
  ("se",8.5) ]

#The coords
coords={
  "nw":(0,50,0,50),
  "ne":(0,50,width-50,width),
  "sw":(height-50,height,0,50),
  "se":(height-50,height,width-50,width) 
}

#Other initialization variables
x,y=height/2,width/2
start=datetime.now()
i=0

score=0

#Initial flipping for mirror effect
t_minus = cv2.flip(t_minus,1)
t = cv2.flip(t,1)
t_plus = cv2.flip(t_plus,1)

while True:
  #Printing out the scores
  cv2.putText(img, "Score: "+str(score),(width/3,height/9) , cv2.FONT_HERSHEY_PLAIN, 2.0, color=(0,0,0), thickness=2)

  #For each move
  if i<len(moves):
    dir,timing=moves[i] #timing is the time under which the action must be performed.
    y1,y2,x1,x2=coords[dir]
    diff=diffImg(t_minus[y1:y2, x1:x2], t[y1:y2, x1:x2], t_plus[y1:y2, x1:x2]) 
    current=datetime.now()
    if cv2.countNonZero(diff) < 1750 and (current-start).total_seconds()<=timing: #1750 is our threshold
      text_color = (255,0,0) #color as (B,G,R)
      img,x,y=arrows.animate(img,x,y,dir)

    else:
      if(current-start).total_seconds()<=timing:
        score+=25

      i+=1
      x,y=height/2,width/2

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
