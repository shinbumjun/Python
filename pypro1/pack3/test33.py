'''
3. 다중 상속 연습문제 

[참고]
https://cafe.daum.net/flowlife/RUrO/24 문제풀이
'''
class Animal: # 부모
    def move(self):
        pass
    
    
class Dog(Animal): # 단일 상속
    name = '개'
    
    def move(self): # move를 오버라이드
        print('개는 낮에 돌아 다님')
        
class Cat(Animal): # 단일 상속
    name = '고양이'
    
    def move(self): 
        print('고양이는 밤에 움직임')
        print('눈빛이 빛남')
        
        
class Wolf(Dog, Cat): # 다중 상속 
    pass
        
class Fox(Cat, Dog): # 다중 상속 
    
    def move(self): # move를 오버라이드
        print('나는 여우야~')
    
    def foxMethod(self): # 고유 메소드
        print('Fox의 고유 메소드')
        
dog = Dog()
print(dog.name) # 개
dog.move() # 개는 낮에 돌아 다님

print()
cat = Cat()
print(cat.name) # 고양이
cat.move()
# 고양이는 밤에 움직임
# 눈빛이 빛남        
    
print()
woif = Wolf() # 순서가 중요
woif.move() # 개는 낮에 돌아 다님

print()
print(Wolf.__mro__) # 클래스 상속 순서 : Wolf -> Dog -> Cat -> Animal -> object
        
     
        
        
        
        
        