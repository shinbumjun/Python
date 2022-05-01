'''
class는 새로운 타입을 만든다.

[그림 설명]
가수 : 노래를 부른다
    타이틀
    성향
    ...
    
가수 A, 가수 B, 가수 C
가수의 덕목을 가져야한다

D를 만들어서 import 

행위만 있으면 함수
속성과 행위로 구성 -> 메소드, 멤버 필드 -> class로 만들어야 한다

이 세상에 없는 새로운 가수라는 타입은 내가 직접 만들고 불러다가 사용하면 된다
'''
print('가수라면 갖춰야 하는 덕목')
class Singer():
    title_song = '화이팅 코리아' # 멤버 변수 : 속성
    
    def sing(self): # 메소드 : 행위
        msg = '노래는 '
        print(msg, self.title_song, '랄라라 ~~~')

    def hello(self): # 메소드 : 행위
        print('안녕하세요 저는 가수예요~')

'''
---------- 정리 ---------- 
아래 내용은 별도의 모듈을 만들었다 가정

'''

print('----- bts -----')
bts = Singer()
bts.hello() # 출력) 안녕하세요 저는 가수예요~
bts.sing() # 출력) 노래는  화이팅 코리아 랄라라 ~~~

print()
print('----- 블랙핑크 -----')
blackpink = Singer() # 생성자로 호출
blackpink.hello() # 출력) 안녕하세요 저는 가수예요~
blackpink.sing() # 출력) 노래는  화이팅 코리아 랄라라 ~~~
blackpink.title_song = '마지막처럼' # 생성된 객체에 title_song을 마지막처럼으로 변경
blackpink.sing() # 출력) 노래는  마지막처럼 랄라라 ~~~
blackpink.co = 'SM' # 생성된 객체에 필드 추가
print('blackpink 소속사 :', blackpink.co) # 출력) blackpink 소속사 : SM

# print('bts 소속사:', bts.co) # blackpink 에만 넣었기 때문에 사용 불가
bts.sing() # 출력) 노래는  화이팅 코리아 랄라라 ~~~

print('----- 둘의 주소는 다르다 -----')
print(id(bts), id(blackpink))
print('----- 타입은 Singer로 같다 -----')
print(type(bts), type(blackpink)) 



















