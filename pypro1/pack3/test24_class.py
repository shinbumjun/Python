'''
*** 중요 - 구체적으로 ***
class : 메소드(함수)나 변수 등을 포함한 별도의 집합체(객체, 개체, Object) - 객체 중심의 프로그래밍이 가능  
'''
from scipy.constants.constants import carat
class Car: 
    handle = 0 # 클래스 안의 전역변수
    speed = 0

    def __init__(self, name, speed): # 생성자가 name, speed을 받음
        self.name = name
        self.speed = speed # speed 지역변수
        
    def showData(self):
        km = '킬로미터'
        msg = '속도: ' + str(self.speed) + km + " 확인한 사람 :" + self.name # 속도: speed 킬로미터
        return msg

print('----- 원형 클래스의 멤버를 출력. prototype 값 출력 -----')
print(Car.handle) 

print('----- 1. 새롭게 만들어진 객체-----')
car1 = Car('tom', 10) # 생성자(self -> car1)
print(car1.handle, car1.name, car1.speed)

car1.color = '검정'
print(car1.color)

print('----- 2. 새롭게 만들어진 객체-----')
car2 = Car('james', 20)
# 지역이 우선이라 james 20 찍히고 지역안에 handle이 없지 때문에 전역에 있는 0이 찍힘
print(car2.handle, car2.name, car2.speed) 

# color는 car1이라는 객체에만 넣었기 때문에 car1에만 존재
# print(car2.color) 
# print(Car.color)

print('----- 3. car1, car2주소가 Car에 들어감 (지역변수 -> 전역변수) -----')
# 리턴하기 때문에 print
print(car1.showData()) # 속도: 10킬로미터 확인한 사람 :tom

ss = car2.showData()
print(ss) # 속도: 20킬로미터 확인한 사람 :james

print()
# 이해하기
# Car
# car1 type 객체
# car2 type 객체
print('주소 :', id(Car), id(car1), id(car2))

print()
print('----- 객체의 멤버를 확인 -----')
print(car1.__dict__) # {'name': 'tom', 'speed': 10, 'color': '검정'}
print(car2.__dict__) # {'name': 'james', 'speed': 20}

print('----- car1만 변경 -----')
car1.speed = 80
print(car1.showData()) # 속도: 80킬로미터 확인한 사람 :tom
print(car2.showData()) # 속도: 20킬로미터 확인한 사람 :james

print('----- 원형클래스 수정 -> 전부다 변경된다 -----')
Car.handle = '한개'
print(car1.handle) # 한개
print(car2.handle) # 한개
'''
[그림설명]
생성자 없이도 만들어짐

1. Car (이름공간)
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
handle = 0
speed = 0
__init__
showData(self)
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

Car.jandle

또 다른 객체가 만들어짐 
2. Car type
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
car1 주소

car1 = Car('tom', 10)
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
'''












