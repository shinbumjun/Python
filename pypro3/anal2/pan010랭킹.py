'''
네이버 제공 영화 랭킹 읽기
(html읽기)
'''
from bs4 import BeautifulSoup

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 방법 1 : urllib.request ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
import urllib.request

url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
data = urllib.request.urlopen(url)

soup = BeautifulSoup(data, 'lxml')

# print(soup.select("div.tit3")) # div의 class tit3
# print(soup.select("div[class=tit3]"))
# print(soup.find_all("div",{'class':'tit3'}))
print(soup.findAll("div",{'class':'tit3'}))

for tag in soup.findAll("div",{'class':'tit3'}):
    print(tag.text.strip())

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 방법 2 : requests ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
import requests
data = requests.get(url).text
soup2 = BeautifulSoup(data, 'lxml') # BeautifulSoup 객체 생성
m_list = soup2.find_all('div', 'tit3')

# print(m_list)
count = 1
for i in m_list:
    title = i.find('a')
    print(str(count)+"위:" + title.string)
    count += 1



