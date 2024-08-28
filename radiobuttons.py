import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options=Options()
chrome_options.add_argument("C:\\drivers\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
button=driver.find_elements(driver.find_element(By.NAME,"radioButton"))
print(len(button))
driver.maximize_window()