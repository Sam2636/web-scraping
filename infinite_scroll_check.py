
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin


##### Web scrapper for infinite scrolling page #####
#driver = webdriver.Chrome(executable_path=r"E:\Chromedriver\chromedriver_win32_chrome83\chromedriver.exe")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

# starting time
start = time.time()

driver = webdriver.Chrome(ChromeDriverManager().install())

#driver.get("https://opensea.io/collection/art")
driver.get("https://opensea.io/assets?search[categories][0]=art")
driver.maximize_window()
#time.sleep(2)  # Allow 2 seconds for the web page to open
driver.implicitly_wait(2)
scroll_pause_time = 1# You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

urls = []

for j in  range(0,5):

    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1 
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        pass

##### Extract Reddit URLs #####
    #urls = []
    """ soup = BeautifulSoup(driver.page_source, "html.parser")
    for parent in soup.find_all("article",class_="Assetreact__DivContainer-sc-bnjqwy-0 fXNMWi Asset--loaded AssetSearchList--asset "):
    #for parent in soup.find_all(class_="Blockreact__Block-sc-1xf18x6-0 ctiaqU AssetsSearchView--assets"):
        #a_tag = parent.find("a", class_="styles__StyledLink-sc-l6elh8-0 cnTbOd Asset--anchor")
        a_tag = parent.find("a", class_="styles__StyledLink-sc-l6elh8-0 ekTmzq Asset--anchor")
        #styles__StyledLink-sc-l6elh8-0 ekTmzq Asset--anchor
        base = "https://opensea.io/collection/art"
        link = a_tag.attrs['href']
        url = urljoin(base, link)
        urls.append(url) """

    sectio= driver.find_elements_by_xpath("//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq Asset--anchor']")
    if len(sectio)!=0:
        for kl in sectio:    
            sales1=kl.get_attribute("href")
            urls.append(sales1)
            #print(len(sales1))
        print(len(urls))    
print('this is',len(urls))    
#print(urls[0:25])

time.sleep(5)

print ("The original list is : " +  str(urls))
print(len(urls))
# using naive method
# to remove duplicated 
# from list 
res = []
for i in urls:
    if i not in res:
        res.append(i)
  
# printing list after removal 
print ("The list after removing duplicates : " + str(res))
print(len(urls))
print(len(res))
print("the difference between them are:{}".format(len(urls)-len(res)))
print("the percentage between them:{}%".format(len(res)/(len(urls))*100))

driver.quit()
#print(urls)

# end time
end = time.time()

tim= end - start
# total time taken
#print(f"Runtime of the program is {(end - start)/60} minutes")
def run_time(seconds):
    seconds_in_day = 86400
    seconds_in_hour = 3600
    seconds_in_minute = 60


    days = seconds // seconds_in_day
    seconds = seconds - (days * seconds_in_day)

    hours = seconds // seconds_in_hour
    seconds = seconds - (hours * seconds_in_hour)

    minutes = seconds // seconds_in_minute
    seconds = seconds - (minutes * seconds_in_minute)

    print("{0:.0f} days, {1:.0f} hours, {2:.0f} minutes, {3:.0f} seconds.".format(days, hours, minutes, seconds))

run_time (float(tim)) 