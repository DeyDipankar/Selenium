from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from PIL import Image
from Screenshot import Screenshot

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

driver.get("https://quotes.toscrape.com/")

# By.ID - driver.find_element(By.ID, "id_of_element")
# By.NAME - driver.find_element(By.NAME, "name_of_element")
# By.XPATH - driver.find_element(By.XPATH, "xpath") - deprecated
# By.CSS_SELECTOR - driver.find_element(By.CSS_SELECTOR, "CSS Selectors") - deprecated
# By.LINK_TEXT - driver.find_element(By.LINK_TEXT, "Text of Link")
# By.PARTIAL_LINK_TEXT - driver.find_element(By.PARTIAL_LINK_TEXT, "Text of Link")
# By.TAG_NAME - driver.find_element(By.TAG_NAME, "Tag name") - deprecated
# By.CLASS_NAME - driver.find_element(By.CLASS_NAME, "class_of_element")

# Find element by classname
life_text = driver.find_element(By.LINK_TEXT, "life")
time.sleep(5)
# life_text.click()

# Take screenshot clipped
#driver.save_screenshot("life.png")

# Take full page screenshot
ss = Screenshot.Screenshot()
ss.full_Screenshot(driver, save_path = r".", image_name = "full_ss.png")

driver.quit()
image = Image.open("full_ss.png")
image.show()