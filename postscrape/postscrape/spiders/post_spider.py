from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.ccsu.edu/cs/faculty.html')
soup = BeautifulSoup(source.text, 'html.parser')


teachers = soup.find('div', id="facultyStaffList").find_all('div', class_="name")
print(len(teachers))