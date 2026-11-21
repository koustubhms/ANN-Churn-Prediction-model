# ANN-Churn-Prediction-model
An Artificial Neural Network (ANN) model designed to predict whether a customer is likely to leave the bank (customer churn prediction).

# Bank Customer Churn Prediction Using ANN

## 📌 Project Overview
This project uses an **Artificial Neural Network (ANN)** to predict whether a bank customer is likely to leave the bank or continue using its services.

The model analyzes customer-related information and identifies potential customer churn, helping banks understand customer behavior and improve customer retention strategies.

## 🎯 Project Objective
- Predict whether a customer will leave the bank.
- Apply Deep Learning techniques to a real-world classification problem.
- Understand ANN architecture, model training, and evaluation.

## 🛠️ Technologies & Libraries Used
- Python
- Pandas
- Scikit-learn
- TensorFlow
- Tensorboard
- Keras
- Streamlit 

## 🧠 Model Architecture
The project uses a Sequential Artificial Neural Network with:
- Input Layer
- Hidden Layer 1 – 64 neurons (ReLU activation)
- Hidden Layer 2 – 32 neurons (ReLU activation)
- Output Layer – 1 neuron (Sigmoid activation)

**Optimizer:** Adam

**Loss Function:** Binary Crossentropy

**Problem Type:** Binary Classification

## ⚙️ Project Workflow
1. Data Collection
2. Data Preprocessing
3. Feature Scaling
4. Train-Test Split
5. ANN Model Building
6. Model Training
7. Model Evaluation
8. Customer Churn Prediction

## 📂 Project Structure
```text
Bank-Customer-Churn-Prediction/
│
├── log/
│
├── ml_env/
│
├── app.py
│
├── Churn_Modelling.csv
│
├── classification.py
│
├── encoder_geo.pkl
│
├── experiments.ipynb
│
├── label_encoder_gender.pkl
│
├── model.h5
│
├── prediction.ipynb
│
├── requirements.txt
│
├── Scalar.pkl
│
└── README.md
```

*Note: Update the folder structure according to your actual project files.*

## 🚀 Installation & Setup

**1. Clone the repository**
```bash
git clone <your-repository-url>
```

**2. Navigate to the project directory**
```bash
cd Bank-Customer-Churn-Prediction
```

**3. Create a virtual environment**
```bash
python -m venv ml_env
```

**4. Activate the virtual environment (Windows)**
```powershell
.\ml_env\Scripts\Activate.ps1
```

**5. Install dependencies**
```bash
pip install -r requirements.txt
```

**6. Run the application (if Streamlit UI is included)**
```bash
streamlit run app.py
```

## 📊 Model Output
The trained ANN model predicts whether a customer is likely to leave the bank.

- **0:** Customer is likely to stay.
- **1:** Customer is likely to leave (churn).

## 📚 Learning Outcomes
- Understanding Artificial Neural Networks.
- Implementing binary classification using TensorFlow/Keras.
- Understanding activation functions and optimizers.
- Applying feature scaling and data preprocessing.
- Training and evaluating a Deep Learning model.
- Building a practical customer churn prediction project.

## 👨‍💻 Author
**Koustubh Satalkar**

---

⭐ If you find this project useful, feel free to explore the repository!
