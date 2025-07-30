import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options=Options()
chrome_options.add_argument("C:\\drivers\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com/")
driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys("chatgpt")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnK"))).click()
time.sleep(3)