from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import time

# For logs
d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }
# This removes the USB warning
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, desired_capabilities=d)

driver.get("https://google.co.in/search?q=stackoverflow")
driver.find_element(By.XPATH)
print(driver.get_log('browser'))

driver.quit() # Closes the browser