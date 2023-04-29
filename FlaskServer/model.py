from werkzeug.utils import secure_filename
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#For Image Classification Model
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

#For Flask Server
from flask import Flask, request, make_response

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

def flowerIdentifier(pillow_image_path):
    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    # image = Image.open("<IMAGE_PATH>").convert("RGB")
    image = Image.open(pillow_image_path)

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)

    return(class_name[2:])

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "POST":
        f = request.files['file']
        f.save(secure_filename(f.filename))
        print('file uploaded successfully')
        pillow_image_path = (os.path.realpath(f.filename))
        prediction = flowerIdentifier(pillow_image_path)
        print(str(prediction))
        os.remove(pillow_image_path)
    response = make_response(prediction, 200)
    response.mimetype = "text/plain"
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)