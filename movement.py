import datetime
import numpy as np
import cv2

def diffImg(t0, t1, t2):
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)

def movesInTime(moves,start,limit):
  toPaint=[]
  toPerform=[]
  current=datetime.datetime.now()
  for move in moves:
    dir,timing=move
    if current>start+datetime.timedelta(0,timing) and current<start+datetime.timedelta(0,timing)+datetime.timedelta(0,limit):
      toPaint.append(move)
    if current>start+datetime.timedelta(0,timing)+datetime.timedelta(0,limit/2) and current<start+datetime.timedelta(0,timing)+datetime.timedelta(0,limit):
      toPerform.append(move)
  return toPaint,toPerform

def actions(t_minus,t,t_plus):
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
    diff=diffImg(t_minus[y1:y2, x1:x2], t[y1:y2, x1:x2], t_plus[y1:y2, x1:x2])
    if cv2.countNonZero(diff) > 1500:
      actions.append(dir)
  return actions

def completed(moves,start,dirs,limit):
  completed=[]
  #dirs=actions(t_minus,t,t_plus)
  toPaint,toPerform=movesInTime(moves,start,limit)
  for move in toPerform:
    dir,timing=move
    if dir in dirs and dir not in [m[0] for m in completed]:
      completed.append(move)
      toPaint.remove(move)
  return completed,toPaint