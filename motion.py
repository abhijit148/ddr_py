import cv2
import numpy as np

def diffImg(t0, t1, t2):
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)

cam = cv2.VideoCapture(0)

winName = "Movement Indicator"
cv2.namedWindow(winName)
imgWindow="Image from Camera"
cv2.namedWindow(imgWindow)

# Read three images first:
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
img=cam.read()[1]


t_plus = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
flag=True
while True:
  diff=diffImg(t_minus[0:50, 0:50], t[0:50, 0:50], t_plus[0:50, 0:50]) 
  if flag==True:
    if cv2.countNonZero(diff) < 1700:
      width = np.size(img, 1)
      height = np.size(img, 0)
      x = width/3
      y = height/3 #change to the desired coordinates
      text_color = (255,0,0) #color as (B,G,R)
      cv2.putText(img, "Top Left", (x,y), cv2.FONT_HERSHEY_PLAIN, 4.0, text_color, thickness=2)
    else:
      flag=False

  cv2.imshow(imgWindow,img)
  cv2.imshow( winName, diff)


  # Read next image
  t_minus = t
  t = t_plus
  img=cam.read()[1]
  t_plus = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
  #t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

  key = cv2.waitKey(10)
  if key == 27:
    cv2.destroyWindow(winName)
    break

print "Goodbye"
