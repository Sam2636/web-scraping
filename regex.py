# requests for fetching html of website
import re
import requests
# Make the GET request to a url
r = requests.get('http://www.cleveland.com/metro/index.ssf/2017/12/case_western_reserve_university_president_barbara_snyders_base_salary_and_bonus_pay_tops_among_private_colleges_in_ohio.html')
# Extract the content
c = r.content
from bs4 import BeautifulSoup
# Create a soup object
soup = BeautifulSoup(c, "html.parser")
#print(soup)


# Find the element on the webpage
main_content = soup.find('div', attrs = {'class': 'entry-content'})

# Extract the relevant information as text
content = main_content.find('ul').text

#print(content)

# Create a pattern to match names
name_pattern = re.compile(r'^([A-Za-z].+?)(?:,)', flags = re.M)
# Find all occurrences of the pattern
names = name_pattern.findall(content)


print(names)

# Make school patttern and extract schools
school_pattern = re.compile(r'(?:,|,\s)([A-Z]{1}.*?)(?:\s\(|:|,)')
schools = school_pattern.findall(content)
print (schools)
# Pattern to match the salaries
salary_pattern = re.compile(r'[$]\d{3}.\d{3}')
salaries = salary_pattern.findall(content)


print(salaries)