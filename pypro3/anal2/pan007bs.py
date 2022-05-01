'''
BeautifulSoup 객체의 find(), select() 연습

[중요]웹 크롤링
'''
from bs4 import BeautifulSoup

html_page = """
<html>
<body>
<h1>제목 태그</h1>
<p>웹문서 읽기</p>
<p>파이썬 라이브러리 사용</p>
</body>
</html>
"""
print(html_page, type(html_page)) # 문자열 : str

soup = BeautifulSoup(html_page, 'html.parser') # BeautifulSoup 객체 생성
print(soup, type(soup)) # bs4.BeautifulSoup

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ html(웹) 읽기 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
h1 = soup.html.body.h1
print(h1) # <h1>제목 태그</h1>
print('h1:', h1.string) # h1: 제목 태그

p1 = soup.html.body.p
print(p1) # <p>웹문서 읽기</p>
print('p1:', p1.text) # p1: 웹문서 읽기

p2 = p1.next_sibling.next_sibling
print(p2) # <p>파이썬 라이브러리 사용</p>

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ find() 사용 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
html_page2 = """
<html>
<body>
<h1 id="title">제목 태그</h1>
<p>웹문서 읽기</p>
<p id="my" class="our">파이썬 라이브러리 사용</p>
</body>
</html>
"""
soup2 = BeautifulSoup(html_page2, 'lxml') # BeautifulSoup 객체 생성
print(soup2.p, ' ', soup2.p.string) # 직접 최소 p tag 선택
print(soup2.find('p').string) # 웹문서 읽기
print(soup2.find('p', id='my').string) # id를 찾아가서 읽음 -> 파이썬 라이브러리 사용

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ id, class,attrs를 이용하여 찾기 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# print(soup2.find(['p', 'h1'])) # <h1 id="title">제목 태그</h1>
print(soup2.find(id='my').string) # 파이썬 라이브러리 사용
print(soup2.find(id='title').string) # 제목 태그
print(soup2.find(class_='our').string) # 파이썬 라이브러리 사용
print(soup2.find(attrs={'class':'our'}).string) # 파이썬 라이브러리 사용
print(soup2.find(attrs={'id':'title'}).string) # 제목 태그

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ find_all(), findAll() 사용 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
html_page3 = """
<html>
<body>
<h1 id="title">제목 태그</h1>
<p>웹문서 읽기</p>
<p id="my" class="our">파이썬 라이브러리 사용</p>
<div>
  <a href="https://www.naver.com">네이버</a>
  <a href="https://www.daum.net">다음</a>
</div>
</body>
</html>
"""
soup3 = BeautifulSoup(html_page3, 'lxml') # BeautifulSoup 객체 생성, 해석기
print(soup3.find_all(['a'])) # a태크 전부 가져오기
print(soup3.find_all('a')) # a태크 전부 가져오기

print(soup3.find_all(['a','p'])) # a,p태그 전부 가져오기
print(soup3.findAll(['a','p'])) # a,p태그 전부 가져오기

links = soup3.find_all('a')
for i in links:
    href = i.attrs['href'] # 링크
    text = i.string # 텍스트
    print(href, ' ', text)
# https://www.naver.com   네이버
# https://www.daum.net   다음

print()
import re
links2 = soup3.find_all(href=re.compile(r'^https')) # 정규 표현식
print(links2)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 셀렉터(css의 secletor) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
html_page4 = """
<html>
<body>

<div>
    first div
</div>

<div id="hello">
    <b>파이썬 만세</b>
    <a href="https://www.kbs.com">kbs</a>
    <a href="https://www.mbs.com">mbc</a>
    <span>
        <a href="https://www.tvn.com">tvn</a>
    </span>
</div>

<span>
    <a href="https://www.mbs.com">mbc</a>
</span>

<ul class="world">
    <li>안녕</li>
    <li>반가워</li>
</ul>

<div id="hi" class="good">
    second div
    <a href="https://www.ytn.com">ytn</a>
</div>

</body>
</html>
"""
soup4 = BeautifulSoup(html_page4, 'lxml') # BeautifulSoup 객체 생성, 해석기

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ aa')
aa = soup4.select_one("div") # 첫번째로 오는 div 전체 출력
print(aa)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ bb')
bb = soup4.select_one("div#hello") # div id="hello" 전체 출력
print(bb)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ cc')
cc = soup4.select_one("div#hello > a") # div태크안에 a태크 하나만 
print(cc.string) # cc의 텍스트 출력

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ dd')
dd = soup4.select("div#hello > a") # 복수 선택 (자녀)
print(dd)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ ee')
ee = soup4.select("div#hello a") # 복수 선택 (자녀, 자손)
print(ee)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ ff')
ff = soup4.select("ul.world > li") # ul의 class = "world" -> li출력 
for k in ff:
    print("li : ", k.string)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ ')
msg = list() # msg = []
for k in ff:
    msg.append(k.string)
    
import pandas as pd
df = pd.DataFrame(msg, columns=['자료'])
print(df)




