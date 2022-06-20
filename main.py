from selenium import webdriver

import time

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = '/home/camiro/Documents/python/Selenium/chromedriver'

driver = webdriver.Chrome(driver_path, options=options)


# Iniciarla en la pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)

# Inicializamos el navegador
driver.get('https://www.linkedin.com')
driver.quit()