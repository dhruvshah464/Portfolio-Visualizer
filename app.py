
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_csv_data

st.set_page_config(page_title="Portfolio Visualizer", layout="wide")

st.title("📊 Offline Portfolio Risk & Return Visualizer")
symbols_input = st.text_input("Enter stock symbols separated by commas (only AAPL, MSFT, GOOG available):", "AAPL, MSFT, GOOG")
symbols = [s.strip().upper() for s in symbols_input.split(",")]

dfs = []
valid_symbols = []
for symbol in symbols:
    df = load_csv_data(symbol)
    if df is not None:
        dfs.append(df["Adj Close"].rename(symbol))
        valid_symbols.append(symbol)
    else:
        st.warning(f"No data for symbol: {symbol}")

if dfs:
    data = pd.concat(dfs, axis=1).dropna()
    returns = data.pct_change().dropna()

    st.subheader("📈 Adjusted Close Prices")
    st.line_chart(data)

    st.subheader("📉 Daily Returns")
    st.line_chart(returns)

    st.subheader("⚖️ Risk & Return Analysis")
    metrics = pd.DataFrame(index=valid_symbols)
    metrics["Expected Return"] = returns.mean() * 252
    metrics["Volatility"] = returns.std() * np.sqrt(252)
    metrics["Sharpe Ratio"] = metrics["Expected Return"] / metrics["Volatility"]
    st.dataframe(metrics.style.format("{:.2%}"))

    st.subheader("📌 Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(returns.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
else:
    st.error("No valid stock data found.")
