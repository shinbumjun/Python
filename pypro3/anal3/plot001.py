'''
# 시각화 : 많은 양의 데이터를 효율적으로 봄으로해서 인사이트를 정확하게 얻어 낼 수 있다...
'''
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family= 'malgun gothic') # 한글 깨짐방지
plt.rcParams['axes.unicode_minus'] = False # 한글 깨짐방지 사용으로 음수깨지는걸 방지

x = ["서울", "인천", "수원"] # set X (이유 : 순서가 있어야해서)
y = [5, 3, 7]

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ x축(서울,인천,수원) y축(0,10) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')  
# plt.plot(y)
# plt.xlim([-1, 3]) # x축 경계값 지정
# plt.ylim([0, 10]) # y축 0~10
# plt.yticks(list(range(0, 11, 3))) # y축 (0~10 3증감)
# plt.plot(x, y)
# plt.show() # Figure 열기

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ x축(0,1,2,3,4), y축(1 3 5 7 9) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# data = np.arange(1, 11, 2) 
# print(data) # [1 3 5 7 9]
# plt.plot(data)
# x = [0,1,2,3,4]
# for a,b in zip(x, data):
#     plt.text(a, b, str(b))
# plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ sin 곡선 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# x = np.arange(10)
# y = np.sin(x)
# print(x, y)
# # [0 1 2 3 4 5 6 7 8 9] [ 0.          0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427
# #  -0.2794155   0.6569866   0.98935825  0.41211849]
#
# plt.plot(x, y)
# plt.plot(x, y, 'bo') # 스타일지정 ㅇ
# plt.plot(x, y, 'r+') # 스타일지정 +
# plt.plot(x, y, 'go:', linewidth=2, markersize=20) # linewidth : 선간격, markersize ㅇ크기
# # lw=2, marker='o', c='g'
# # go : -- 옵션에 뭘 주냐에 따라서 선형태가 달라진다
# plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ hold (sin,cos 포물선 모양) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
x= np.arange(0, np.pi * 3, 0.1) # 데이터
y_sin = np.sin(x) # 데이터
y_cos = np.cos(x) # 데이터

# plt.figure(figsize=(10, 5))
# plt.plot(x, y_sin, 'r')
# plt.scatter(x, y_cos)
# plt.xlabel('x축') # x축 이름
# plt.ylabel('y축') # y축 이름
# plt.legend(['sine', 'cosine'])
# plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ subplot (sin,cos 위아래 배치) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# plt.subplot(2, 1, 1) # 2행 1열 1번째
# plt.plot(x, y_sin, 'r')
# plt.title('사인 그래프') # 이름
#
# plt.subplot(2, 1, 2) # 2행 1열 2번째
# plt.scatter(x, y_cos)
# plt.title('코사인 그래프') # 이름
# plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 꺽은 선 그래프 (저장하는 법) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
irum = ['a', 'b', 'c', 'd', 'e'] # 데이터
kor = [80, 50, 70, 70, 90] # 데이터1 
eng = [60, 70, 80, 70, 60] # 데이터2

plt.plot(irum, kor, 'ro-') # 1빨간 선 동그라미
plt.plot(irum, eng, 'bs-') # 2파란 선 네모

plt.title('시험점수') # 이름

plt.ylim([0, 100]) # y축
plt.legend(['국어', '영어'], loc = 4) # 4에 위치 (국어, 영어 선알림) 
plt.grid(True) # 간격표시

fig = plt.gcf() # 그래프를 이미지로 저장
plt.show() # 이것을 저장
fig.savefig('plot1.png') # 그래프를 plot1.png로 저장

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 저장된 plot1.png 읽어오기 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
from matplotlib.pyplot import imread
img = imread('plot1.png')
plt.imshow(img)
plt.show()
















