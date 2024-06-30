# Cat vs. Dog Classifier with k-NN

This project is an intuitive and interactive tool built around the k-Nearest Neighbors (k-NN) algorithm for classifying images as either cats or dogs. With a straightforward user interface, users can effortlessly submit cat or dog images. Behind the scenes, the k-NN classifier analyzes the input image and provides a likelihood score, indicating whether the picture is more likely to be a cat or a dog. Whether you're a machine learning enthusiast or just curious about the capabilities of k-NN, this project offers a user-friendly way to explore image classification in a fun and engaging manner.

## Features

- **User-Friendly Interface**: Easily upload images for classification.
- **k-NN Algorithm**: Utilizes the k-Nearest Neighbors algorithm for image classification.
- **Likelihood Score**: Provides a probability score indicating whether the image is more likely to be a cat or a dog.
- **Interactive Experience**: Designed to be accessible and enjoyable for users of all experience levels.

## Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) (for managing the project environment)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) (for cloning the repository)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/cjohn-afk/CatsOrDogs-kNN-Classifier.git
   ```

2. **Navigate to the Project Directory**
   ```bash
   cd CatsOrDogs-kNN-Classifier
   ```

3. **Set Up the Environment**
   ```bash
   conda create -n CatsOrDogs-kNN-Classifier --file environment.yml
   ```

4. **Activate the Environment**
   ```bash
   conda activate CatsOrDogs-kNN-Classifier
   ```

5. **Run the Project**
   ```bash
   flask --app KNNProject run
   ```

   The application will start, and you can access it by navigating to `http://127.0.0.1:5000/` in your web browser.

## Usage

1. Open your web browser and go to `http://127.0.0.1:5000/`.
2. Upload an image of a cat or a dog.
3. The classifier will process the image and display a likelihood score indicating whether the image is more likely to be a cat or a dog.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the GPL 2.0 License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or need further assistance, feel free to contact the project maintainer:

- **GitHub**: [cjohn-afk](https://github.com/cjohn-afk)

---

Enjoy using the Cat vs. Dog Classifier and exploring the world of image classification with k-NN!
