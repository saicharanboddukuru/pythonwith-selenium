import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options=Options()
chrome_options.add_argument("C:\\drivers\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.nopcommerce.com/en")
element=driver.find_elements(By.XPATH,"//div[@class='footer-upper']//a")
print(len(element))
#print(element[3].text)
for ele in element:
    print(ele.text)
time.sleep(3)