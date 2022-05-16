'''
군집분석(Clustering) : 비지도학습
계층적 군집분석 : 특정 알고리즘에 의해 데이터들을 연결하여 계층적으로 군집(클러스터)을 형성
응집형 : 자료 하나를 군집으로 간주하고 가까운 군집끼리 연결해가는 방법(상향식)
분리형 : 전체 자료를 하나의 큰 군집으로 간주하고, 유의한 부분을 분리해가는 방법(하향식)
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic')

np.random.seed(123)
var = ['X', 'Y']
labels = ['점0', '점1', '점2', '점3', '점4']
x = np.random.random_sample([5, 2]) * 10 # 5행2열
df = pd.DataFrame(x, columns = var, index = labels)
print(df)
#            X         Y
# 점0  0.696469  0.286139
# 점1  0.226851  0.551315
# 점2  0.719469  0.423106
# 점3  0.980764  0.684830
# 점4  0.480932  0.392118

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('시각화')
# plt.scatter(x[:, 0], x[:, 1], s=50, c='blue', marker='o')
# plt.grid(True)
# plt.show()

from scipy.spatial.distance import pdist, squareform
dist_vec = pdist(df, metric = 'euclidean')
print(dist_vec) # 거리

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('거리벡터를 사각형 형식으로 출력')
row_dist = pd.DataFrame(squareform(dist_vec), columns = labels, index=labels)
print(row_dist)
#           점0        점1        점2        점3        점4
# 점0  0.000000  5.393133  1.388848  4.896710  2.401826
# 점1  5.393133  0.000000  5.090279  7.656440  2.998344
# 점2  1.388848  5.090279  0.000000  3.698301  2.405416
# 점3  4.896710  7.656440  3.698301  0.000000  5.792346
# 점4  2.401826  2.998344  2.405416  5.792346  0.000000

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('계층적 군집분석')
from scipy.cluster.hierarchy import linkage
row_cluster = linkage(dist_vec, method='ward') # single, average, ...

df = pd.DataFrame(row_cluster, columns = ['클러스터_1','클러스터_2','거리','클러스터 멤버수'])
print(df)
#    클러스터_1  클러스터_2        거리  클러스터 멤버수
# 0     0.0     2.0  1.388848       2.0
# 1     4.0     5.0  2.657109       3.0
# 2     1.0     6.0  5.454004       4.0
# 3     3.0     7.0  6.647102       5.0

from scipy.cluster.hierarchy import dendrogram
row_dend = dendrogram(row_cluster, labels = labels)
plt.tight_layout()
plt.ylabel('유클리드 거리')
plt.show()












