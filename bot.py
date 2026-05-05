import requests
import tweepy
import os

# 1. Konfiguracja (Dane pobierzemy z tzw. zmiennych środowiskowych dla bezpieczeństwa)
CMC_API_KEY = os.environ.get("CMC_API_KEY")
X_API_KEY = os.environ.get("X_API_KEY")
X_API_SECRET = os.environ.get("X_API_SECRET")
X_ACCESS_TOKEN = os.environ.get("X_ACCESS_TOKEN")
X_ACCESS_SECRET = os.environ.get("X_ACCESS_SECRET")

def get_btc_price():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    parameters = {'symbol': 'BTC', 'convert': 'USD'}
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': CMC_API_KEY}
    
    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()
    price = data['data']['BTC']['quote']['USD']['price']
    return round(price, 2)

def post_to_x(price):
    # Autoryzacja w X API v2
    client = tweepy.Client(
        consumer_key=X_API_KEY, consumer_secret=X_API_SECRET,
        access_token=X_ACCESS_TOKEN, access_token_secret=X_ACCESS_SECRET
    )
    
    # TWOJA TREŚĆ POWITANIA
    message = f"Hi everyone. The current price of Bitcoin is $:{price:,}"
    
    client.create_tweet(text=message)
    print(f"Opublikowano: {message}")

if __name__ == "__main__":
    current_price = get_btc_price()
    post_to_x(current_price)
