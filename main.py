from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

driver_path = '/home/camiro/Documents/python/Selenium/chromedriver'

driver = webdriver.Chrome(driver_path, options=options)


driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)


driver.get('https://www.linkedin.com/jobs/search/?f_E=4&f_WT=2&keywords=react%20developer&location=Bogota%2C%20D.C.')

# Sign in section:
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

email_field = driver.find_element_by_id("username")
email_field.send_keys(EMAIL_ADDRESS)

password_field = driver.find_element_by_id("password")
password_field.send_keys(EMAIL_PASSWORD)
password_field.send_keys(Keys.ENTER)
# driver.quit()

