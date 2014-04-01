import cv2
import numpy as np

#'Database' of images
arrows={
	'ne':'images/ne.png',
	'nw':'images/nw.png',
	'se':'images/se.png',
	'sw':'images/sw.png'
}

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
def getcoords(x,y,dir):
	if dir=='se':
		return x+10,y+10
	elif dir=='ne':
		return x-10,y+10
	elif dir=='sw':
		return x+10,y-10
	elif dir=='nw':
		return x-10,y-10
	else:
		return x,y

#A function to move an arrow on a bacground image - back
def animate(back,x,y,dir):
	fore=cv2.imread(arrows[dir])
	x,y=getcoords(x,y,dir)
	if x>=np.size(back, 0)-np.size(fore, 0) or y>=np.size(back, 1)-np.size(fore, 1) or x<0 or y<0:
			x=np.size(back, 0)/2
			y=np.size(back, 1)/2
	#print x,y,np.size(back, 1)-np.size(fore, 1),np.size(back, 0)-np.size(fore, 0)
	output=overlayImage(back,fore,x,y)
	return output,x,y