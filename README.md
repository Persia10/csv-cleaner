# csv-cleaner
A simple Python script that removes empty rows from CSV files using pandas.
# CSV Cleaner

A simple Python script that cleans messy CSV files by removing any rows with missing values.  
This tool uses the pandas library to help you prepare your data quickly and easily.

## Features
- Removes incomplete rows from CSV files  
- Saves the cleaned data to a new CSV file  
- Easy to use for data cleaning and preprocessing  

## Requirements
- Python 3  
- pandas library (`pip install pandas`)

## How to Use
1. Place your raw CSV file (e.g., `dirty_data.csv`) in the same folder as this script.  
2. Edit the script or use the function call below to specify your input and output file names:

   ```python
   clean_csv("dirty_data.csv", "clean_data.csv")
