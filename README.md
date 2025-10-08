# 📈 Stock Market Prediction using Linear Regression

## 🧠 Overview
This project aims to design a **lightweight, interpretable, and educational stock market prediction system** using **Linear Regression**.  
It focuses on providing beginners and researchers with a **transparent baseline model** that demonstrates how statistical learning methods can forecast stock price trends **without relying on complex deep learning architectures**.

---

## 🌟 Project Objectives
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

### 🧽 Model Evaluation
- **Metrics:** R² Score, Mean Absolute Error (MAE), Root Mean Squared Error (RMSE)  
- Visual comparison of predicted vs. actual prices  

### 🎨 Visualization Layer
- Scatter plots and regression lines for interpretability  
- Demonstrates how regression coefficients influence predictions  

---

## 🧹 Project Structure
```
Stock-Prediction-LinearRegression/
│
├── data/                      # Raw and preprocessed datasets
├── notebooks/                 # Jupyter notebooks for testing & EDA
├── src/                       # Core Python scripts
│   ├── preprocess.py
│   ├── train_model.py
│   ├── evaluate.py
│   └── visualize.py
│
├── results/                   # Model outputs, graphs, and reports
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
```

---

## 🚀 Installation and Usage

### 🔧 Prerequisites
- Python 3.10+
- pip (Python package installer)

### 🧭 Steps
```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/Stock-Prediction-LinearRegression.git
cd Stock-Prediction-LinearRegression

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run preprocessing
python src/preprocess.py

# 4. Train the model
python src/train_model.py

# 5. Evaluate results
python src/evaluate.py
```

#### 💡 Optional: Run via Jupyter Notebook
```bash
jupyter notebook notebooks/Stock_Prediction.ipynb
```

---

## 📊 Results Summary

| Metric | Description | Example Value |
|---------|--------------|---------------|
| **R² Score** | Measures model fit | 0.87 |
| **MAE** | Average absolute error | 1.25 |
| **RMSE** | Root mean square error | 2.10 |

> The model demonstrates good predictive power for trend direction and short-term movement but may underperform during high volatility periods — as expected for a simple regression baseline.

---

## 🧠 Key Insights
- Linear Regression provides a **clear, interpretable baseline** for market trend prediction.  
- Data preprocessing and normalization **significantly influence** model performance.  
- Visualization tools help in understanding **regression behavior** in a financial context.  
- The project sets a **foundation for future enhancement** using more advanced ML and DL techniques.

---

## 📦 Deliverables
- ✅ Baseline Prediction Model  
- ✅ Evaluation Metrics Report  
- ✅ Visualization Graphs  
- ✅ Comprehensive Documentation & Presentation Slides  

---

## 👨‍💻 Team Information

| Member | Role | ID | Email |
|---------|------|----|--------|
| **Divyanshi Agarwal** | Team Lead | 240221984 | 240221984@geu.ac.in |
| **Akhil Kotnala** | Model Development | 24021775 | 24021775@geu.ac.in |
| **Himanshu Butola** | Data Analysis & Visualization | 240211293 | 240211293@geu.ac.in |
| **Nehal Mall** | Documentation & Evaluation | 24022108 | 24022108@geu.ac.in |

---

## 🏁 Future Scope
- 📈 Integrate **Polynomial Regression** and **Lasso Regression** for performance comparison.  
- 🤖 Extend to **Neural Networks (LSTM)** for sequence-based forecasting.  
- 🌐 Deploy as a **web-based dashboard** using Streamlit or Flask.  

---

## 📜 License
This project is developed as part of the **Software Development Skills - III (SDS-III)** course at **Graphic Era University**.  
For **educational and academic purposes only**.
