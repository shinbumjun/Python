'''
군집화 (iris_datset)
'''
import pandas as pd
from sklearn.datasets import load_iris 
import matplotlib.pyplot as plt

iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
print(iris_df.head(3))
#    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
# 0                5.1               3.5                1.4               0.2
# 1                4.9               3.0                1.4               0.2
# 2                4.7               3.2                1.3               0.2

from scipy.spatial.distance import pdist, squareform

# dist_vec = pdist(iris_df.loc[0:4, ['sepal length (cm)', 'sepal width (cm)']], metric = 'euclidean')
dist_vec = pdist(iris_df.loc[:, ['sepal length (cm)', 'sepal width (cm)']], metric = 'euclidean')
# 150개 다보기
print(dist_vec)
row_dist = pd.DataFrame(squareform(dist_vec))
print(row_dist)
#           0         1         2         3         4
# 0  0.000000  0.538516  0.500000  0.640312  0.141421
# 1  0.538516  0.000000  0.282843  0.316228  0.608276
# 2  0.500000  0.282843  0.000000  0.141421  0.500000
# 3  0.640312  0.316228  0.141421  0.000000  0.640312
# 4  0.141421  0.608276  0.500000  0.640312  0.000000

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('dendrogram')
from scipy.cluster.hierarchy import linkage, dendrogram
row_cluster = linkage(dist_vec, method = 'complete')
print('row_cluster:', row_cluster)
df = pd.DataFrame(row_cluster, columns = ['id_1', 'id_2', 'dist', 'member'])
print(df)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('dendrogram 시각화로 보기')
row_dend = dendrogram(row_cluster)
plt.tight_layout()
plt.ylabel('euclidean dist')
plt.show()

















