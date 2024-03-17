from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

def load_and_preprocess_image(image):
    img = Image.open(image).resize((128, 128))
    img = np.array(img) / 255.0
    return np.expand_dims(img, axis=0)

def predict(image):
    model = load_model('Model/cherry_leaf_model.h5')
    processed_image = load_and_preprocess_image(image)
    prediction = model.predict(processed_image)
    return np.round(prediction).astype(int)[0][0]
