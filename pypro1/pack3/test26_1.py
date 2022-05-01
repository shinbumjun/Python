'''
Singer 타입의 객체
abc 라는 가수 객체

class는 새로운 타입을 만든다 

자원의 재활용 : has a(포함), is a(상속)

[참고]
Class 다이어그램
sequence 다이어그램
Use Case 다이어그램

~알고리즘 강조~
'''
import pack3.test26_class

def process():  
    abc = pack3.test26_class.Singer() # import.Singer()
    print('타이틀 송:', abc.title_song) # 타이틀 송: 화이팅 코리아
    abc.sing() # 노래는  화이팅 코리아 랄라라 ~~~
    abc.hello() # 안녕하세요 저는 가수예요~
    
if __name__ == '__main__': # 여기가 메인이 맞으면 실행
    process()










