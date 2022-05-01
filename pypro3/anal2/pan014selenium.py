'''
6. 이클립스 또는 jupyter notebook으로 실행해 보기  : 화면 캡처
셀레니움으로 브라우저를 띄워 제어를 할 수 있다

Run하면 daum_img.png 생성(스크린샷)
'''

from selenium import webdriver
 
try:
    url = "https://www.daum.net"
    browser = webdriver.Chrome('C:/work/chromedriver') # 브라우저 열기
    browser.implicitly_wait(3) # 선택적인 명령으로 지정한 시간(초)동안 기다린다
 
    browser.get(url); # 원하는 url을 적어 줌. 해당 사이트가 열린다
    browser.save_screenshot("daum_img.png") # 스크린샷
    browser.quit() # 모든 작업을 끝내고 브라우저를 닫음
    
    print('성공')

except Exception:
    
    print('에러')
    
    
    
    
    
    
    
    
    
    