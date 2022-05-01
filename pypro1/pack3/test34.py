'''
2. 클래스의 상속관계 연습문제 - 다형성 

*** 두 개의 가전제품 클래스의 부모 클래스를 만들고 메소드를 오버라이드 하길 기대!

조건 : ElecrProduct의 sub class 두 개를 만들고
volumeControl()을 overriding 하여 다형성을 구현하시오

[참고]
https://cafe.daum.net/flowlife/RUrO/24 문제풀이

[참고]
추상클래스를 사용하는 이유는 오버라이드를 강요하기 위해 !

'''   
# 부모
class ElecProduct:
    volume = 0
    # 자식은 이것을 오버라이드 했으면 좋겠어
    def volumeControl(self, volume): # volume를 하나 받기
        pass
    
# 자녀
class ElecTv(ElecProduct): # 단일 상속
    
    # 오버라이딩을 강요하고 싶으면 추상이용
    def volumeControl(self, volume): # 오버라이딩이 옵션. 강요x
        self.volume += volume
        print('TV 소리 크기 : ', self.volume)
        
# 자녀
class ElecRadio(ElecProduct): # 단일 상속
    
    # def soriControl(self, volume): # 오버라이드 이용을 안함, 다형성 사용못함
    def volumeControl(self, volume): # 오버라이딩이 옵션. 강요x
        vol = volume
        self.volume += vol
        print('라디오 소리 크기 : ', self.volume)      
        
    def showProduct(self):
        print('라디오 만세')  
    
print('----- tv -----')
tv = ElecTv()   
tv.volumeControl(5) # TV 소리 크리 :  5
tv.volumeControl(-2) # TV 소리 크리 :  3

print('----- radio -----')
radio = ElecRadio()
radio.volumeControl(7) # 라디오 소리 크리 :  7
radio.showProduct() # 라디오 만세
    
print('----- 다형성 -----')    
product = tv
product.volumeControl(10) # TV 소리 크기 :  13
product = radio
product.volumeControl(10) # 라디오 소리 크기 :  17
    
    
    
    
    
    
    
    
    