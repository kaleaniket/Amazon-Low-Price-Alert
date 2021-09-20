import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

MY_EMAIL = "akaledummy@gmail.com"
PASSWORD = "93856162"

URL = "https://www.amazon.in/Test-Exclusive_2020_1151-Multi-3GB-Storage/dp/B089MT35TK/ref=sr_1_1?dchild=1&keywords=redmi+note+10+pro&qid=1632120024&sr=8-1"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Cookie": "PHPSESSID=ajf5mjhe6tfiv9jn71h3i9pc31; _ga=GA1.2.1512257273.1632120106; _gid=GA1.2.1507113444.1632120106"
}

response = requests.get(URL, headers= headers)
product_page = response.text
# print(product_page)

soup = BeautifulSoup(product_page, "lxml")

current_price = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText()
price_split = current_price.split("₹")[1]
value1 = price_split.split(",")[0]
value2 = price_split.split(",")[1]
final_price = float(value1 + value2)
print(final_price)

if final_price < 17999.1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Low price alert!!!!.\n\nRedmi Note 10 pro price drop"
        )
