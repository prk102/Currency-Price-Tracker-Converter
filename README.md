# Currency-Price-Tracker-Converter
A terminal-based tool that calculates real-time exchange rates for global currencies.

## Features
- Real-time exchange rate calculation across 30+ fiat currencies.
- Clean terminal UI with input sanitation and formatted decimal precision.
- Robust network error handling (invalid codes, timeouts, offline fallback).
- Zero authentication or API keys required.

## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/currency-converter-cli.git](https://github.com/YOUR_USERNAME/currency-converter-cli.git)
   cd currency-converter-cli
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script from your terminal:
```bash
python main.py
```

### Example

```text
====================================
   Live Currency Tracker & Calc     
====================================
Enter base currency (e.g. USD, EUR, GBP): USD
Enter target currency (e.g. JPY, CAD, EUR): EUR
Enter amount in USD: 250

Fetching latest rates...
------------------------------------
Date:       2026-09-28
Base Rate:  1 USD = 0.9184 EUR
Total:      250.00 USD = 229.60 EUR
------------------------------------
```

## Tech Stack
- **Language:** Python
- **Libraries:** `requests`
- **Data Source:** Frankfurter API (European Central Bank data)
