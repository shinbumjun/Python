'''
추상 클래스 연습문제

https://cafe.daum.net/flowlife/RUrO/24
4번 문제 (월요일)
'''
# 추상 클래스 연습문제
from abc import * # 추상

class Employee(metaclass = ABCMeta): # 추상 클래스
    def __init__(self, irum, nai): # 생성자에
        self.irum = irum # 인스턴스에 이름이 만들어진다
        self.nai = nai
 
    @abstractmethod
    def pay(self): # 추상 메소드
        pass
    
    @abstractmethod
    def data_print(self): # 추상 메소드
        pass
    
    def irumnai_print(self): # 일반 메소드
        print('이름 : ' + self.irum + ', 나이 : ' + str(self.nai), end = ' ')
        

class Temporary(Employee): # 자녀 클래스
    def __init__(self, irum, nai, ilsu, ildang ): # 이름,나이,일수,일당
        Employee.__init__(self, irum, nai) # 2개는 들고 부모에게 넘겨줌 
        
        self.ilsu = ilsu # 일수
        self.ildang = ildang # 일당
        
        # 결국은 부모를 통해서 4가지를 가지고 있는 객체가 만들어짐 
        # pay, data_print 오버라이드를 하지 않은 이상 객체가 만들수 없음
    
    def pay(self):
        return self.ilsu * self.ildang # 일수 x 일당 
    
    def data_print(self):
        self.irumnai_print() # (부모로 이동)이름, 나이
        print(', 월급 : ' + str(self.pay()))

class Regular(Employee):
    def __init__(self, irum, nai, salary):
        super().__init__(irum, nai) # super().__init__ : 부모의 생성자를 불러올수 있다(형식)
        self.salary = salary
    
    def pay(self):
        return self.salary
    
    def data_print(self):
        self.irumnai_print()
        print(', 급여 : ' + str(self.pay()))   
    
class Salesman(Regular):
    def __init__(self, irum, nai, salary, sales, commission):
        super().__init__(irum, nai, salary) # 부모의 것
        self.sales = sales # 실적
        self.commission = commission # 수수료율
    
    def pay(self):
        return super().pay() + (self.sales * self.commission) # 부모의 것 (급여)
    
    def data_print(self):
        self.irumnai_print()
        print(', 수령액 : ' + str(self.pay()))   
        

t = Temporary('홍길동', 25, 20, 15000)
t.data_print()

r = Regular('한국인', 27, 3500000)
r.data_print()

s = Salesman('손오공', 29, 1200000, 5000000, 0.25) # 급여, 영업수당, 실적, 수수료율
s.data_print()
























