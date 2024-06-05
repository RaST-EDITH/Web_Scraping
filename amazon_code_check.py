import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# Suppress unnecessary logging messages
options = Options()
options.add_argument("--headless")
options.add_argument("--log-level=3")

# path = 'C://chromedriver.exe'
# browser = webdriver.Chrome(executable_path=path, options=options)

browser = webdriver.Chrome(options=options)

browser.get('https://www.amazon.in')

input_search = browser.find_element(By.ID, 'twotabsearchtextbox')
search_button = browser.find_element(By.XPATH, "(//input[@type='submit'])[1]")

input_search.send_keys("Samsung S23 FE")
# sleep(1)

search_button.click()

products = []
pages = 2
for i in range(pages):
    print('Scraping page', i+1)
    product = browser.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
    price = browser.find_elements(By.XPATH, "//span[@class='a-price-whole']")
    for name, cost in zip(product, price):
        product_info = {
            'name': name.text,
            'price': cost.text
        }
        products.append(product_info)
    next_button = browser.find_element(By.XPATH, "//a[text()='Next']")
    next_button.click()
    # sleep(2)

for x in products :
    print(x)
browser.quit()
