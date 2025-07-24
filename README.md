### 📊 Portfolio Visualizer

A simple interactive Streamlit app to visualize stock data from CSV files. Ideal for exploring historical trends and comparing performance of different stocks like AAPL, MSFT, AMZN, and more.

---

### 🚀 Features

* 📈 Visualize historical stock prices
* 📁 Load data from local CSV files
* 🔍 Filter and select individual stocks
* 📅 Dynamic date range selection
* 📊 Line chart for closing prices

---

### 🗂️ Project Structure

```
Portfolio-Visualizer/
├── app.py                # Main Streamlit application
├── utils.py              # Utility functions for data processing
├── stock_data_csvs/      # Folder with stock CSV files
│   ├── AAPL.csv
│   ├── MSFT.csv
│   ├── GOOGL.csv
│   ├── AMZN.csv
│   └── TSLA.csv
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

### ⚙️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/dhruvshah464/Portfolio-Visualizer.git
   cd Portfolio-Visualizer
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**

   ```bash
   streamlit run app.py
   ```

---

### 📁 Add Your Own Data

Place your stock CSV files in the `stock_data_csvs/` folder. Each file should follow this structure:

```
Date,Open,High,Low,Close,Volume
2020-01-01,300,305,295,303,1200000
```

---

### 📌 Requirements

* Python 3.7+
* Streamlit
* Pandas
* Plotly or Matplotlib (if used)

---

### 📬 Author

**Dhruv Shah**
Connect on [LinkedIn](www.linkedin.com/in/shah-dhruv-)

---

