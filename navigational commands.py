import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options=Options()
chrome_options.add_argument("C:\\drivers\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/")
driver.get("https://www.shopify.com/in")
driver.back()
driver.forward()
driver.refresh()
driver.quit()