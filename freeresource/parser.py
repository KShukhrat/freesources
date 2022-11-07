import requests
from bs4 import BeautifulSoup

#rutracker.org
def url(link = 'https://rutracker.org/forum/'):
    return f'https://rutracker.org/forum/{link}'
link = url('viewforum.php?f=1556')
res = requests.get(link)
soup = BeautifulSoup(res.content, 'lxml')


def category_list():
    cat = soup.findAll('td', class_='pad_4')
    for i in cat:
        cat_name = i.text.strip() #cat name
        try:
            cat_link = i.a.attrs['href'] #cat url
        except:
            pass
        if cat_name != "":
            category = url(cat_link)#Разное (Компьютерные видеоуроки)
    return category
# print(category_list())
def pages():#pages
    page = 0
    pages=[]
    while True:
        if page == 0:
            s = category_list() + f'&start={page}'
            pages.append(s)
            page += 50
        elif page > 0:
            s = category_list() + f'&start={page}'
            pages.append(s)
            page += 50
        if page > 800:
            break
    return pages
#https://rutracker.org/forum/viewforum.php?f=1567&start=50
alc={}
courses_links=[]
for l in pages():
    link = l
    res = requests.get(link)
    soup = BeautifulSoup(res.content, 'lxml')
    name_list = soup.findAll('a', class_='torTopic bold tt-text')
    for m in name_list:
        name_list = m.text.strip()#name
        course_link = m.attrs['href']#link name list
        alc.update({name_list: course_link})
        if course_link not in courses_links:
            courses_links.append(course_link)
for cl in courses_links:
    link = url(cl)
    res = requests.get(link)
    soup = BeautifulSoup(res.content, 'lxml')
    name_list = soup.find('span', class_='post-b')
    print(name_list.text)
    # for m in name_list:
    #     print(m.text.strip())
# https://rutracker.org/forum/viewtopic.php?t=3180116

