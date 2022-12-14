import os
import django
import export as export
import requests
from bs4 import BeautifulSoup
import rateMyProfessor
from rateMyProfessor import settings
import sqlite3

# url = "https://directory.ccsu.edu/"

os.environ['DJANGO_SETTINGS_MODULE'] = 'rateMyProfessor.settings'
django.setup()

from base.models import Professor, Subject, Courses

url = "https://directory.ccsu.edu/?name=&field_taxonomy_target_id&page="

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept-Language": "en",
}




# For Professors

# for i in range(0, 34):

# stringi = str(i)
# newurl = url + stringi
# r = requests.get(newurl, headers=headers)

# soup = BeautifulSoup(r.text, "lxml")
# print(soup.prettify())

# name = soup.select(selector=".full-name")
# title = soup.select(selector=".profile-department")
# classname = soup.select(selector=".name")
# image = soup.select(selector=".profile-img")

# print(newtitle.getText())
# if title == "Professor" or title == "Associate Professor":

# o = 0
# for j in name:
#     newtitle = title[o].find("div", {"class": "title"})
#     if 'Professor' in newtitle.getText() or 'Lecturer' in newtitle.getText():
#         picture = image[o].find("img")
#         imageurl = "https://directory.ccsu.edu" + picture.attrs['src']
#         professor = Professor(name=name[o].getText(), department=classname[o].getText(), picture=imageurl)
#         professor.save()
#     o = o + 1




# For Departments (Best Option) Requires a file-departments.txt

# url = "/Users/andy/Desktop/departments.txt"
# page = open(url)
# soup = BeautifulSoup(page.read(), "lxml")
# # print(soup.prettify())
#     # soup = BeautifulSoup(fp, 'html.parser')
#     # r = requests.get(url, headers=headers)
# #     soup = BeautifulSoup(fp, "lxml")
# #
# subjects = soup.select(selector=".subj_id")
# # print(subjects)
# subjects = subjects[0].find_all("option")
#
# p = 0
# for s in subjects:
#     subjecta = s.getText()
#     course = Subject(subject=subjecta)
#     course.save()
#     # print(subjecta)
#     p = p + 1







# For Departments from a different ccsu website

# url = "https://www2.ccsu.edu/academics/undergrad"
# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.text, "lxml")
#
# subjects = soup.select(selector=".program_listing")
# print(subjects)
# subjects = subjects[0].find_all("span", {"class": "program_name"})

# p = 0
# for s in subjects:
#     subjecta = subjects[p].getText()
#     subjecta = subjecta.replace(' BA', '')
#     subjecta = subjecta.replace(' BS', '')
#     subjecta = subjecta.replace(' BFA', '')
#     subjecta = subjecta.replace(' BGA', '')
#     course = Subject(subject=subjecta)
#     course.save()
#     # print(subjecta)
#     p = p + 1




# For Departments from another different ccsu website

# url = "https://ccsu.smartcatalogiq.com/en/current/Undergraduate-Graduate-Catalog/Undergraduate-Majors"
# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.text, "lxml")
#
# subjects = soup.select(selector=".sc-childlinks")
# subjects = subjects[0].find_all("p")
#
# p = 0
# for s in subjects:
#     subjecta = subjects[p].getText()
#     subjecta = subjecta.replace(', B.A.', '')
#     subjecta = subjecta.replace(', B.S.', '')
#     course = Subject(subject=subjecta)
#     course.save()
#     # print(subjecta)
#     p = p + 1






# For Courses

# url = "http://ccsu.smartcatalogiq.com/en/current/Undergraduate-Graduate-Catalog/All-Courses"
# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.text, "lxml")
#
# subjects = soup.select(selector=".sc-child-item-links")
# subjects = subjects[0].find_all("a", href=True)
#
# urls = ["http://ccsu.smartcatalogiq.com"] * 129
#
# # for i in range(0, 127):
# for i in range(0, 128):
#     newstring = str(subjects[i].get("href"))
#     urls[i] = urls[i] + newstring
#     r = requests.get(urls[i], headers=headers)
#     soup = BeautifulSoup(r.text, "lxml")
#
#     classes = soup.select(selector=".sc-course-list")
#     classes = classes[0].find_all("a")
#
#     w = 0
#     for c in classes:
#         course = Courses(course=classes[w].getText())
#         course.save()
#         # print(classes[w].getText())
#         w = w + 1


