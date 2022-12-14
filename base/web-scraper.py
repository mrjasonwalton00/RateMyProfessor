import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/andy/Desktop/chromedriver.exe')
driver.get('https://www.ccsu.edu/cs/faculty.html')
results = []
content = driver.page_source
soup = BeautifulSoup(content)
print(soup.prettify())

# for element in soup.find_all(attrs='name'):
#     name = element.find('div')
#     if name not in results:
#         results.append(name.text)
# print(results)