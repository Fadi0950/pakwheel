from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.pakwheels.com/")
print(driver.title)
year_of_model=driver.find_element(By.ID,"home-query")

year_of_model.send_keys("2015")
search_button=driver.find_element(By.ID,"home-search-btn")
search_button.click()
try:
    search_result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "used-car-search-results"))
    )
    # print(search_result.text)
    try:
        car_list = search_result.find_elements(By.XPATH,'//div/ul[@class="list-unstyled search-results search-results-mid next-prev car-search-results "]//a/h3')
        for car in car_list:
            print(car.text)
        # break
    except NoSuchElementException:
        print('No element of that id present!')

finally :
    driver.quit()

driver.quit()