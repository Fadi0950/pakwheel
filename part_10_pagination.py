# //*[@id="main-container"]/section[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[4]/ul/li[7]
from selenium import webdriver  #webdrive module
from webdriver_manager.chrome import ChromeDriverManager    #this will automatic the chrome driver
from selenium.webdriver.common.by import By #By used with selection
from selenium.webdriver.chrome.service import Service   #it resolve the depricated error
from selenium.webdriver.common.keys import Keys #important
from selenium.common.exceptions import NoSuchElementException   #Exception handling
from selenium.common.exceptions import ElementNotInteractableException  #Exception handling
from selenium.webdriver.support.ui import WebDriverWait #used to properly load all web elements
from selenium.webdriver.support import expected_conditions as EC    #dont know what it is used for ?
from selenium.webdriver.support.ui import Select    #to select elements of checkbox
from bs4 import BeautifulSoup   #not important
from selenium.webdriver.common.action_chains import ActionChains    #used for chaining events but not necessary right now
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.pakwheels.com/")
driver.implicitly_wait(10)
print(driver.title)

#//*[@class="btn btn-sm btn-link-outline btn-classified"]
# year_of_model=driver.find_element(By.ID,"home-query").send_keys("2015")
#
# search_button=driver.find_element(By.ID,"home-search-btn")
# search_button.click()
#it will click no filter to find and filter data
driver.find_element(By.XPATH,'//*[@class="btn btn-sm btn-link-outline btn-classified"]').click()

#this block just select from 2015 to 2015
try:


    From_year = driver.find_element(By.ID, "yr_from")

    To_year = driver.find_element(By.ID, "yr_to")
    From_year.send_keys("2015")
    To_year.send_keys("2015")
    Go_ = driver.find_element(By.ID, "yr-go")
    Go_.click()
    #this time.sleep used to proper fetch data after interval of time
    time.sleep(3)
    #this block will select the color white in checkbox
    colour = driver.find_element(By.XPATH, '//div[@id="collapse_16"]/div/ul/li[1]/label/a/input')
    driver.execute_script("arguments[0].click();", colour)
    time.sleep(5)
    #pagination




    data_1=driver.find_elements(By.XPATH,'//div[@class="search-title"]//a/h3')
    print(f"_________________________________Page 1 data___________________________________")
    for i in data_1:
        print(i.text)
    #now adding data to the list data tupe/collection
    # white_cars_2015=[] #empty list
    # for data in data_1:
    #     white_cars_2015.append(data.text)
    # print(white_cars_2015)
    time.sleep(5)
    for j in range(10):


        next_page=driver.find_element(By.XPATH,'//ul/li[@class="next_page"]/a')
        next_page.click()

        time.sleep(5)
        try:
            driver.find_element(By.XPATH,'//*[@id="email_alert_div"]/div/div/div[1]/button').click()
        except:
            print("Skipped............................")
     


      



    
    # print(f"______________________________________________________________Page 2 Data_____________________________________________________________________________")
    # page_2_data=driver.find_elements(By.XPATH,'//div[@class="search-title"]//a/h3')
    # time.sleep(5)
    # for j in page_2_data:
    #     print(j.text)
    # time.sleep(5)



#exception block
except ElementNotInteractableException as e:
    print(f"The Error is:{e} ")

time.sleep(30)