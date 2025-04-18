import streamlit as st
import tensorflow as tf
import numpy as np
#from tensorflow.keras.preprocessing import image
from keras.utils import img_to_array
from PIL import Image

# Load model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("tomatos.h5")

model = load_model()

# Labels
labels = ["Early_blight", "Late_blight", "Healthy"]

# Preprocessing function
def preprocess_image(uploaded_file):
    img = Image.open(uploaded_file).convert("RGB")
    img = img.resize((256, 256))
    #img_array = image.img_to_array(img)
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    return img, img_array

# Prediction function
def predict_image(model, img_array):
    predictions = model.predict(img_array)
    predicted_class = labels[np.argmax(predictions[0])]
    confidence = round(100 * np.max(predictions[0]), 2)
    return predicted_class, confidence

# Streamlit UI
st.title("🍅 Tomato Leaf Disease Classifier")

uploaded_file = st.file_uploader("Upload a tomato leaf image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img, img_array = preprocess_image(uploaded_file)
    st.image(img, caption="Uploaded Image",use_container_width=True)
    predicted_class, confidence = predict_image(model, img_array)

    st.markdown(f"### 🧠 Prediction: `{predicted_class}`")
    st.markdown(f"### ✅ Confidence: `{confidence}%`")
