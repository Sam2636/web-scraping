from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#Create new instance of Chrome in Incognito mode
option = webdriver.ChromeOptions()
option.add_argument(" — incognito")


#creating new instance of the chrome
#browser = webdriver.Chrome(executable_path='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome', chrome_options=option)

#browser request
driver.get("https://rarible.com/")


# Wait 20 seconds for page to load
timeout = 20
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "https://img.rarible.com/prod/image/upload/prod-itemImages/0x60f80121c31a0d46b5279700f9df786054aa5ee5:1134816" )))
except TimeoutException:
    print("Timed out waiting for page to load")
    driver.quit()
    
# find_elements_by_xpath returns an array of selenium objects.
titles_element = driver.find_elements_by_xpath("//a[@class=’text-bold’]")
# use list comprehension to get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_element]
# print out all the titles.
print('titles:')
print(titles, '\n')
    

#image class
# /html/body/div/div[2]/div[2]/div[2]/div/div/div/div[8]/div[2]/div/div[2]/div/div[3]/div/div[2]/div[2]/div
#to print a tag ,img src tag