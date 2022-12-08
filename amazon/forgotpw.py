import time
import os
from dotenv import load_dotenv
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

load_dotenv(override=True,dotenv_path='../.env')
PHONE_NO = os.getenv('TEST_NO')
chromedriver_autoinstaller.install() # automatically installs driver if not found in path

# Global settings
DEFAULT_LOAD_TIME = 5

options = ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])

driver = Chrome(options=options)
driver.get('https://www.amazon.com/')
driver.maximize_window()


# click on sign in
signin = driver.find_element(by=By.XPATH,value='//*[@id="nav-signin-tooltip"]/a/span')
signin.click()
time.sleep(DEFAULT_LOAD_TIME)
# insert no.
driver.find_element(by=By.XPATH, value='//*[@id="ap_email"]').send_keys(PHONE_NO)
PHONE_NO='' # to handle double sendkeys,cached by browser
# click continue
continue_clicked = driver.find_element(by=By.XPATH, value='//*[@id="continue"]')
continue_clicked.click()
time.sleep(DEFAULT_LOAD_TIME)
# forgot pw
fogot_pw_clicked = driver.find_element(by=By.XPATH, value='//*[@id="auth-fpp-link-bottom"]')
fogot_pw_clicked.click()
time.sleep(DEFAULT_LOAD_TIME)
# enter no. again
driver.find_element(by=By.XPATH, value='//*[@id="ap_email"]').send_keys(PHONE_NO)
# send confirmation code continue
continue_clicked = driver.find_element(by=By.XPATH, value='//*[@id="continue"]')
continue_clicked.click()
time.sleep(20)
driver.find_element(by=By.XPATH, value='//*[@id="cvf-resend-link"]').click()

driver.close()
driver.quit()