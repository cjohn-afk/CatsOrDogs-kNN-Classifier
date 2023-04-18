# import the necessary packages
import numpy as np 
import cv2 
import os #lets us extract subdirectory names from image paths

class SimpleTestImageLoader:

    #constructor for dataset loader class
    def __init__(self, preprocessors=None):
        self.preprocessors = preprocessors
   
        if self.preprocessors is None:
            self.preprocessors = []

    #function to load the image, call preprocess function on it, and add it to the data array
    def load(self, imagePath, verbose=-1):

        #initialize the list of features and label
        data = []

        # load input image
        image = cv2.imread(imagePath)

        # loop over the preprocessors, resize each image
        if self.preprocessors is not None:
            for p in self.preprocessors:
                image = p.preprocess(image)

        #add the resized image to the data array
        data.append(image)
                
        # return a tuple of the data and labels
        return np.array(data)


