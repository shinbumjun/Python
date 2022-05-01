'''
그래프 시각화, 응용
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 방법1 : matplotlib 스타일의 인터페이스로 시각화 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# plt.figure()
# plt.subplot(2,1,1) # 순서 : row(행갯수), column(열갯수), pane1 number(번호)
#
# plt.plot(x, np.sin(x)) # sin
# plt.subplot(2,1,2) # 순서 : row(행갯수), column(열갯수), pane1 number(번호)
# plt.plot(x, np.cos(x)) # cos
# plt.show()


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 방법2 : matplotlib의 개체지향 인터페이스로 시각화 (위랑 같은 방법) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# fig, ax = plt.subplots(nrows=2, ncols=1)
# ax[0].plot(x, np.sin(x))
# ax[1].plot(x, np.cos(x))
# plt.show()


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 1번방법 응용 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# fig = plt.figure()
# ax1 = fig.add_subplot(1, 2, 1) # 1행,2열,1번째
# ax2 = fig.add_subplot(1, 2, 2) # 1행,2열,2번째
#
# ax1.hist(np.random.randn(10), bins = 5, alpha = 0.5) # bins 구간수(굵기), alpha 1에 가까우면 불투명
# # ax1.hist(np.arange())
# ax2.plot(np.random.randn(10))
# plt.show()


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 세로 막대그래프 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
data = [50, 80, 100, 70, 90] # 데이터

# plt.bar(range(len(data)), data) # 세로 막대그래프
# plt.show()


print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 가로 막대그래프 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# err = np.random.rand(len(data)) # 표준편차, 오차, 신뢰구간 등 표시
# plt.barh(range(len(data)), data, xerr=err, alpha = 1) # 가로 막대그래프 (alpha 1 불투명)
# plt.show()

plt.pie(data, explode=(0, 0.1, 10, 0, 0), colors = ['yellow', 'red', 'blue']) # 중앙에서부터 간격과 색 넣기
plt.title('pie chart') # 원 모양의 그래프
plt.show()

plt.boxplot(data) # 이상치 확인할때 좋은 그래프
plt.show()

n = 30
np.random.seed(0) # 산포도 그래프
x = np.random.rand(n)
y = np.random.rand(n)
color = np.random.rand(n)
scale = np.pi * (15 * np.random.rand(n)) ** 2
plt.scatter(x, y , s=scale, c = color)
plt.show()

# 시계열 데이터
import pandas as pd
fdata = pd.DataFrame(np.random.randn(1000, 4),
                     index=pd.date_range('1/1/2000', periods=1000), columns = list('abcd'))
print(fdata.head()) # 출력

fdata = fdata.cumsum() 
plt.plot(fdata) # 그래프
plt.show()

# # pandas 의 plot 기능
# fdata.plot()
# fdata.plot(kind='bar')
# fdata.plot(kind='box')
# plt.xlabel('time')
# plt.xlabel('data')
# plt.show()









