import pandas as pd
import matplotlib.pyplot as plt

# --- Load Data (CSV) ---
def load_stock_data(filename):
    # Read the file (adjust engine if needed)
    if filename.endswith('.csv'):
        df = pd.read_csv(filename)
    else:
        df = pd.read_excel(filename, engine='openpyxl')

    # Convert Date column properly
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Clean the Price column (remove commas, % or ₹ symbols if present)
    df['Price'] = df['Price'].replace({',': '', '₹': ''}, regex=True)

    # Convert to numeric type
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

    # Drop rows where Price couldn’t be converted
    df = df.dropna(subset=['Price'])

    return df




# --- Calculate Metrics ---
def analyze_stock(df, name):
    df['Daily Return'] = df['Price'].pct_change()
    df['MA_50'] = df['Price'].rolling(window=50).mean()
    df['MA_200'] = df['Price'].rolling(window=200).mean()
    print(f"\n----- {name} Analysis -----")
    print(f"Total Period: {df['Date'].iloc[0].date()} → {df['Date'].iloc[-1].date()}")
    print(f"Total Return: {((df['Price'].iloc[-1]/df['Price'].iloc[0]) - 1)*100:.2f}%")
    print(f"Average Annual Volatility: {df['Daily Return'].std()*100*252*0.5:.2f}%")
    return df


# --- Visualization ---
def plot_stocks(stock_data):
    plt.figure(figsize=(12,6))
    for name, df in stock_data.items():
        plt.plot(df['Date'], df['Price'], label=name)  # <-- use 'Price'
    plt.title("Stock Prices Over 10 Years")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.legend()
    plt.grid(True)
    plt.show()


# --- Correlation Analysis ---
def correlation_analysis(stock_data):
    """Calculate and print correlation between different stocks."""
    combined = pd.DataFrame()
    for name, df in stock_data.items():
        combined[name] = df.set_index('Date')['Price']
    corr = combined.pct_change().corr()
    print("\n📊 Correlation Matrix:")
    print(corr)
    return corr

# --- Main Execution ---
if __name__ == "__main__":
    # Load your CSV files here
    stock_files = {
        'Stock A': 'stock1.csv',
        # 'Stock B': 'stock2.csv',
        # 'Stock C': 'stock3.csv'
    }

    # Load each stock file
    stock_data = {name: load_stock_data(file) for name, file in stock_files.items()}

    # Analyze each stock
    analyzed_data = {name: analyze_stock(df, name) for name, df in stock_data.items()}

    # Plot stock data
    plot_stocks(analyzed_data)

    # Correlation analysis
    correlation_analysis(analyzed_data)
