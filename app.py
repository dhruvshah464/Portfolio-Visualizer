import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_csv_data

# Set page configuration
st.set_page_config(page_title="Portfolio Visualizer", layout="wide")

# Title
st.title("📊 Offline Portfolio Risk & Return Visualizer")

# Symbol input with only allowed options
default_symbols = "AAPL, MSFT, GOOGL"
st.markdown("Available symbols: `AAPL`, `MSFT`, `GOOGL`")
symbols_input = st.text_input("Enter stock symbols separated by commas:", default_symbols)
symbols = [s.strip().upper() for s in symbols_input.split(",") if s.strip().upper() in ["AAPL", "MSFT", "GOOGL"]]

# Load data
dfs = []
valid_symbols = []
for symbol in symbols:
    df = load_csv_data(symbol)
    if df is not None:
        dfs.append(df["Adj Close"].rename(symbol))
        valid_symbols.append(symbol)
    else:
        st.warning(f"No data found for symbol: {symbol}")

# If valid data is available
if dfs:
    data = pd.concat(dfs, axis=1).dropna()
    returns = data.pct_change().dropna()

    # Adjusted Close Price Chart
    st.subheader("📈 Adjusted Close Prices")
    st.line_chart(data)

    # Daily Returns Chart
    st.subheader("📉 Daily Returns")
    st.line_chart(returns)

    # Risk & Return Metrics
    st.subheader("⚖️ Risk & Return Analysis")
    metrics = pd.DataFrame(index=valid_symbols)
    metrics["Expected Return"] = returns.mean() * 252
    metrics["Volatility"] = returns.std() * np.sqrt(252)
    metrics["Sharpe Ratio"] = metrics["Expected Return"] / metrics["Volatility"]
    st.dataframe(metrics.style.format("{:.2%}"))

    # Correlation Heatmap
    st.subheader("📌 Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(returns.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

else:
    st.error("⚠️ No valid stock data found. Please check the symbols and try again.")
