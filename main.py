import requests

def get_exchange_rate(base_currency, target_currency):
    """
    Fetches the live exchange rate between two currencies.
    """
    # building the API URL with query parameters
    url = f"https://api.frankfurter.app/latest?from={base_currency}&to={target_currency}"

    try:
        #sending the HTTP request to the server
        response = requests.get(url, timeout=5)

        #Checking if the server responded with an error (e.g. 404, 500)
        response.raise_for_status()

        #Converting the server's raw text response into a Python dictionary
        data = response.json()

        #Extracting the specific rate from the dictionary
        rate = data["rates"][target_currency]
        date = data["date"]

        return rate, date

    except requests.exceptions.HTTPError:
        print(f"\n[Error] Invalid currency code: '{base_currency}' or '{target_currency}'.")
        return None, None
    except requests.exceptions.ConnectionError:
        print("\n[Error] Could not connect to the internet. Check your network.")
        return None, None
    except Exception as e:
        print(f"\n[Error] An unexpected error occurred: {e}")
        return None, None

def main():
    print("========================================")
    print("   Live Currency Tracker & Calculator   ")
    print("========================================")

    #Asking the user for inputs
    base = input("Enter base currency (e.g. USD, EUR, GBP): ").strip().upper()
    target = input("Enter target currency (e.g. JPY, CAD, EUR): ").strip().upper()

    if base == target:
        print("\nBase and target currencies are identical (Rate: 1.0).")
        return

    #Prompting for the amount to convert
    try:
        amount = float(input(f"Enter amount in {base}: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid number. Please enter digits only.")
        return

    print("\nFetching latest rates...")
    rate, date = get_exchange_rate(base, target)

    if rate != 0:
        total = amount * rate
        print("------------------------------------")
        print(f"Date:       {date}")
        print(f"Base Rate:  1 {base} = {rate:.4f} {target}")
        print(f"Total:      {amount:,.2f} {base} = {total:,.2f} {target}")
        print("------------------------------------")

if __name__ == "__main__":
    main()
