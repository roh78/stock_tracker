# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "AMZN": 3300,
    "MSFT": 300
}

portfolio = {}

# Taking user input
print("Enter your stock holdings (type 'done' to finish):")

while True:
    stock = input("Enter stock symbol: ").upper()
    
    if stock == 'DONE':
        break

    if stock not in stock_prices:
        print("Stock not available in price list.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculating total investment
total_investment = 0

print("\n--- Portfolio Summary ---")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value

    print(f"{stock}: {quantity} shares × ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to file
save_option = input("\nDo you want to save the result? (yes/no): ").lower()

if save_option == "yes":
    file_type = input("Save as (txt/csv): ").lower()

    if file_type == "txt":
        with open("portfolio.txt", "w") as file:
            file.write("Portfolio Summary\n")
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                value = price * quantity
                file.write(f"{stock}: {quantity} × {price} = {value}\n")
            file.write(f"\nTotal Investment: {total_investment}")

        print("Saved as portfolio.txt")

    elif file_type == "csv":
        with open("portfolio.csv", "w") as file:
            file.write("Stock,Quantity,Price,Value\n")
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                value = price * quantity
                file.write(f"{stock},{quantity},{price},{value}\n")
            file.write(f"\nTotal,,,{total_investment}")

        print("Saved as portfolio.csv")

    else:
        print("Invalid file type. Skipping save.")