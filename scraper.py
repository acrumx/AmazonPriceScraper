import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/gp/product/B07PXGQC1Q/ref=ox_sc_act_title_1?smid=ATVPDKIKX0DER&psc=1'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[:4])


    if converted_price < 159:
        send_mail()

    print(title.strip())

    print(price)
    print(converted_price)

    if converted_price > 159:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('iwf.inquiries@gmail.com', 'krztxcxytzufvcil')

    subject = 'Price fell down!'
    body = 'Check out the New  Airpods Price here: https://www.amazon.com/gp/product/B07PXGQC1Q/ref=ox_sc_act_title_1?smid=ATVPDKIKX0DER&psc=1'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'iwf.inquiries@gmail.com',
        'acrumrinex@gmail.com',
    )
    print('Congrats, the email message has been sent!')

    server.quit()

    check_price()