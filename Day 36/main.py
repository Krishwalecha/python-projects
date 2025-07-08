import os
import json
import requests
import urllib.request
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables from .env file
load_dotenv()

# API keys and Twilio configuration
API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_FROM = os.environ.get("TWILIO_FROM")
TWILIO_TO = os.environ.get("TWILIO_TO")

GNEWS_API_KEY = os.environ.get("GNEWS_API_KEY")

# Get user input for stock symbol
symbol_input = input("Enter stock symbol you want info about (TSLA, MSFT, AAPL, etc): ").upper()


def get_stock_data(symbol: str) -> tuple[float, float]:
    """
    Fetches the latest and previous day's closing stock prices
    using the Alpha Vantage API and calculates the percentage change.

    Args:
        symbol (str): Stock symbol (e.g., "AAPL")

    Returns:
        tuple: (price_difference: float, percentage_change: float)
    """
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "compact",
        "apikey": API_KEY,
    }

    stock_response = requests.get(ALPHA_VANTAGE_ENDPOINT, params=stock_parameters)
    stock_response.raise_for_status()

    stock_data = stock_response.json()

    if "Time Series (Daily)" not in stock_data:
        raise Exception(f"Alpha Vantage API error: {stock_data}")

    time_series = stock_data["Time Series (Daily)"]
    valid_dates = list(time_series.keys())
    latest_date, previous_date = valid_dates[0], valid_dates[1]

    latest_closing_price = float(time_series[latest_date]["4. close"])
    previous_closing_price = float(time_series[previous_date]["4. close"])

    price_difference = latest_closing_price - previous_closing_price
    price_difference_percentage = (price_difference / previous_closing_price) * 100

    return price_difference, price_difference_percentage


def get_news(symbol: str) -> tuple[list[str], list[str], list[str]]:
    """
    Fetches top 3 news headlines for the given stock symbol using GNews API.

    Args:
        symbol (str): Stock symbol

    Returns:
        tuple: (titles: list[str], descriptions: list[str], urls: list[str])
    """
    gnews_url = (
        f"https://gnews.io/api/v4/search?q={symbol}&lang=en&country=us&max=3&apikey={GNEWS_API_KEY}"
    )
    with urllib.request.urlopen(gnews_url) as response:
        data = json.loads(response.read().decode("utf-8"))
        articles = data.get("articles", [])
        titles = [article['title'] for article in articles]
        descriptions = [article['description'] for article in articles]
        urls = [article['url'] for article in articles]
        return titles, descriptions, urls


def send_message():
    """
    Gets stock change data and news headlines, formats a message,
    and sends it via Twilio SMS.
    """
    try:
        price_difference, price_difference_percentage = get_stock_data(symbol_input)
        news_title, news_desc, news_urls = get_news(symbol_input)

        if news_title and news_desc and news_urls:
            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            news_body = ""

            for i in range(len(news_title)):  # zip skipped as per your request
                news_body += (
                    f"{i + 1}. {news_title[i]}: {news_desc[i]}\n"
                    f"Read more at: {news_urls[i]}\n\n"
                )

            body = (
                f"{symbol_input} {'💹' if price_difference > 0 else '📉'} {price_difference_percentage:.2f}%\n"
                f"Latest News:\n{news_body}"
            )

            message = client.messages.create(
                body=body,
                from_=TWILIO_FROM,
                to=TWILIO_TO
            )

            print(f"✅ SMS sent! Status: {message.status}")
            print(f"📩 Message content:\n{message.body}")
        else:
            print("⚠️ No news articles found or news data incomplete.")
    except Exception as e:
        print(f"❌ Error occurred: {e}")


send_message()
