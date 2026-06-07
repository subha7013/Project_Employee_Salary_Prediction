# 💼 Employee Salary Predictor

A Machine Learning-powered web application that predicts an employee's estimated salary based on education, job role, work experience, age, gender, and location. Built using **Python**, **Scikit-Learn**, and **Streamlit**, the application provides real-time salary predictions through an interactive user interface.

---

## 🚀 Project Overview

Employee compensation is influenced by multiple factors such as education level, years of experience, job designation, and workplace location. This project leverages Machine Learning to analyze these factors and estimate salary values with high accuracy.

The system is trained on employee salary data and deployed as a user-friendly web application where users can enter employee details and instantly receive a salary prediction.

---

## ✨ Features

* 🎓 Education-based salary estimation
* 💼 Experience and role-aware predictions
* 📍 Location-specific salary adjustments
* ⚧️ Gender and age consideration
* 🤖 Machine Learning-powered predictions
* 📊 Interactive Streamlit dashboard
* ⚡ Instant real-time salary estimation
* 📱 Responsive and easy-to-use interface

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Machine Learning

* Scikit-Learn
* Gradient Boosting Regressor

### Data Processing

* Pandas
* NumPy

### Model Serialization

* Joblib

### Visualization & Analysis

* Matplotlib
* Seaborn

---

## 📂 Project Structure

```bash
Employee-Salary-Predictor/
│
├── app.py
├── salary_boosted_model.joblib
├── salary_prediction_data.csv
├── project_Employee_Salary_Prediction.ipynb
├── requirements.txt
└── README.md
```

---

## 📊 Dataset Features

| Feature    | Description                          |
| ---------- | ------------------------------------ |
| Education  | High School, Bachelor, Master, PhD   |
| Experience | Years of professional experience     |
| Location   | Urban, Suburban, Rural               |
| Job_Title  | Engineer, Manager, Analyst, Director |
| Age        | Employee age                         |
| Gender     | Male / Female                        |
| Salary     | Target variable                      |

---

## 🧠 Machine Learning Pipeline

The model training pipeline consists of:

### Data Preprocessing

* Handling categorical variables using One-Hot Encoding
* Standardizing numerical features
* Feature transformation using ColumnTransformer

### Model

Gradient Boosting Regressor

```python
GradientBoostingRegressor(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=4,
    random_state=42
)
```

### Validation

* Train-Test Split (80-20)
* 5-Fold Cross Validation
* R² Score Evaluation
* Mean Squared Error Analysis

---

## 📈 Model Performance

| Metric                      | Value       |
| --------------------------- | ----------- |
| Average Cross Validation R² | 0.8345      |
| Test R² Score               | 0.8405      |
| Test MSE                    | 130,219,122 |

The model demonstrates strong predictive performance and generalizes well to unseen employee data.

---

## 🎯 How It Works

1. User enters employee information.
2. Input data is converted into a Pandas DataFrame.
3. The trained Gradient Boosting model processes the features.
4. Predicted salary is generated instantly.
5. Result is displayed on the Streamlit dashboard.

---

## 🖥️ User Interface

The application allows users to select:

* Education Level
* Job Title
* Gender
* Years of Experience
* Age
* Work Location

After clicking **Predict Salary**, the estimated monthly salary is displayed.

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/employee-salary-predictor.git
cd employee-salary-predictor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📦 Requirements

```txt
streamlit
pandas
numpy
scikit-learn
joblib
matplotlib
seaborn
```

---

## 🔮 Future Enhancements

* Salary range prediction
* Department-specific forecasting
* Advanced visualization dashboard
* Employee promotion prediction
* Cloud deployment using AWS or Azure
* Explainable AI (SHAP) integration
* Support for additional job categories

---

## 👨‍💻 Author

Subhasish Nath

Machine Learning | Data Science | Full Stack Development

---

## 📄 License

This project is developed for educational and portfolio purposes. Feel free to modify and extend it for learning and research.
