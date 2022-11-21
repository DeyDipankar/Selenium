from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options() 
chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=3200x20800") # ANYTHING MORE THAN 3200 width my pycharm cant cope (Rendering error)

driver = webdriver.Chrome(options=chrome_options, executable_path=r"./") # webdriver.Chrome(options=options)
outFileName = (r'./')
driver.maximize_window()

URL = "https://marblebox.com/"

driver.get(URL) #time.sleep(0.5)
#driver.maximize_window()

driver.get_screenshot_as_file(outFileName+"/"+"capture4.png")

driver.quit()