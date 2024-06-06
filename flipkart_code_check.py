import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# Suppress unnecessary logging messages
options = Options()
options.add_argument("--headless")
options.add_argument("--log-level=3")

browser = webdriver.Chrome(options=options)

try :
    browser.get('https://www.flipkart.com')
    print("Site visited")

    # Close the login popup if it appears
    try:
        login_popup_close_button = browser.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']")
        login_popup_close_button.click()
    except:
        pass

    input_search = browser.find_element(By.NAME, 'q')

    search_button = browser.find_element(By.XPATH, "//button[@type='submit']")

    product_name = "Shoes"
    input_search.send_keys(product_name)

    search_button.click()

    products = []

    pages = 2
    for i in range(pages):
        print('Scraping page', i+1)
        product = browser.find_elements(By.XPATH, "//div[@class='KzDlHZ']")
        price = browser.find_elements(By.XPATH, "//div[@class='Nx9bqj _4b5DiR']")
        for name, cost in zip(product, price):
            product_info = {
                'name': name.text,
                'price': cost.text
            }
            products.append(product_info)
        # next_button = browser.find_element(By.XPATH, "//a[@class='_1LKTO3']/span[text()='Next']")
        # next_button.click()
        sleep(2)

    for x in products :
        print(x)
    browser.quit()

except :
    print("No connection")
