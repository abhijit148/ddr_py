import cv2
import numpy as np
from datetime import datetime

#'Database' of images
arrows={
	'ne':'images/ne.png',
	'nw':'images/nw.png',
	'se':'images/se.png',
	'sw':'images/sw.png'
}

#Paste fixed arrows on the image in all 4 corners
def setScreen(img):
	dirs=['ne','nw','se','sw']
	for dir in dirs:
		obj=cv2.imread(arrows[dir],cv2.IMREAD_UNCHANGED)
		x,y=finalCoords(img,obj,dir)
		img=overlayImage(img,obj,x,y)
	return img

#Get coordinates to fix arrows in all 4 corners
def finalCoords(img,obj,dir):
	xmax = np.size(img, 1)-np.size(obj, 1)
	ymax = np.size(img, 0)-np.size(obj, 0)

	if dir=='se':
		return xmax,ymax
	elif dir=='ne':
		return xmax,0
	elif dir=='sw':
		return 0,ymax
	elif dir=='nw':
		return 0,0
	else: #Obsolete Situation
		return xmax/2,ymax/2 

#Draws a list of moves on an image by calling other functions
def drawMoves(img,moves,start,limit):
	for move in moves:
		img=putMove(img,start,limit,move)
	return img

#Main purpose of this method is to figure out the position where arrow should be superimposed
#and then call the superimposer - overlayImage
def putMove(img,start,limit,move):
	current=datetime.now()
	dir,timing=move
	fore=cv2.imread(arrows[dir],cv2.IMREAD_UNCHANGED) #MUST be loaded with alpha channel for overlay to work

	centery = np.size(img, 0)/2
	centerx = np.size(img, 1)/2

	offsetx=centerx*((current-start).total_seconds()-timing)/limit #(limit*100000)
	offsety=centery*((current-start).total_seconds()-timing)/limit #(limit*100000)

	posx,posy=getcoords(centerx,centery,offsetx,offsety,dir)

	#Fore positions correction w.r.t to size of fore image
	if dir=='ne':
		posx-=np.size(fore, 1)
	if dir=='sw':
		posy-=np.size(fore, 0)
	if dir=='se':
		posx-=np.size(fore, 1)
		posy-=np.size(fore, 0)

	if posx>=2*centerx-np.size(fore, 1):
		posx=2*centerx-np.size(fore, 1)-1

	if posy>=2*centery-np.size(fore, 0):
		posy=2*centery-np.size(fore, 0)-1

	if posx<0:
		posx=0

	if posy<0:
		posy=0

	img=overlayImage(img,fore,posx,posy)
	return img

#This function superimposes an image s_img (witho alpha channel) on another image l_img (without alpha channel) at coordinate x and y
def overlayImage(l_img,s_img,x_offset,y_offset):
	for c in range(0,3):
		l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1], c] = s_img[:,:,c] * (s_img[:,:,3]/255.0) +  l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1], c] * (1.0 - s_img[:,:,3]/255.0)	
	return l_img

#This function gets the next coordinate in a particular direction
def getcoords(x,y,x1,y1,dir):
	if dir=='se':
		return x+x1,y+y1
	elif dir=='ne':
		return x+x1,y-y1
	elif dir=='sw':
		return x-x1,y+y1
	elif dir=='nw':
		return x-x1,y-y1
	else:
		return x,y