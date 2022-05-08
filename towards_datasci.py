
import re
import requests
# Make the GET request to a url
r = requests.get('https://towardsdatascience.com/')
# Extract the content
c = r.content
from bs4 import BeautifulSoup
# Create a soup object
soup = BeautifulSoup(c, "html.parser")
#print(soup)
print(soup.title)
warning = soup.find_all('div',class_="jo gs gt")
#//*[@id="root"]
print(warning)


