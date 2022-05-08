import urllib
# urlretrieve
from selenium import webdriver
import time
import json

driver = webdriver.Firefox(executable_path=r"C:/Users/sam/Desktop/geckodriver.exe")
#driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/50238513169613623414318316929603473828187640181229633390544894734653443801089')
#website
driver.get('https://opensea.io/')

driver.maximize_window()
#get title
print("--->title",driver.title)

obj = driver.find_elements_by_xpath("//img[contains(@src,'')]")
for i in obj:
    img_src=i.get_attribute("src")
    time.sleep(2)
    print(img_src)
