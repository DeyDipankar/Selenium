from selenium import webdriver
import time
from Screenshot import Screenshot
from PIL import Image
import os
from selenium.webdriver.common.by import By

'''Refs : 
1. https://www.geeksforgeeks.org/driving-headless-chrome-with-python/
2. https://stackoverflow.com/a/67201242/14202432
3. https://stackoverflow.com/questions/39600245/how-to-capture-website-screenshot-in-high-resolution
'''
options = webdriver.ChromeOptions()
#  We need Chrome to be headless because UI entails CPU and RAM overheads. 
# Headless Chrome is just a regular Chrome but without User Interface(UI)
# options.add_argument('--headless')
# options.add_argument("--window-size=1920x1080")
# options.headless = True
options.add_experimental_option("excludeSwitches", ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

driver.get("https://marblebox.com/")
time.sleep(10)

# driver.maximize_window()

menu = driver.find_element(By.CLASS_NAME, "uabb-hamburger-menu-bottom")
menu.click()
time.sleep(10)

team = driver.find_element(By.CLASS_NAME, "menu-item-text")
location = team.location
size = team.size
team.click()
time.sleep(1)
driver.execute_script("document.body.style.zoom = '35%'")     # ZOOM

# time.sleep(2)

path_to_ss = r"./screenshot"
filename = "full_ss.png"
# ss = Screenshot.Screenshot()
# my_ss = ss.full_Screenshot(driver=driver, save_path = path_to_ss, image_name = filename)
driver.get_screenshot_as_file(filename=os.path.join(path_to_ss,filename))
print(driver.title)
driver.close()
driver.quit()

# image_full_path = path_to_ss + "/" + filename
# im = Image.open(image_full_path)
# left = location['x'] * 2 # must mutliply all these numbers by your zoom
# top = location['y'] * 2
# right = (location['x'] + size['width']) * 2
# bottom = (location['y'] + size['height']) * 2

# im = im.crop((left, top, right, bottom)) # defines crop points
# im.save(fp=f"processed_{filename}", path=path_to_ss)
# im.close()

# saved_path = path_to_ss + "/" + f"processed_{filename}"
# im = Image.open(saved_path)
# im.show()