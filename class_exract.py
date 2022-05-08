#method 1

""" import urllib.request
from bs4 import BeautifulSoup as BS

html = urllib.request.urlopen("https://rarible.com/").read()

soup = BS(html)

print (soup.findAll(tag_name).get_text()) """


#method 2

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as BS

req = Request('https://rarible.com/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read() 
soup = BS(webpage,"html.parser")

#print (soup.findAll('').get_text())

for el in soup.find_all('a', attrs={'class': 'sc-dlnjwi sc-hKFxyN dJXsSm jvuNlF'}):
    print ( el.get_text())
""" 
<span data-address="0x4da48ac48b782a7c01e70065e4a51faf2c3f7b09" title="0x4da48ac48b782a7c01e70065e4a51faf2c3f7b09" class="sc-dlnjwi sc-hKFxyN dJXsSm jvuNlF">LIRONA</span>


 """




#method 3

""" import urllib.request
from bs4 import BeautifulSoup
#from urllib import urlopen
import re

webpage = urllib.request.urlopen('https://rarible.com/').read
findrows = re.compile('<tr class="- banding(?:On|Off)>(.*?)</tr>')
findlink = re.compile('<a href =">(.*)</a>')

row_array = re.findall(findrows, webpage)
links = re.finall(findlink, webpate)

print(len(row_array))

iterator = [] """

#mehod 4 with amazon
""" from urllib.request import Request, urlopen

req = Request('https://www.amazon.in/events/greatfreedomsale/?tag=msn2020deskstd1-21', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()  """

#method 5
""" import urllib.request
from bs4 import BeautifulSoup as BS

html = urllib.request.urlopen("https://www.amazon.in/events/greatfreedomsale/?tag=msn2020deskstd1-21").read()

soup = BS(html)

print (soup.findAll(tag_name).get_text())  """