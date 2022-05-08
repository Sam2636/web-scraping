import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
from urllib.parse import urljoin

driver = webdriver.Chrome(ChromeDriverManager().install())

#driver = webdriver.Chrome(executable_path=r"E:\Chromedriver\chromedriver_win32_chrome83\chromedriver.exe")
driver.get("https://opensea.io/collection/art")

time.sleep(2)  # Allow 2 seconds for the web page to open
scroll_pause_time = 3 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

#while True:
for j in range(0,15):
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break 


    urls = []
    soup = BeautifulSoup(driver.page_source, "html.parser")

    for parent in soup.find_all(class_="Assetreact__DivContainer-sc-bnjqwy-0 gwTKfX Asset--loaded AssetSearchList--asset"):
        a_tag = parent.find("a", class_="styles__StyledLink-sc-l6elh8-0 cnTbOd Asset--anchor")
        base = "https://opensea.io/collection/art"
        link = a_tag.attrs['href']
        url = urljoin(base, link)
        urls.append(url)

print(urls)  
print(len(urls))  