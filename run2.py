from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
dc = DesiredCapabilities.CHROME
dc["goog:loggingPrefs"] = {"browser":"INFO"}
driver = webdriver.Chrome(options=options, desired_capabilities=dc)
driver.get("https://google.co.in/search?q=stackoverflow")
driver.implicitly_wait(10)

for entry in driver.get_log('browser'):
    print(entry)
 
driver.quit()