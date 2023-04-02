# import the necessary packages
import cv2
class SimplePreprocessor:
	def __init__(self, width, height, inter=cv2.INTER_AREA):
		# constructor for preprocessor, width/height/interpolation defined for use when resizing our imags
		self.width = width
		self.height = height
		self.inter = inter

	#rsize() function from cv2 resizes an individual image
	def preprocess(self, image):
		return cv2.resize(image, (self.width, self.height),
			interpolation=self.inter)
