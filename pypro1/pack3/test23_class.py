'''
*** 다시 보기 ***
*** 중요 ***

모듈의 마지막 멤버 class
(변수, 명령, 함수, 클래스)

1. 클래스 : OOP - 자원의 재활용 (포함, 상속 - 다형성 구사)
나의 타입을 만들수 있다

2. 클래스는 새로운 타입을 생성. *****
멤버 -> 멤버변수(필드), 멤버 메소드
- 자바와는 다르게 접근 지정자 x, overloading x

3. 클래스 선언 후 실행하면 객체가 생성 (prototype)

class 사용하는 이유는 ? 
함수 지향적인(중심적인) OOP
'''
print(type(1)) # int 타입 -> 어딘가에 객체가 만들어짐 (이름 공간), 주소를 가지고 있음

print(type([])) # list 타입

print()
print('모듈의 멤버')
a = 1

def func():
    pass

class TestClass: 
    aa = 1 # 멤버 변수(필드), class내에서는 전역변수
    
    def __init__(self): # 특별한 메소드, 하나만 만들수 있음
        print('생성자: 초기화 담당')

    def __del__(self):
        print('소멸자: 마무리 담당') # GC : 필요없는 메모리는 해제시킴\
        
    def myMethod(self):
        name = "신기해" 
        print('클래스 내에 있는 함수를 메소드 : self를 매개변수로 갖는다') # 자바의 this와 유사
        print(name) # 지역변수
        print(self.aa) # 클래스 안에 있는 멤버를 지정할 때
    
print(TestClass.aa, id(TestClass)) # 1 2468958931056(객체로 만들어짐)

print('----- -----')
# TestClass.myMethod() 
print('test는 객체 변수')
test = TestClass() # 생성자를 호출하고 TestClass 타입의 객체가 생성, test가 Testclass의 주소를 기억

print('----- -----')
print(test.aa)
print('----- -----')
test.myMethod()


print('----- 이건 다시보기 -----')
print(TestClass.aa, id(TestClass))
# TestClass.myMethod()

test = TestClass() # 생성자를 호출하고 TestClass 타입의 객체가 생성
print(test.aa)
test.myMethod() # Bound method call
TestClass.myMethod(test) # unBound method call

print('----- -----')
print(type(test)) # <class '__main__.TestClass'> : 내가 만든 타입
print(isinstance(test, TestClass)) # TestClass 이면 True
print(id(test), id(TestClass)) # 1842070256464 1842068574416 : 객체가 2개 만들어짐















