import time
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#website 
driver.get('https://opensea.io/collection/art')

driver.maximize_window()
#get title
time.sleep(10)

#min value
#/html/body/div/div[1]/main/div/div/div[2]/div/div/div[1]/aside/div/div[2]/div/div/div/div/div[2]/div[1]/section/div/div/input
driver.execute_script("window.scrollBy(0,300)","")
obj=driver.find_element_by_xpath("//input[@placeholder='Min']")
s=obj.send_keys("1.25")
obj=driver.find_element_by_xpath("//input[@placeholder='Max']")
s=obj.send_keys("3.25")

#button
#//button[@class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 cWgiBW kaikhX ActionButtonreact__StyledButton-sc-7jpoey-0 bwNKOH']
#//button[@class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 fAtwh kaikhX ActionButtonreact__StyledButton-sc-7jpoey-0 bwNKOH']
apply=driver.find_element_by_xpath("//button[@class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 fAtwh kaikhX ActionButtonreact__StyledButton-sc-7jpoey-0 bwNKOH']")
s=apply.click()