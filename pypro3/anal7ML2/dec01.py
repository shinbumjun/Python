'''
DecisionTree(의사결정나무)
classification, regression 모두 가능하나 분류모델로 더 많이 사용됨 
Decision Tree는 여러 가지 규칙을 순차적으로 적용하면서 독립 변수 공간을 분할하는 분류 모형이다.

[블로그]
https://cafe.daum.net/flowlife/SBU0/13

[참고] Graphviz 2.38
https://www.npackd.org/p/org.graphviz.Graphviz/2.38

[설치 경로] 
C:\Graphviz\

[Path 설정]
고급 시스템 속성 -> Path 편집 -> 새로만들기
C:\Graphviz\bin

[Anaconda Prompt] 설치
C:\>pip install pydotplus
C:\>pip install graphviz
'''
import collections
from sklearn import tree

x = [[180, 15],[177, 42],[156, 35],[174, 5],[166, 33],[170, 12], [171, 7]]
y = ['man', 'woman', 'woman', 'man', 'woman', 'man', 'woman']
label_names = ['height', 'hair length']

model = tree.DecisionTreeClassifier(criterion = 'entropy', random_state = 0) # 불순물
model.fit(x, y)
pred = model.predict(x)
print(pred) # 예측값 : ['man' 'woman' 'woman' 'man' 'woman']

mydata = [[171, 18]]
new_pred = model.predict(mydata)
print('분류 예측 결과 : ', new_pred)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('시각화')
import pydotplus 

dot_data = tree.export_graphviz(model, feature_names = label_names, 
                                out_file = None, filled = True, rounded = True)
graph = pydotplus.graph_from_dot_data(dot_data)
colors = ('red', 'orange')
edges = collections.defaultdict(list)
print(edges, type(edges))

for e in graph.get_edge_list():
    edges[e.get_source()].append(int(e.get_destination()))
    
print(edges)

for e in edges:
    edges[e].sort()
    for i in range(2):
        dest = graph.get_node(str(edges[e][i]))[0]
        dest.set_fillcolor(colors[i])
        
graph.write_png('tree.png')

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('tree.png 그래프로 보기')
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

img = imread('tree.png')
plt.imshow(img)
plt.show()


















