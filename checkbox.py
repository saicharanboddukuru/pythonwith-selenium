import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options=Options()
chrome_options.add_argument("C:\\drivers\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxs=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxs))
for checkbox in checkboxs:
    if checkbox.get_attribute("value") == "option2":
     checkbox.click()
     assert checkbox.is_selected()

