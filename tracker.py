import bs4
import urllib.request
import smtplib
import time

url = 'https://www.amazon.ca/Sony-Mirrorless-ILCE7RM3-Essential-Accessories/dp/B0BY9P9RMZ/ref=sr_1_1_sspa?crid=EP0R9IKXV7UN&keywords=sony+a7&qid=1684766809&sprefix=sony+a7%2Caps%2C149&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.fe67de69-a579-4370-9bc8-5e38fc5a3bcc&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMkxPMlUyTEhTOFQ0JmVuY3J5cHRlZElkPUEwNzczMzQyMzVEMVFTSTFUVlJKSiZlbmNyeXB0ZWRBZElkPUExMDM0OTE1MkpYUlZRUFhVMUIwWiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='


def check_price():
    sauce = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce, "html.parser")
    prices = soup.find(id="corePriceDisplay_desktop_feature_div").get_text()
    price = float(prices[4:12].replace(',', ''))

    if price < 1500:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mareenafr24@gmail.com', 'spwdpnectbxtjwfy')

    subject = 'Price fell down'
    body = 'Check the link https://www.amazon.ca/Sony-Mirrorless-ILCE7RM3-Essential-Accessories/dp/B0BY9P9RMZ/ref=sr_1_1_sspa?crid=EP0R9IKXV7UN&keywords=sony+a7&qid=1684766809&sprefix=sony+a7%2Caps%2C149&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.fe67de69-a579-4370-9bc8-5e38fc5a3bcc&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMkxPMlUyTEhTOFQ0JmVuY3J5cHRlZElkPUEwNzczMzQyMzVEMVFTSTFUVlJKSiZlbmNyeXB0ZWRBZElkPUExMDM0OTE1MkpYUlZRUFhVMUIwWiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'mareenafr24@gmail.com',
        'mareenafr@gmail.com',
        msg
    )
    print('EMAIL HAS BEEN SENT!')

    server.quit()


while True:
    check_price()
    time.sleep(60)
