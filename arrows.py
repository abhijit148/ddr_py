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

	centery = np.size(img, 1)/2
	centerx = np.size(img, 0)/2

	offsetx=centerx*(current-start).microseconds/(limit*100000)
	offsety=centery*(current-start).microseconds/(limit*100000)

	posx,posy=getcoords(centerx,centery,offsetx,offsety,dir)

	fore=cv2.imread(arrows[dir])

	if posx>=2*centerx-np.size(fore, 0):
		posx=2*centerx-np.size(fore, 0)-1

	if posy>=2*centery-np.size(fore, 1):
		posy=2*centery-np.size(fore, 1)-1

	if posx<0:
		posx=0

	if posy<0:
		posy=0

	#print offsetx,offsety
	img=overlayImage(img,fore,posx,posy)
	return img

#This function superimposes an image fore (without black) on another image back at coordinate x and y
def overlayImage(back,fore,x,y):
	background=back
	foreground=fore
	output=background
	width = np.size(foreground, 1)
	height = np.size(foreground, 0)
	for i in range(width):
		for j in range(height):
			if sum(foreground[i][j])!=0:
				output[x+i][y+j]=foreground[i][j]

	return output

#This function gets the next coordinate in a particular direction
def getcoords(x,y,x1,y1,dir):
	if dir=='se':
		return x+x1,y+y1
	elif dir=='ne':
		return x-x1,y+y1
	elif dir=='sw':
		return x+x1,y-y1
	elif dir=='nw':
		return x-x1,y-y1
	else:
		return x,y