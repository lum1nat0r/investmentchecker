import yfinance as yf

def check_stock(symbol):
    try:
        # Fetch the stock data
        stock = yf.Ticker(symbol)
        
        # Get the current price of the stock
        current_price = stock.history(period='1d')['Close'].iloc[-1]
        
        # Get the 52-week high price
        ath = stock.info['fiftyTwoWeekHigh']

        # Calculate the threshold for a 20% drop
        threshold_price = ath * 0.8

        print(f"Current Price of {symbol}: ${current_price:.2f}")
        print(f"52 Week ATH of {symbol}: ${ath:.2f}")
        print(f"Threshold Price (20% down from ATH): ${threshold_price:.2f}")

        # Check if the current price is 20% down from the ATH
        if current_price <= threshold_price:
            print(f"Recommendation: Buy {symbol}! Current price is 20% down from ATH.")
        else:
            print(f"No recommendation for {symbol}. Current price is not 20% down from ATH.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    stock_symbol = input("Enter the stock symbol (e.g., GOOG): ").strip()
    check_stock(stock_symbol)
