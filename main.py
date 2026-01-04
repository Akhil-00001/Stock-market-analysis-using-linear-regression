import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- Load Data (CSV/Excel) ---
def load_stock_data(filename):
    if filename.endswith('.csv'):
        df = pd.read_csv(filename)
    else:
        df = pd.read_excel(filename, engine='openpyxl')

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    df['Price'] = df['Price'].replace({',': '', '₹': ''}, regex=True)
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

    df = df.dropna(subset=['Price'])
    df = df.sort_values('Date').reset_index(drop=True)
    return df


# --- Analyze Single Stock ---
def analyze_stock(df, name):
    df['Daily Return'] = df['Price'].pct_change()
    df['MA_50'] = df['Price'].rolling(window=50).mean()
    df['MA_200'] = df['Price'].rolling(window=200).mean()

    print(f"\n----- {name} Analysis -----")
    print(f"Total Period: {df['Date'].iloc[0].date()} → {df['Date'].iloc[-1].date()}")
    print(f"Total Return: {((df['Price'].iloc[-1]/df['Price'].iloc[0]) - 1)*100:.2f}%")
    print(f"Average Annual Volatility: {df['Daily Return'].std()*100*252*0.5:.2f}%")
    return df


# --- Plot Multiple Stocks ---
def plot_stocks(stock_data):
    plt.figure(figsize=(12,6))
    for name, df in stock_data.items():
        plt.plot(df['Date'], df['Price'], label=name)
    plt.title("Stock Price Comparison")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.legend()
    plt.grid(True)
    plt.show()


# --- Linear Regression Trend Line ---
def plot_linear_regression(df, name):
    x = (df['Date'] - df['Date'].min()).dt.days.values  # Convert to numpy array
    y = df['Price'].values  # Convert to numpy array
    
    # Remove any NaN values
    mask = ~np.isnan(x) & ~np.isnan(y)
    x = x[mask]
    y = y[mask]
    
    if len(x) < 2:
        print(f"Not enough valid data points for {name}")
        return
        
    try:
        m, b = np.polyfit(x, y, 1)
        
        plt.figure(figsize=(10,5))
        # Plot original data
        plt.scatter(df['Date'], df['Price'], alpha=0.5, label=f"{name} Price")
        
        # Calculate and plot trend line
        line_x = np.array([df['Date'].min(), df['Date'].max()])
        line_y = m * np.array([0, (df['Date'].max() - df['Date'].min()).days]) + b
        plt.plot(line_x, line_y, 'r-', label=f"{name} Trend Line", linewidth=2)
        
        plt.title(f"{name} Price Trend (with Linear Regression)")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error calculating trend line for {name}: {str(e)}")


# --- Correlation and Comparison ---
def correlation_analysis(stock_data):
    combined = pd.concat(
    {name: df.drop_duplicates(subset='Date').set_index('Date')['Price'] for name, df in stock_data.items()},
    axis=1
    )


    combined = combined.fillna(method='ffill').fillna(method='bfill')
    corr = combined.pct_change().corr()

    print("\n📈 Correlation Matrix:")
    print(corr)

    plt.figure(figsize=(6, 4))
    plt.imshow(corr, cmap='coolwarm', interpolation='none')
    plt.colorbar(label="Correlation")
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
    plt.yticks(range(len(corr.index)), corr.index)
    plt.title("Stock Price Correlation Heatmap")
    plt.tight_layout()
    plt.show()


    return corr


# --- Compare Daily Returns ---
def plot_daily_returns(stock_data):
    plt.figure(figsize=(12,6))
    for name, df in stock_data.items():
        plt.plot(df['Date'], df['Daily Return'], label=f"{name} Daily Return")
    plt.title("Daily Return Comparison")
    plt.xlabel("Date")
    plt.ylabel("Daily Return (%)")
    plt.legend()
    plt.grid(True)
    plt.show()


# --- Main Execution ---
if __name__ == "__main__":
    stock_files = {
        'Adani': 'stock1.csv',
        'Alibaba': 'stock2.csv',
        'IRFC': 'stock3.csv',
        'Suzlon Energy': 'stock4.csv'
    }

    stock_data = {name: load_stock_data(file) for name, file in stock_files.items()}
    analyzed_data = {name: analyze_stock(df, name) for name, df in stock_data.items()}

    plot_stocks(analyzed_data)
    plot_daily_returns(analyzed_data)
    correlation_analysis(analyzed_data)

    # --- Linear Regression Trend Line for Each Stock ---
    for name, df in analyzed_data.items():
        plot_linear_regression(df,name)
