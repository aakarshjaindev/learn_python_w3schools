import requests

def get_exchange_rates():
    try:
        # Using Exchange Rates API
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        return response.json()['rates']
    except:
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    if not rates:
        return "Error fetching exchange rates"
    
    # Convert to USD first (base currency)
    usd_amount = amount / rates[from_currency]
    # Convert from USD to target currency
    final_amount = usd_amount * rates[to_currency]
    return round(final_amount, 2)

def main():
    rates = get_exchange_rates()
    if not rates:
        print("Failed to fetch exchange rates")
        return

    print("\nWelcome to Currency Converter")
    print("\nAvailable currencies:", ', '.join(list(rates.keys())[:10]))  # Show first 10 currencies
    
    while True:
        try:
            from_currency = input("\nEnter base currency (or 'q' to quit): ").upper()
            if from_currency == 'Q':
                break
                
            if from_currency not in rates:
                print("Invalid currency!")
                continue
                
            to_currency = input("Enter target currency: ").upper()
            if to_currency not in rates:
                print("Invalid currency!")
                continue
                
            amount = float(input("Enter amount: "))
            
            result = convert_currency(amount, from_currency, to_currency, rates)
            print(f"\n{amount} {from_currency} = {result} {to_currency}")
            
        except ValueError:
            print("Invalid input! Please enter numeric amount")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
