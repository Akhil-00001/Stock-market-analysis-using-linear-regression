# 📈 Stock Market Prediction using Linear Regression

## 🧠 Overview
This project presents a **simple yet effective stock market analysis and prediction system** using **Linear Regression and trend-based indicators**. It focuses on making financial data interpretation transparent and beginner-friendly by combining **data cleaning, analysis, and visualization** in one lightweight Python program.

---

## 🎯 Project Objectives
- 🔹 Perform time-series analysis of stock prices using historical data.  
- 🔹 Calculate essential financial metrics like returns and moving averages.  
- 🔹 Visualize long-term stock performance through clear trend graphs.  
- 🔹 Compute correlation between multiple stocks to analyze relationships.  
- 🔹 Provide a strong baseline for more advanced predictive models.

---

## ⚙️ System Architecture
The project workflow consists of the following components:

### 🗂️ Data Input
- **File Source:** CSV file containing stock data.
- **Expected Columns:** `Date`, `Price`

### 🧹 Data Preprocessing
- Cleans price data by removing unwanted symbols (₹, %, commas).  
- Converts date strings to valid datetime objects.  
- Drops invalid or missing entries for accurate analysis.

### 📊 Stock Analysis
- Computes **daily returns**, **50-day**, and **200-day moving averages**.  
- Displays key metrics such as total return and average volatility.  
- Uses printed summaries for clear numerical insights.

### 🎨 Visualization
- Generates line plots showing stock price trends across time.  
- Displays multiple stock comparisons on one chart.  
- Provides grid and legends for better readability.

### 🔗 Correlation Analysis
- Combines all loaded stock datasets by date.  
- Calculates **correlation matrix** between returns of different stocks.  
- Helps identify relationships between company performances.

---

## 🧩 Project Structure
```
Stock-Prediction-LinearRegression/
│
├── main.py                   # Main script for data analysis & visualization
├── stock1.csv                # Example input CSV data file
├── results/                  # (Optional) To store generated plots or reports
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies
```

---

## 🚀 Installation and Usage

### 🔧 Prerequisites
- Python 3.10+
- Required libraries:
  ```bash
  pip install pandas matplotlib openpyxl
  ```

### 🧭 Steps to Run
```bash
# 1. Clone the repository
git clone https://github.com/Akhil-00001/Stock-Prediction-LinearRegression.git
cd Stock-Prediction-LinearRegression

# 2. Run the analysis
python main.py
```

### 📁 CSV Format Example
Your `stock1.csv` should look like this:
```
Date,Price
2015-01-01,145.20
2015-01-02,146.75
2015-01-05,147.10
...
```

Ensure your file is in the **same folder** as `main.py`.

---

## 📊 Example Output
```
----- Stock A Analysis -----
Total Period: 2015-01-01 → 2025-10-01
Total Return: 82.45%
Average Annual Volatility: 19.83%

📊 Correlation Matrix:
           Stock A
Stock A    1.000000
```
A graph titled *"Stock Prices Over 10 Years"* will also be displayed showing historical price movement.

---

## 🧠 Key Insights
- Demonstrates how **pandas** and **matplotlib** can be used for financial data analysis.  
- Highlights the importance of **data cleaning** for accurate results.  
- Provides clear visual understanding of **long-term market trends**.  
- Serves as a **foundation** for advanced predictive modeling using ML/DL.

---

## 📦 Deliverables
- ✅ Cleaned and analyzed dataset.  
- ✅ Printed summary of financial metrics.  
- ✅ Line plots of price movement.  
- ✅ Correlation matrix for multi-stock comparison.  

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
- 📈 Integrate **Linear Regression Forecasting** to predict future prices.  
- 🤖 Extend to **Polynomial Regression** or **LSTM-based prediction**.  
- 🌐 Create an **interactive dashboard** using Streamlit or Flask.

---

## 📜 License
This project is part of **Software Development Skills - III (SDS-III)** course at **Graphic Era University**.  
For **educational and academic purposes only**.
