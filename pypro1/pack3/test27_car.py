'''
*** 이해하기 *** 
# 완성차 : 여러 개의 부품 클래스를 이용해 완성 차를 생산

'''
import pack3.test27_handle

class PohamCar:
    turnShowMessage = "정지"
    
    def __init__(self, ownerName):
        self.ownerName = ownerName # 자동차를 산 사람 이름을 기재
        self.handle = pack3.test27_handle.PohamHandle() # ********** 클래스의 포함관계 **********

    def TurnHandle(self, q): # 핸들을 붙잡고 운전
        if q > 0: # 양수면 오른쪽 
            # .이 두개면 포함관계
            self.turnShowMessage = self.handle.RightTurn(q) # PohamHandle 클래스의 RightTurn 메소드 사용
        elif q < 0:
            self.turnShowMessage = self.handle.LeftTurn(q) # PohamHandle 클래스의 LeftTurn 메소드 사용
        elif q == 0:
            self.turnShowMessage = '직진'
            self.handle.quantity = 0

if __name__ == '__main__':
    tom = PohamCar('미스터 톰') # PohamCar의 객체의 주소를 tom이 참조
    tom.TurnHandle(10)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShowMessage + str(tom.handle.quantity))
    # 미스터 톰의 회전량은 우회전10
    
    tom.TurnHandle(0)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShowMessage + str(tom.handle.quantity))
    # 미스터 톰의 회전량은 직진0
    
    print()
    sujan = PohamCar('미스 수잔') 
    sujan.TurnHandle(-15)
    print(sujan.ownerName + '의 회전량은 ' + sujan.turnShowMessage + str(sujan.handle.quantity))
    # 미스 수잔의 회전량은 좌회전-15















