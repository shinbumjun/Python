'''
문제는 다시보기
# 로또 생성기 : 클래스의 포함
'''
import random
# from prompt_toolkit import input

class LottoBall:
    def __init__(self, num):
        self.num = num

class LottoMachine:
    def __init__(self):
        self.ballList = [] # list 타입의 변수 준비
      
        for i in range(1, 46): # 1 ~ 45
            self.ballList.append(LottoBall(i)) # ********** 클래스의 포함 **********
            
    def selectBall(self):      
        # 섞기전
        for a in range(45):
            print(self.ballList[a].num, end = ' ')
        
        # for i in range(1, 46): # 1에서 45까지
        #    self.ballList.append(LottoBall(i)) # ********** 클래스의 포함 **********

        random.shuffle(self.ballList)
        # 섞기 후
        print()
        for a in range(45): 
            print(self.ballList[a].num, end = ' ')
            
        return self.ballList[0:6] ###
            
class LottoUi:
    def __init__(self):
        self.machine = LottoMachine() # ********** 클래스의 포함 **********
    
    def playLotto(self):
        input("로또 번호 뽑기를 시작하려면 엔터키를 누르세요")
        selectBalls = self.machine.selectBall()
        print()
        print("당첨번호 : ")
        for ball in selectBalls:
            print(ball.num, end = ' ')
        
if __name__ == '__main__':
    # aa = LottoUi()
    # aa.playLott()
    LottoUi().playLotto()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    









