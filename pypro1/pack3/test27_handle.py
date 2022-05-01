'''
[그림설명]
OOP 객체지향
자원의 재활용 : has a(포함), is a(상속)

자동차
class 부품을 모아서 만들면 완성품이 된다 

[연습]
핸들 class만 만들어 보자

회전량 - 직진(0), 좌(-), 우(+)

'''
# 완성 제품의 부품 클래스로 핸들
class PohamHandle: 
    quantity = 0 # 회전량
    
    def LeftTurn(self, quantity):
        self.quantity = quantity
        return '좌회전'
    
    def RightTurn(self, quantity):
        self.quantity = quantity
        return '우회전'
    
    # ...
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




















