import os
import smtplib
import datetime as dt
from dotenv import load_dotenv
from random import choice

# Load environment variables from .env
load_dotenv()

# Get current weekday (Monday = 0)
today = dt.datetime.now()
weekday = today.weekday()

# Load credentials
email = os.environ.get("EMAIL_USER")
password = os.environ.get("EMAIL_PASS")
recipient = os.environ.get("EMAIL_RECIPIENT")

# Proceed only if it's Monday
if weekday == 0:
    try:
        # Read quotes
        with open(r"Day 32\Weekly Quote Sender\quotes.txt", mode="r+") as file:
            quotes = file.readlines()
            
            if not quotes:
                raise ValueError("No quotes left in the file!")

            # Select and remove quote
            quote = choice(quotes)
            quotes.remove(quote)

            # Rewrite file without the used quote
            file.seek(0)
            file.truncate()
            file.writelines(quotes)

        # Send email
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=email, password=password)

        msg = f"Subject: Monday's Motivational Quote\n\n{quote}"
        connection.sendmail(from_addr=email, to_addrs=recipient, msg=msg)
        print("✅ Email sent successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        connection.quit()
