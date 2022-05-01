'''
iris data로 시각화
'''
import pandas as pd
import matplotlib.pyplot as plt

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 웹에서 가져오기 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
iris_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/iris.csv")
print(iris_data.info())
print(iris_data.head(3))
#    Sepal.Length  Sepal.Width  Petal.Length  Petal.Width Species
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa


plt.scatter(iris_data['Sepal.Width'], iris_data['Petal.Width']) # x, y좌표
plt.show()


# pandas의 시각화
from pandas.plotting import scatter_matrix
iris_col = iris_data.loc[:, 'Sepal.Width':'Petal.Width']

scatter_matrix(iris_col, diagonal='kde') # diagonal='kde' 밀도분포
plt.show()


# seaborn
import seaborn as sns
sns.pairplot(iris_data, hue='Species', height=1)
plt.show()






















