'''
웹 문서 읽기
import requests

웹 크롤링
'''
import urllib.request as req
from bs4 import BeautifulSoup

# 위치백과 사이트에서 이순신으로 검색된 자료 읽기

# 사이트 https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0
url = "https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0"
wiki = req.urlopen(url)
# print(wiki.read()) # 뒤에를 읽을 려면 주석처리

soup = BeautifulSoup(wiki, 'html.parser') # BeautifulSoup 객체로 만들어줌
# print(soup)

# 페이지 검사 copy selector 
#mw-content-text > div.mw-parser-output > p:nth-child(5)
# print(soup.select("div.mw-parser-output > p")) # p전체

ss = soup.select("div.mw-parser-output > p")
for s in ss:
    if s.string != None:
        print(s.string)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 형식 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
url2 = "https://news.daum.net/society#1"
daum = req.urlopen(url2)
soup2 = BeautifulSoup(daum, 'lxml')
print(soup2.select_one("body > div.direct-link > a").string)
# 본문 바로가기

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ a 링크 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
datas = soup2.select("div.direct-link > a")
print(datas)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 링크, 텍스트 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
for i in datas:
    href = i.attrs['href'] # 링크
    ss = i.string # 텍스트
    print('href:%s, test:%s'%(href, ss))
    
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ for문으로 20번 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
datas = soup2.findAll('a') # a 전부
# print(datas)
for i in datas[:20]:
    href = i.attrs['href']
    ss = i.string
    print('href:%s, test:%s'%(href, ss))
    
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 일정 시간 마다 웹문서 스크래핑 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')

data = soup2.findAll('a') # fond_all
# print(datas)
for i in datas[:20]:
    href = i.attrs['href']
    ss = i.string
    print('href:%s, text:%s'%(href,ss))




