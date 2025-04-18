
# 🍅 Tomato Leaf Disease Classifier

This Streamlit web app allows users to classify tomato leaf images into one of the following categories:
- Early Blight
- Late Blight
- Healthy

The model is built using TensorFlow/Keras and predicts the class of the uploaded image with a confidence score.

## 🔧 Features

- Upload a tomato leaf image (`.jpg`, `.jpeg`, or `.png`)
- Automatically classifies the disease using a pre-trained CNN model (`tomatos.h5`)
- Displays the prediction and confidence score

## 🧠 Model

- Trained with TensorFlow and saved as `tomatos.h5`
- Input image size: 256x256
- Classes: `Early_blight`, `Late_blight`, `Healthy`

## 📁 File Structure

- `app.py` : Main Streamlit application
- `tomatos.h5` : Trained CNN model file
- `requirements.txt` : List of Python dependencies
- `README.md` : Project documentation

## 📝 Example

![Example](example.png)

## 📦 Requirements

See `requirements.txt` for dependencies.

## 📬 Contact

For any queries, reach out at [your-email@example.com]

---

*Built with ❤️ using Streamlit and TensorFlow*
