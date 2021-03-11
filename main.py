import requests
import smtplib
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Hbada-Ergonomic-Computer-Adjustment-Headrest/dp/B07WST1F3N/ref=sr_1_1_sspa?crid=NNMA4RKS91CG&dchild=1&keywords=Gaming+Chair&nav_sdd=aps&qid=1610134374&sprefix=chair&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVkdXN1hDRllQRUNYJmVuY3J5cHRlZElkPUExMDIyNTE3Mkc2T1Y5UEpTN0tESCZlbmNyeXB0ZWRBZElkPUEwMTY3NTQ1WjJOQ0NPMThOMVVXJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,hy;q=0.6"
}

response = requests.get(url=url, headers=header)
soup = BeautifulSoup(response.content, "lxml")

price = "$139.24"
price_without = float(price.split("$")[1])
name = soup.find(id="productTitle").get_text().split("\n")[8].split("Racing")[0]
print(name)

if price_without <= 140.00:
    with smtplib.SMTP("smtp.gmail.com") as conect:
        conect.starttls()
        conect.login(user="sberrusmoscow@gmail.com", password="00ls0002002123")
        conect.sendmail(from_addr="sberrusmoscow@gmail.com", to_addrs="arman009.cooll@gmail.com", msg=f"Subject: Amazon {name} \n\n The {name} is now just for {price}! HURRY UP!")