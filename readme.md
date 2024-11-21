# Cryptocurrency Data Fetcher and Analyzer

## Overview
This project fetches live cryptocurrency data for the top 50 cryptocurrencies, performs analysis, and updates an Excel sheet every 5 minutes.

## Prerequisites
- Python 3.8+
- Internet connection

## Installation
1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install requirements:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the script:
```
python crypto_data_fetcher.py
```

## Features
- Fetches top 50 cryptocurrencies by market cap
- Includes:
  * Cryptocurrency Name
  * Symbol
  * Current Price (USD)
  * Market Capitalization
  * 24-hour Trading Volume
  * 24-hour Price Change (%)

- Generates an Excel file with:
  * Live cryptocurrency data
  * Color-coded price change percentages
  * Separate analysis sheet

## Notes
- Requires stable internet connection
- Updates data every 5 minutes
- Uses CoinGecko API for data retrieval