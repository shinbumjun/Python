'''
# Pool 클래스로 웹 스크래핑

# 멀티 프로세싱을 위한 웹 스크래핑 
# 멀티 프로세싱 x
# https://beomi.github.io/beomi.github.io_old/ 사이트에 컨텐츠를 scraping
'''
import requests # 특정 사이트의 웹 문서를 읽기 위한 모듈 로딩
from bs4 import BeautifulSoup as bs # 읽어 온 웹 문서를 처리하기 위한 모듈 로딩
import time # 지연시간

from multiprocessing import Pool

def get_link(): # 제목 atag 읽기, 특정 사이트와 연결을 위해 링크된 a 태그의 URL을 가져오기 위한 함수
    data = requests.get("https://beomi.github.io/beomi.github.io_old/").text
    soup = bs(data, 'html.parser')
    my_titles = soup.select('h3 > a')

    data = []
    
    for title in my_titles:
        data.append(title.get('href'))
        
    return data

def get_content(link): # get_link 함수에서 전달 받은 url로 접속해 제목 읽기 함수
    # print(link)
    abs_link = 'https://beomi.github.io' + link
    #print(abs_link)
    data = requests.get(abs_link).text
    soup = bs(data, 'html.parser') # 가져온 데이터로 처리 작업 (그러나 여기에서는 그저 처리 소요 시간이 궁금)
    # 가져온 데이터로 뭔가를 할 수 있다. ...
    print(soup.select('h1')[0].text)  # 첫번째 h1 태그의 텍스트 하나만 출력
    
if __name__ == '__main__':
    startTime = time.time()
    
    # 1) 멀티 프로세싱 x -> 1.4
    # print(get_link()) # 출력
    # print(len(get_link())) # 26(총 몇개를 가져왔는지)
    for link in get_link():
         get_content(link)
    
    # 2) 멀티 프로세싱 o, 병렬처리 -> 0.9
#    pool = Pool(processes = 4) # 4개의 프로세스 사용
#    pool.map(get_content, get_link()) # 링크의 갯수만큼 컨텐츠를 받는다, 함수와 인자값을 매핑하면서 처리
         
    print('---%s 초 ---'%(time.time() - startTime)) # 멀티 프로세싱x, 멀티 프로세싱o 시간 비교해보기~



