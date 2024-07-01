# import the necessary packages
from sklearn.neighbors import KNeighborsClassifier #knn algorithm implementaion from scikit-learn
from sklearn.preprocessing import LabelEncoder 
from sklearn.model_selection import train_test_split #used for creating training and testing splits
from sklearn.metrics import classification_report #used to print table of results
from KNNProject.imageclassifier.preprocessing.simplepreprocessor import SimplePreprocessor
from KNNProject.imageclassifier.datasets.simpledatasetloader import SimpleDatasetLoader
from KNNProject import config
from imutils import paths
from pathlib import Path
import pickle

# import argparse
#
# # construct the argument parse when running the program
# ap = argparse.ArgumentParser()
#
# #path to image dataset is a required argument
# ap.add_argument("-d", "--dataset", required=True,
# 	help="path to input dataset")
#
# #optional, the number of neighbors(k) to use when running algorithm, default is 1
# ap.add_argument("-k", "--neighbors", type=int, default=1,
# 	help="# of nearest neighbors for classification")
#
# #optional, default -1 will use all cores on processor to run algorithm
# ap.add_argument("-j", "--jobs", type=int, default=-1,
# 	help="# of jobs for k-NN distance (-1 uses all available cores)")
# args = vars(ap.parse_args())

preprocessed_data_file = Path(config.preprocessed_data_file)
model_file = Path(config.model_file)

sp = SimplePreprocessor(32, 32)

if not preprocessed_data_file.exists():
	# grab the list of images that we'll be describing, from the dataset argument provided
	print("[INFO] loading images...")

	imagePaths = list(paths.list_images(config.dataset_path))

	# initialize the image preprocessor and dataSetLoader, images will be resized to 32 x 32 pixels

	sdl = SimpleDatasetLoader(preprocessors=[sp])

	# load the dataset from the disk
	(data, labels) = sdl.load(imagePaths, verbose=500)

	# flatten each 3d array element (image) to a single vector (pixel intensities, in this case)
	#getting data will probably happen here
	data = data.reshape((data.shape[0], 3072))

	# show some information on memory consumption of the images
	print("[INFO] features matrix: {:.1f}MB".format(
		data.nbytes / (1024 * 1024.0)))

	labeled_data = [data, labels]
	pickle.dump(labeled_data, open(config.preprocessed_data_file, 'wb'))
else:
	labeled_data = pickle.load(open(config.preprocessed_data_file, 'rb'))

data = labeled_data[0]
labels = labeled_data[1]


# convert the labels ("dog, cat") to integers, one unique integer per class
le = LabelEncoder()
labels = le.fit_transform(labels)

# partition the data into training and testing splits using 75% of
# the data for training and the remaining 25% for testing
#will likely use 100% for training and then manually add image to classify in final project
(trainX, testX, trainY, testY) = train_test_split(data, labels,
	test_size=0.25, random_state=42)


# begin evaluating:
print("[INFO] evaluating k-NN classifier...")
if not model_file.exists():
	# create KNN classifier, "neighbors" is the parameter provided at runtime
	model = KNeighborsClassifier(n_neighbors=config.neighbors,
		n_jobs=config.jobs)

	#train the model (trainX refers to the vector data, trainY refers to the labels)
	model.fit(trainX, trainY)

	pickle.dump(model, open(config.model_file, 'wb'))

else:
	model = pickle.load(open(config.model_file, 'rb'))


#use predict() on the test data (testX), print the classification report
cReport = classification_report(testY, model.predict(testX),	target_names=le.classes_, output_dict=True)
