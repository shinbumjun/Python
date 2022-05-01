'''
matplotlib 모듈의 기능 보충용 seaborn
'''
import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset("titanic") # titanic 데이터
print(titanic.info())


sns.displot(titanic['age'])
plt.show()


sns.boxplot(y='age', data = titanic, palette = 'Paired')
plt.show()


# sns.countplot(x="class", data = titanic) # 범주형
sns.countplot(x="class", data = titanic, hue="who") # hue="카테고리형 변수"
plt.show()


t_pivot = titanic.pivot_table(index="class", columns="sex", aggfunc="size")
print(t_pivot)
# sex     female  male
# class               
# First       94   122
# Second      76   108
# Third      144   347

sns.heatmap(t_pivot, cmap=sns.light_palette(color="gray", as_cmap=True), annot=True, fmt="d")
plt.show()










