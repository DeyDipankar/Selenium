from argparse import Action
import os

os.chdir("..")
# print(os.getcwd())
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

driver.get("https://www.geeksforgeeks.org/")
time.sleep(3)
element = driver.find_element(By.XPATH, value="//*[@id='gcse-form']/button/i")
element_copy = element
element.click()
element_copy.send_keys("Python")
time.sleep(2)

action = ActionChains(driver)


time.sleep(2)
driver.close()
driver.quit()