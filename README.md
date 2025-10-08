# 📈 Stock Market Prediction using Linear Regression

## 🧠 Overview
This project aims to design a **lightweight, interpretable, and educational stock market prediction system** using **Linear Regression**.  
It focuses on providing beginners and researchers with a **transparent baseline model** that demonstrates how statistical learning methods can forecast stock price trends **without relying on complex deep learning architectures**.

---

## 🎯 Project Objectives
- 🔹 Predict short-term stock price trends using historical data.  
- 🔹 Develop a simple yet effective baseline regression model for financial forecasting.  
- 🔹 Promote educational understanding of regression-based prediction and model evaluation.  
- 🔹 Create an extendable framework that can later incorporate advanced models like Polynomial or Neural Networks.

---

## ⚙️ System Architecture
The project follows a **modular pipeline** consisting of the following components:

### 🗂️ Data Collection
- **Sources:** Yahoo Finance, Kaggle datasets  
- **Format:** CSV (Open, High, Low, Close, Volume)

### 🧹 Data Preprocessing
- Handling missing values, duplicates, and outliers  
- Normalization and feature scaling  

### 📊 Exploratory Data Analysis (EDA)
- Correlation heatmaps and trend line plots  
- Identification of key influencing variables  

### 🧮 Model Development
- **Algorithm:** Linear Regression (`scikit-learn`)  
- **Data Split:** 70% training, 30% testing  
- **Libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

### 🧾 Model Evaluation
- **Metrics:** R² Score, Mean Absolute Error (MAE), Root Mean Squared Error (RMSE)  
- Visual comparison of predicted vs. actual prices  

### 🎨 Visualization Layer
- Scatter plots and regression lines for interpretability  
- Demonstrates how regression coefficients influence predictions  

---

## 🧩 Project Structure
