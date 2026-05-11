# 📸 Image Classification Model (Deep Learning)

An interactive Artificial Intelligence tool that classifies images using a **Convolutional Neural Network (CNN)**. This project demonstrates how computers learn to recognize visual patterns, similar to how the human eye and brain work together.

---

### 🚀 How it Works

To make this "AI Brain" work, the project follows three main stages:

1. **The Architecture (CNN):** - **Convolutional Layers:** These act like digital magnifying glasses, searching for edges, textures, and shapes.
   - **Pooling Layers:** These simplify the data, making the model faster and more efficient.
   - **Dense Layers:** These act like a committee that looks at all the features and decides the final category.

2. **Training:** The model was trained on thousands of labeled images. It was taught using an **Optimizer** (to correct its mistakes) and a **Loss Function** (to measure how far off its guesses were).

3. **Deployment:** Using **Streamlit**, we turn the complex Python code into a simple web dashboard where anyone can upload an image and get an instant prediction.

---

### 🛠️ Tech Stack & Tools

* **Programming Language:** Python 3.x
* **Deep Learning Framework:** TensorFlow & Keras
* **Web Interface:** Streamlit
* **Image Processing:** Pillow (PIL) & NumPy
* **Data Visualization:** Matplotlib (Set with a clean white background)

---

### 📁 Project Structure

* `app.py`: The main script that runs the Streamlit web application.
* `animal_classifier_model.h5`: The pre-trained Deep Learning model (the "brain").
* `requirements.txt`: A list of all Python libraries needed to run this project.
* `README.md`: This documentation file.

---

### 💻 Installation & Setup

Follow these steps to run the project on your local machine:

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/your-username/Image-Classification-Model.git](https://github.com/your-username/Image-Classification-Model.git)
   cd Image-Classification-Model

### Install dependencies:
Bash

pip install -r requirements.txt


### Run the application:  
Bash  
streamlit run app.py


### 📊 Results

The model was trained on a diverse dataset of animal images. During training, we monitored the Accuracy and Loss to ensure the model learns effectively without just "memorizing" the pictures (avoiding Overfitting).Note for Students: This project is a perfect starting point for understanding Computer Vision. You can try swapping the dataset to classify cars, fruits, or even handwritten digits!
### 🤝 Contributing

Feel free to fork this project, report issues, or submit a pull request if you want to improve the model architecture or the UI!
