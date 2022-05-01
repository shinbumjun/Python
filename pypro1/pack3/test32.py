'''
다중 상속
복수의 클래스를 상속 가능 : 순서가 중요

[그림 설명]
아버지1         아버지2
+ data        + data
+ skill       + skill

아들
아버지1, 아버지2 둘다 상속
어떤 data와 skill를 가져야 하는가?

다이아몬드의 늪

'''
# 두개의 부모 클래스
class Donkey:
    data = '당나귀 만세'
    
    def skill(self):
        print('당나귀:짐 나르기')
        
class Horse: 
    data = '내가 먼저야'
    def skill(self):
        print('말:달리기')
        
    def hobby(self):
        print('프로그램 짜기')
    
# 자녀 클래스 (먼저 적어준 class에 우선 순위가 있다)
class Mule1(Donkey, Horse):
    pass

mu1 = Mule1()
print(mu1.data) # 당나귀 만세
mu1.skill() # 당나귀:짐 나르기
mu1.hobby() # 프로그램 짜기

print('----- 순서 바꿔서 -----')
class Mule2(Horse, Donkey):
    data = 'self는 요기있네?'
    def play(self):
        print('노새 고유 메소드')
        
    def hobby(self):
        print('노새는 걷기를 좋아함') # 오버라이드를 함
    
    def showHobby(self):
        self.hobby()
        super().hobby()
        print(self.data, super().data) # 두개를 정확하게 이해하기

mu2 = Mule2() # 생성자 
mu2.skill() # 말:달리기
mu2.hobby() # 노새는 걷기를 좋아함

print()
mu2.play() # 노새 고유 메소드
mu2.showHobby()
# 노새는 걷기를 좋아함
# 프로그램 짜기
# self는 요기있네? 내가 먼저야






