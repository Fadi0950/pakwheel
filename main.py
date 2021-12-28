"""Project Extract the data from pakwheels.com
A-Extract the data from 2015 to 2021 of all white cars
"""
"""commments
Import selenium libray
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import  time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.pakwheels.com/")
# try:
#  cookies = driver.find_element(By.XPATH, '//button[@id="onesignal-slidedown-allow-button"]').click()
# except NoSuchElementException as e:
#     print("Erro_1",e)
year_of_model=driver.find_element(By.ID,"home-query")
year_of_model.click()
year_of_model.send_keys("2015")
search_button=driver.find_element(By.ID,"home-search-btn")
search_button.click()
print("Page___________1")

year_from = driver.find_element(By.ID, 'yr_from')
year_from.send_keys("2015")
year_from.send_keys(Keys.RETURN)



year_to = driver.find_element(By.ID, 'yr_to')
year_to.send_keys("2015")
year_to.send_keys(Keys.RETURN)
clk = driver.find_element(By.ID, 'yr-go')
clk.click()
try:

  colour=driver.find_element(By.XPATH,'//div[@id="collapse_16"]/div/ul/li[1]/label/a/input')
  white_cars=driver.execute_script("arguments[0].click();", colour)

except ElementNotInteractableException as e:
    print(f"The Error is:{e} ")



list_1 = driver.find_elements(By.XPATH, '//div/ul[@class="list-unstyled search-results search-results-mid next-prev car-search-results "]//a/h3')
for title in list_1:
    print(title.text)


time.sleep(30)



