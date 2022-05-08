import time
import json
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#website 
#driver.get('https://opensea.io/collection/art')
#driver.get('https://opensea.io/assets/0x7645eec8bb51862a5aa855c40971b2877dae81af/2720')
#driver.get('https://opensea.io/assets/0x8d04a8c79ceb0889bdd12acdf3fa9d207ed3ff63/15')

#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/73421096514701913038321027627106130670963264759533318575472723461417792962561')
#s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/40482595849772694285173713041642282097106100196042549765489074297924826955777')
s=driver.get('https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/34085485605809858234645056736246100833627908360907625323341299738449415241729')
driver.maximize_window()
#get title
time.sleep(3)

print("--->title",driver.title)


""" #/html/body/div/div[1]/main/div/div/div[2]/div/div/div[1]/aside/div/div[2]/div/div/div/div/div[2]/div[1]/section/div/div/input
driver.execute_script("window.scrollBy(0,300)","")
obj=driver.find_element_by_xpath("//input[@placeholder='Min']")
s=obj.send_keys("1.25")
obj=driver.find_element_by_xpath("//input[@placeholder='Max']")
s=obj.send_keys("3.25")
 """
#button
#//button[@class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 cWgiBW kaikhX ActionButtonreact__StyledButton-sc-7jpoey-0 bwNKOH']
#//button[@class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 mFlni iZpARs']
#apply=driver.find_element_by_xpath("//button[@class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 mFlni iZpARs']")
#//button[@class="Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 mFlni iZpARs"]
#apply=driver.find_element_by_xpath("//button[@class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 mFlni iZpARs']")
#driver.implicitly_wait(5)
time.sleep(2)
apply=driver.find_element_by_xpath("//i[@class='Iconreact__Icon-sc-1gugx8q-0 irnoQt Pill--delete material-icons Pill--delete']")
apply.click()


action =ActionChains(driver)

action.double_click(on_element = apply)


    #clear_all
try:    
    """ apply=driver.find_element_by_xpath("//div[@class='Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 dBFmez jYqxGr ksFzlZ iXcsEj']")
    apply.click()
    # <div class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 dBFmez jYqxGr ksFzlZ iXcsEj" bis_skin_checked="1"><button type="button" class="UnstyledButtonreact__UnstyledButton-sc-ty1bh0-0 btgkrL"><li class="EventHistory--filter-dropdown-clear">Clear All</li></button></div>
    driver.implicitly_wait(10) """
    apply=driver.find_element_by_xpath("//div[@class='Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 dBFmez jYqxGr ksFzlZ iXcsEj']")
    action =ActionChains(driver)
    action.click(on_element = apply)

    
    print("cleared_all")

except :
    pass
    print("no_clear_option")

driver.quit()

""" #click first image
for i in range(5):
    first_image=driver.find_element_by_xpath("//article[@class='Assetreact__DivContainer-sc-bnjqwy-0 gwTKfX Asset--loaded AssetSearchList--asset']")
    s=first_image.click()
    time.sleep(3)
    driver.execute_script("window.history.go(-1)") #come backs to the original page
    time.sleep(2)

 """
""" 
 
#1 &2    ------------------>#working 
sectio= driver.find_elements_by_xpath("//div[@class='TradeStation--main']")
#//div[@class='item--frame']
#//section[@class='Blockreact__Block-sc-1xf18x6-0 Framereact__Frame-sc-139h1ex-0 fAtwh eoqSMa']
print(len(sectio))
if len(sectio)!=0:
    for i in sectio:
        sales1=i.text.splitlines()
        #print(i.text)
        time.sleep(3) 
        print(sales1)
else:
    sales1=[0,0,0,0]              
    #print('this is not workng',) 



#sales ends in ---------------------->working
sect= driver.find_elements_by_xpath("//div[@class='TradeStation--header']")
if len(sect)!=0: 
    #print(sales)
    for i in sect:
        sales=i.text.splitlines()
        print(sales)
    #print(i.text)
    time.sleep(3)  
else:
    sales=[0,0,0,0]     

 """
""" #image_url
image_url=[]
#line=input()
while True:
    driver.execute_script("window.scrollBy(0,50)","")
    
    obj = driver.find_elements_by_xpath("//img[@class='Image--image']")
    for i in obj:
        img_src=i.get_attribute("src")
        image_url.append(img_src)
        print(img_src) """

""" if input()=='q':
        break  """
       