from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

binary = r'C:/Program Files/Mozilla Firefox/firefox.exe\\'
options = Options()
options.add_argument("--headless")
Options.binary = binary
cap = DesiredCapabilities().FIREFOX 
cap["marionette"] = True #optional 
#driver = webdriver.Firefox(firefox_options=options, capabilities=cap, executable_path=r"C:\Users\sam\Downloads\geckodriver-v0.30.0-win64")
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


driver.get("http://google.com/")
print ("Headless Firefox Initialized")
driver.quit()