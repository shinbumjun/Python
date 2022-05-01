'''
# 상속 (단일 상속)
[그림 설명]
  Person
  ㅣ  ㅣ
  e   w
     ㅣ 
     p 
     
p는 w를 통해서 Person으로 가야한다

엑셀은 조금 할 줄 알아야한다
보고서

파워포인트
access
'''
# 부모
class Person:
    say = '난 사람이야'
    nai = 20
    __abc = 'good' # 변수명에 __를 주면 private
    
    def __init__(self, nai):
        print('Person 생성자')
        self.nai = nai
        
    def printInfo(self): # 객체가 생성이 되었으면 그쪽으로간다
        print('나이:{}, 이야기:{}'.format(self.nai, self.say)) # self를 this와 비교
        
    def hello(self):
        print('안녕')
        print(self.__abc)
        
    @staticmethod # 스태틱 메소드, self 없음, 다른 class에서 사용 가능, 데코레이터 (스프링에서는 어노테이션)
    def sbs(tel):
        print('sbs_static method', tel)

print(Person.say, Person.nai) # 출력)난 사람이야 20
p = Person(22) # 출력)Person 생성자, 새로운 객체
p.printInfo() # 출력)나이:22, 이야기:난 사람이야

print('***' * 10)
class Employee(Person):
    say = '일하는 동물'
    subject = '근로자' # Employee가 가지고 있는 고유한 것
    
    def __init__(self):
        print('Employee 생성자 ~~~')
        
    def printInfo(self): # method overide
        print('Employee 클래스 내의 printInfo')    
        
    def eprintInfo(self):
        self.printInfo() # 자신의 printInfo(), 자신한테 printInfo() 없다면 부모, 둘다 없다면 모듈로
        super().printInfo() # 부모의 printInfo()
        print(self.say, super().say) # 중요 : self.say는 본인, super().say는 부모
        self.hello()
        
e = Employee() # 출력) Employee 생성자 ~~~, 생성자를 부른다
print(e.say, e.nai) # 출력) 난 사람이야 20
print(e.subject) # 근로자
e.printInfo() 
# 출력) 나이:20, 이야기:일하는 동물, 주소를 담아서 객체에 생성 나이가 없으므로 부모로 올라가서 나이를 찍음
# 자신에게 printInfo 생기면, 출력) Employee 클래스 내의 printInfo
e.eprintInfo() 
# 출력) 나이:20, 이야기:일하는 동물, 없으면 부모에게로 올라감
# 자신에게 printInfo 생기면, 출력) Employee 클래스 내의 printInfo

print()
print('***' * 10)
class Worker(Person):
    def __init__(self, nai): # 나이를 하나 받는것으로
        print('Worker 생성자')
        super().__init__(nai) # 부모의 생성자, 부모에게 나이도 줘야함, Bound method call
    
    def printInfo(self):
        print('신범준')
        
    def wprintInfo(self):
        super().printInfo() # 본인에게 없기 때문에 부모로, 바로 부모로, 본인에게 있으면 신범준
        
w = Worker('25') # 출력) Worker 생성자 Person 생성자, 생성자 부르고 25
print(w.say, w.nai) # 출력) 난 사람이야 25, 본인한테 없기 때문에 부모
w.printInfo() # 출력) 나이:25, 이야기:난 사람이야, 본인에게 없기 때문에 부모로, 본인에게 있으면 신범준
w.wprintInfo() # 출력) 나이:25, 이야기:난 사람이야, 바로 부모로

print()
print('***' * 10)
class Programmer(Worker): # Programmer는 Worker의 자식
    def __init__(self, nai):
        print('Programmer 생성자')
        Worker.__init__(self, nai) # Bound method call

    def wprintInfo(self): # 오버라이딩
        print('Programmer 내에 작성된 wprintInfo') 

    def hello2(self):
        print(super().__abc) # private 이기 때문에 에러

pr = Programmer(33) # pr이 주소를 참조
# 거슬러 올라감
# Programmer 생성자
# Worker 생성자
# Person 생성자
print(pr.say, pr.nai) # 출력) 난 사람이야 33, 부모로 올라가고 부모에서 super하기 때문에 부모의 부모
pr.printInfo() # 출력) 나이:33, 이야기:난 사람이야, 부모로 올라가고 부모에게 없어서 부모의 부모, 부모에게 있으면 신범준
pr.wprintInfo() # 출력) Programmer 내에 작성된 wprintInfo

print()
p.hello()
# 안녕
# good
# pr.hello2() # private 이기 때문에 해당 class에서만 사용, 에러

print()
w.sbs('111-1111') # sbs_static method 111-1111
pr.sbs('222-2222') # sbs_static method 222-2222

print('----- 클래스 타입 (어떤 피가 흐르는지) -----')
a = 10
print(type(a)) # int
print(type(pr)) # Programmer 타입
print(Programmer.__bases__) # Worker
print(Worker.__bases__) # Person
print(Person.__bases__) # object, 최상의 super class











