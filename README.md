# Data Sweeper 📊🔄

## Overview

Welcome to **Data Sweeper**, a versatile and user-friendly tool designed to transform your data files between Excel (.xlsx) and CSV (.csv) formats effortlessly. This app is built using Streamlit and Pandas, providing an intuitive interface for data cleaning, visualization, and conversion.

## Features

- **Seamless File Conversion:** Convert between Excel and CSV formats with ease.
- **Data Cleaning Options:** Remove duplicates and fill missing values with just a few clicks.
- **Data Preview:** Preview the head of your dataframe for quick inspection.
- **Column Selection:** Choose specific columns for conversion to tailor your data.
- **Data Visualization:** Visualize selected data columns with built-in charts.
- **Modern UI:** A sleek and professional interface with gradient background and transparent elements.

## How to Use

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/cr33p1ngp4ck3t/Data-Sweeper.git
   cd Data-Sweeper
   ```

2. **Install Required Libraries:**
   Ensure you have Python installed, then install the necessary libraries using pip:
   ```bash
   pip install streamlit pandas
   ```

### Running the App

1. **Run the Streamlit App:**

   ```bash
   streamlit run app.py
   ```

2. **Access the App:**
   Open your web browser and go to `http://localhost:8501` to access the Data Sweeper app.

### Using the App

1. **Upload Files:**
   Upload your .csv or .xlsx files using the file uploader.

2. **Data Preview:**
   View the name and size of the uploaded file, and preview the head of the dataframe.

3. **Data Cleaning:**

   - **Remove Duplicates:** Click the button to remove duplicate rows.
   - **Fill Missing Values:** Click the button to fill missing numerical values with the column mean.

4. **Column Selection:**
   Select the columns you want to include in the conversion.

5. **Data Visualization:**
   Optionally, visualize the selected data columns with a bar chart.

6. **File Conversion:**
   Choose the format (CSV or Excel) you want to convert the file to, and click the button to download the converted file.
