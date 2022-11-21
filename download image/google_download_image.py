import os
os.chdir('..')
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options = ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get('https://www.google.com')
search_text = "CR7"

# this one worked
image_search_element = driver.find_element(by=By.XPATH, value='//*[@id="gb"]/div/div[1]/div/div[2]/a')
image_search_element.click()
search_space = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_space.send_keys(search_text)
search_space = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_space.send_keys(Keys.ENTER)
# image_element = driver.find_element(by=By.XPATH, value='//*[@id="islrg"]/div[1]/div[2]/a[1]/div[1]/img')

# action = ActionChains(driver)
# action.click(image_search_element)
# try:
#     action.move_to_element(search_space).key_down(Keys.LEFT_CONTROL).send_keys(search_text).perform()
# except:
#     action.move_to_element(search_space).key_down(Keys.LEFT_CONTROL).send_keys(search_text).perform()
# # action.perform()
# search_space.send_keys(search_text)
# search_space.send_keys(Keys.ENTER)

time.sleep(3)
driver.close()
driver.quit()


# driver.close()
# driver.quit()