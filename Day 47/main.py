from requests import get
from bs4 import BeautifulSoup
import smtplib
from os import environ
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = environ.get("EMAIL_USER")
SENDER_PASSWORD = environ.get("EMAIL_PASS")
RECIPIENT_EMAIL = environ.get("EMAIL_RECIPIENT")
PRODUCT_URL = "https://www.amazon.com/dp/B075CYMYK6"
PRICE_THRESHOLD = 90.0

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/114.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9"
}

def fetch_current_price(url: str) -> float:
    response = get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        price_whole = soup.find("span", class_="a-price-whole").get_text().replace(",", "").replace(".", "").strip()
        price_fraction = soup.find("span", class_="a-price-fraction").get_text().strip()
        return float(f"{price_whole}.{price_fraction}")
    except (AttributeError, ValueError):
        raise Exception("Unable to locate or parse price from the page.")

def send_price_alert(price: float):
    subject = "Amazon Price Alert: Deal Available"
    body = (
        f"The product you're watching is now available for ${price:.2f}.\n\n"
        f"Check it out here:\n{PRODUCT_URL}\n\n"
        f"Regards,\nAmazon Price Tracker Bot"
    )
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
        server.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECIPIENT_EMAIL, msg=message.encode("utf-8"))

def main():
    try:
        current_price = fetch_current_price(PRODUCT_URL)
        print(f"Current price: ${current_price:.2f}")

        if current_price <= PRICE_THRESHOLD:
            send_price_alert(current_price)
            print("Price alert email sent.")
        else:
            print("No alert sent. Price is above threshold.")
    except Exception as e:
        print(f"Error: {e}")

main()
