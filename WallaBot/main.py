from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from random import uniform, randint
from plyer import notification
import smtplib
import os
from dotenv import load_dotenv
import pandas as pd
import re


def random_number():
    return uniform(0.5, 1.24623)


def long_random_number():
    return uniform(5.7641, 7.246)


def replace_coordinates(url):
    latitude = f"40.{randint(1, 999999)}"
    longitude = f"-3.{randint(1, 999999)}"
    url = re.sub(r'latitude=\d+\.\d+', f'latitude={latitude}', url)
    url = re.sub(r'longitude=-\d+\.\d+', f'longitude={longitude}', url)
    return url


print("-" * 50)

load_dotenv()

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

products_urls = [
    "https://es.wallapop.com/app/search?min_sale_price=55&max_sale_price=110&shipping=true&time_filter=today&filters_source=default_filters&keywords=kindle&latitude=38.5077521&longitude=-0.232639&order_by=newest&condition=un_opened,in_box,new,as_good_as_new",
    "https://es.wallapop.com/app/search?time_filter=lastWeek&min_sale_price=35&max_sale_price=110&shipping=true&latitude=40.416775&longitude=-3.703790&keywords=kindle%2011&order_by=newest&country_code=ES&filters_source=default_filters&condition=un_opened,in_box,new,as_good_as_new,good",
    "https://es.wallapop.com/app/search?latitude=41.385064&longitude=2.173403&keywords=kindle%20paperwhite%2011&min_sale_price=38&max_sale_price=110&order_by=newest&shipping=true&country_code=ES&condition=un_opened,in_box,new,as_good_as_new,good&filters_source=stored_filtersfilters_source=stored_filters"
]

products_urls = [replace_coordinates(url) for url in products_urls]

driver = webdriver.Chrome()
driver.get("https://es.wallapop.com/app/search")

try:
    sleep(random_number())
    accept_terms_button = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
    accept_terms_button.click()
except NoSuchElementException:
    pass

try:
    sleep(random_number())
    skip_button = driver.find_element(By.CLASS_NAME, 'Saltar')
    skip_button.click()
except NoSuchElementException:
    pass

try:
    sleep(long_random_number())
    nothing = driver.find_element(By.XPATH, '/html/body')
    nothing.click()
    sleep(random_number())
    nothing.click()
    sleep(random_number())
    nothing.click()
except NoSuchElementException:
    pass

links_available = []

output_file = "found_products.xlsx"

nothing = driver.find_element(By.XPATH, '/html/body')

with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    all_data = []

    loop_count = 0

    while True:
        for idx, url in enumerate(products_urls):
            driver.get(url)
            sleep(long_random_number())

            items = driver.find_elements(By.CLASS_NAME, "ItemCardList__item")

            data = []

            for item in items:
                try:
                    badge_hydrated = item.find_elements(By.CSS_SELECTOR, "wallapop-badge.hydrated")
                    if badge_hydrated and badge_hydrated[0].text == 'Reservado':
                        continue

                    link = item.get_attribute("href")
                    if link not in links_available:
                        links_available.append(link)
                    else:
                        continue

                    title = item.find_element(By.CLASS_NAME, "ItemCard__title").text

                    price_text = item.find_element(By.CLASS_NAME, "ItemCard__price").text
                    price = float(re.sub(r'[^\d.]', '', price_text.replace(',', '.')))

                    print(f"Title: {title}")
                    print(f"Price: {price}€")
                    print(f"Link: {link}")
                    print("-" * 50)

                    data.append([title, price, f'=HYPERLINK("{link}", "HYPERLINK")'])
                    all_data.append([title, price, f'=HYPERLINK("{link}", "HYPERLINK")'])

                    if loop_count != 0:
                        notification.notify(
                            title='Product Available',
                            message=f'{title}',
                            app_icon='images/walla.ico',
                            timeout=10
                        )

                    with smtplib.SMTP("smtp.gmail.com") as connection:
                        connection.starttls()
                        connection.login(os.getenv('MY_EMAIL'), os.getenv('MY_PASSWORD'))

                        # Crear el mensaje con el asunto
                        subject = f"{title}"
                        body = f"{title}\n{link}"
                        msg = f"Subject: {subject}\n\n{body}"  # Agregamos el asunto aquí

                        # Enviar el correo con asunto
                        connection.sendmail(
                            from_addr=os.getenv('MY_EMAIL'),
                            to_addrs=os.getenv('ENDPOINT_EMAIL'),
                            msg=msg
                        )

                except Exception as e:
                    pass

            df = pd.DataFrame(data, columns=["Title", "Price", "Hyperlink"])
            sheet_name = f"URL_{idx + 1}"
            df.to_excel(writer, sheet_name=sheet_name, index=False)

        all_df = pd.DataFrame(all_data, columns=["Title", "Price", "Hyperlink"])
        all_df.to_excel(writer, sheet_name="All_Data", index=False)

        loop_count += 1
