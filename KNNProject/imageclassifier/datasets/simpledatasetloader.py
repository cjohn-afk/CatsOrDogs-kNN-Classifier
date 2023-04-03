# import the necessary packages
import numpy as np 
import cv2 
import os #lets us extract subdirectory names from image paths

class SimpleDatasetLoader:

    #constructor for dataset loader class
    def __init__(self, preprocessors=None):
        self.preprocessors = preprocessors
   
        if self.preprocessors is None:
            self.preprocessors = []

    #function to load the images, call preprocess function on them, and add them to the data and label arrays
    def load(self, imagePaths, verbose=-1):

        #initialize the list of features and label
        data = []
        labels = []

        # loop over the input images, loading them/extracting label based on path /dataset_name/class/image.jpg
        for (i, imagePath) in enumerate(imagePaths):
            image = cv2.imread(imagePath)
            label = imagePath.split(os.path.sep)[-2]

            # loop over the preprocessors, resize each image
            if self.preprocessors is not None:
                for p in self.preprocessors:
                    image = p.preprocess(image)

            #add the resized image to the image list, add its label to the label list
            data.append(image)
            labels.append(label)

            # show an update on the console every `verbose` images
            if verbose > 0 and i > 0 and (i + 1) % verbose == 0:
                print("[INFO] processed {}/{}".format(i + 1,
                    len(imagePaths)))
                
        # return a tuple of the data and labels
        return (np.array(data), np.array(labels))


