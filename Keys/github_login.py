import os
import sys
# sys.path.append("..") # Doesn't work
os.chdir("..")
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#to wait before throwing exception
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from dotenv import load_dotenv


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options) #options=options

load_dotenv()
username = os.getenv('GITHUB_USERNAME')
password = os.getenv('GITHUB_PASSWORD')

driver.get("https://github.com/login")
time.sleep(2)
driver.find_element(by=By.XPATH, value='//*[@id="login_field"]').send_keys(username)
driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys(password)
driver.find_element(by=By.XPATH, value='//*[@id="login"]/div[4]/form/div/input[11]').click()
# print(serach_box.text)

# wait till the element loaded
# timeout = 5
# try:
#     element_present = EC.presence_of_element_located((By.ID, 'element_id'))
#     WebDriverWait(driver, timeout).until(element_present)
# except TimeoutException:
#     print "Timed out waiting for page to load"

# wait the ready state to be complete
delay = 10
WebDriverWait(driver=driver, timeout=delay).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
expected_error = 'Incorrect username or password.'
try:
    error_element = driver.find_element(by=By.XPATH, value='//*[@id="js-flash-container"]/div')
    # print(error_element.text)
    if error_element.text == expected_error:
        print("[!] Login failed!!")
except:
    print("[+] Login successful")
driver.close()
driver.quit()