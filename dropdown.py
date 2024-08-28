import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from checkbox import checkboxs
chrome_options=Options()
chrome_options.add_argument("C:\\drivers\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://demo.automationtesting.in/Register.html")
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("saicharan")
driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("boddukuru")
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("saicharan@gmail.com")
driver.find_element(By.XPATH,"//input[@type='tel']").send_keys("8330969659")
driver.find_element(By.XPATH,"//input[@value='Male']").click()
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    checkbox.click()#here selecting the all check boxes
    driver.find_element(By.XPATH,"//div[@id='msdd']")

