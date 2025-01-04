from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

name,score,eatable = '','',''

def Mushroom(image_path):
    global name,score,eatable
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("project/AI_recognizer/keras_model.h5", compile=False)

    # Load the labels
    class_names = open("project/AI_recognizer/labels.txt", "r", encoding="utf8").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(image_path).convert("RGB")

    #resizing the image to be at least 224x224 and then cropping from the center
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
    class_name = class_names[index][:-1]
    confidence_score = round(prediction[0][index]*100)

    if index < 10:
        class_name = f'🟩{class_name[2:]}🟩'
        eatable = '🟩EATABLE🟩'
    else:
        class_name = f'🟥{class_name[3:]}🟥'
        eatable = '🟥NOT EATABLE🟥'
    # print(class_name) #debugging

    return [class_name, confidence_score, eatable]

if __name__ == '__main__':
    print(Mushroom('image.jpg'))