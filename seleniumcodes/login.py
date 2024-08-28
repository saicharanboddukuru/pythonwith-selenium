import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options=Options()
chrome_options.add_argument("C:\\drivers\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://demos.nop-templates.com/")
driver.find_elements(By.ID,"small-searchterms")
driver.maximize_window()
print("this is the title of the page",driver.title)
print("this is the url of the page",driver.current_url)#this command is used to capture the current url
print(driver.page_source)
time.sleep(10)
driver.quit()