'''
class
'''
kor = 100

def abc():
    print('함수라고 해')
    
class MyClass:
    kor = 90 # 멤버 변수
    
    def abc(self):
        print('난 메소드야') # 멤버 메소드
    
    # class 멤버는 self로 찍어야한다 
    # 그것이 아니라면 모듈 전체로 본다
    def show(self):
        # kor = 88
        print(self.kor) # self는 MyClass의 kor=90를 참조한다
        print(kor) # 메소드 내에 지역변수를 찾는다, 메소드 내에 변수가 없으면 모듈의 멤버로 가서 kor = 100인 된다
        self.abc() # 난 메소드야, self -> 클래스의 메소드를 호출
        abc() # 함수라고 해, 모듈의 평션을 호출
        
my = MyClass()
my.show()
# 90
# 100
# 난 메소드야
# 함수라고 해

print('----- -----')
class OurClass:
    a = 1

print(OurClass.a) # 1

our1 = OurClass()
print(our1.a) # 1

our2 = OurClass()
print(our2.a) # 1

our2.b = 2 # 객체가 생성괸 our2의 b에 2를 주입
print(our2.b) # 2

# print(our1.b) # 에러


























