import cv2

class motionDetector:
	t0,t1,t2=None,None,None

	def __init__(self,t_minus,t,t_plus):
		self.t0=t_minus
		self.t1=t
		self.t2=t_plus

	def detect(self):
		d1 = cv2.absdiff(self.t2, self.t1)
		d2 = cv2.absdiff(self.t1, self.t0)
		return cv2.bitwise_and(d1, d2)