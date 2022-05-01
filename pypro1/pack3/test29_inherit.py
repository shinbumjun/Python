'''
자원의 재활용을 목적으로 클래스의 상속 - 다형성
`
'''

# 독립적으로 x, 부모로써만 
class Animal:
    def __init__(self): # 파이썬의 특성, 생성자
        print('Animal 생성자')
        
    def move(self):
        print('움직이는 생물')
    # ..

print('--- 자식1 ---')
class Dog(Animal): # 상속
    def __init__(self): # 파이썬의 특성, 생성자
        print('Dog 생성자') 
    
    def my(self):
        print('난 댕댕이라고 해요')

dog1 = Dog() # 객체생성, 자식의 생성자가 있을 경우 자식의 생성자만 수행한다 

dog1.my() # 본인의 메소드, 출력) 난 댕댕이라고 해요
dog1.move() # 부모로부터 물려받은, 출력) 움직이는 생물

print()
print('--- 자식2 ---')
class Horse(Animal): # 상속
    pass

horse = Horse() # 객체생성, 부모의 생성자만 있기 때문에 부모의 생성자 수행
horse.move() # 부모로부터 물려받은 














