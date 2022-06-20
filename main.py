from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

from dotenv import load_dotenv
import os

load_dotenv() 

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD =  os.getenv('EMAIL_PASSWORD')


# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



driver.set_window_position(2000, 0)
driver.maximize_window()



driver.get('https://www.linkedin.com/jobs/search/?f_E=4&f_WT=2&keywords=react%20developer&location=Bogota%2C%20D.C.')

# Sign in section:

sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()


email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(EMAIL_ADDRESS)

password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(EMAIL_PASSWORD)
password_field.send_keys(Keys.ENTER)
# driver.quit()


# list jobs

# all_listings = driver.find_element(by=By.CSS_SELECTOR, value=".occludable-update")
# all_listings=[]
# all_listings = driver.find_element(By.CSS_SELECTOR, ".job-card-container--clickable")
content=[]
content = driver.find_element(By.CLASS_NAME, 'job-card-container')

# print("🚀 ~ ", type(content))
# print("🚀 ~ ", content)
for e in content:
    print("🚀 ~ ", e)



# for listing in all_listings:
#     print("called")
#     listing.click()
#     time.sleep(2)

