'''
BeautifulSoup : HTML. XML 문서의 자료를 효율적으로 추출

BeautifulSoup 사용 방법 및 웹 문서 스크랩핑

https://cafe.daum.net/flowlife/RUrO/42
'''
from bs4 import BeautifulSoup

# ** 아래 소스 코드는 2021년 11월 현재 가능 코드임 - contents가 계속 변화함을 잊지 말자. **
# 간단 예제1)

import requests  

from bs4 import BeautifulSoup

def go():
    base_url = "http://www.naver.com:80/index.html"

    #storing all the information including headers in the variable source code
    source_code = requests.get(base_url)

    #sort source code and store only the plaintext
    plain_text = source_code.text

    #converting plain_text to Beautiful Soup object so the library can sort thru it
    convert_data = BeautifulSoup(plain_text, 'lxml')

    for link in convert_data.findAll('a'):
        href = base_url + link.get('href')  #Building a clickable url
        print(href)                          #displaying href
 
go()





