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
print(driver.title)


year_of_model=driver.find_element(By.ID,"home-query")

year_of_model.send_keys("2015")
search_button=driver.find_element(By.ID,"home-search-btn")
search_button.click()
try:
    From_year = driver.find_element(By.ID, "yr_from")

    To_year = driver.find_element(By.ID, "yr_to")
    From_year.send_keys("2015")
    To_year.send_keys("2015")
    go = driver.find_element(By.ID, "yr-go").click()

    # colour = driver.find_element(By.XPATH, '//div[@id="collapse_16"]/div/ul/li[1]/label/a/input')
    # white_cars = driver.execute_script("arguments[0].click();", colour)

except ElementNotInteractableException as e:
    print(f"The Error is:{e} ")

time.sleep(30)