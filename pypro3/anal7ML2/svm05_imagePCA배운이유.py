'''
SVM으로 이미지 분류
'''
from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline

faces = fetch_lfw_people(min_faces_per_person = 60, color = False) # 각 인물당 사진은 60장
print(faces)
print(faces.DESCR)

print(faces.data)
print(faces.data.shape) # (1348, 2914)
print(faces.target) # [1 3 3 ... 7 3 5]
print(faces.target_names) # ['Ariel Sharon' 'Colin Powell' 'Donald Rumsfeld' 'George W Bush' ...
print(faces.images.shape) # (1348, 62, 47)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('한명보기')
# print(faces.images[1])
# print(faces.images[1])
# plt.imshow(faces.images[1], cmap='bone')
# plt.show() # 1번째는 부시 
# 흑색은 62행 47열 (0 ~ 255)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('3행 5열 보기')
# fig, ax = plt.subplots(3, 5)
# # print(fig) # Figure(640x480)
# print(len(ax.flat))
#
# for i, axi in enumerate(ax.flat):
#     axi.imshow(faces.images[i], cmap='bone')
#     axi.set(xticks = [], yticks = [], xlabel = faces.target_names[faces.target[i]])
# plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('PCA로 이미지 차원을 축소한 후 분류 모델 작성')
m_pca = PCA(n_components = 150, whiten = True, random_state = 0) 
# 이미지에 가장 큰영향을 주는 150 개의 주성분. 차원축소된 데이터로 추출
x_row = m_pca.fit_transform(faces.data)
print('x_row : ', x_row, x_row.shape) # (1348, 150)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('PCA가 선행된 데이터로 SVM 모델 작성')
m_svc = SVC(C = 1)
model = make_pipeline(m_pca, m_svc)
print(model)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('train / test 데이터 나누기')
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(faces.data, faces.target, random_state = 1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
print(x_train[0])
print(y_train[0])

model.fit(x_train, y_train)
pred = model.predict(x_test)
print('pred : ', pred[:10]) # 예측 : [1 4 1 3 3 3 7 3 3 3]
print('real : ', y_test[:10]) # 결과 : [1 4 1 5 3 2 7 3 1 3]

from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
mat = confusion_matrix(y_test, pred)
print('confusion matrix : \n', mat)
print('accu4racy : ', accuracy_score(y_test, pred)) # 0.7952
print(classification_report(y_test, pred, target_names = faces.target_names))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('분류 결과 시각화 (맞은건 검정색, 틀린건 빨간색)')
fig, ax = plt.subplots(4, 6)

for i, axi in enumerate(ax.flat):
    axi.imshow(x_test[i].reshape(62, 47), cmap='bone')
    axi.set(xticks = [], yticks = [])
    axi.set_ylabel(faces.target_names[pred[i]].split()[-1], color = 'black' if pred[i] == y_test[i] else 'red')  
    
plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('오차 행렬 시각화')
import seaborn as sns
sns.heatmap(mat.T, square = True, annot = True, fmt = 'd', cbar = False, 
            xticklabels = faces.target_names, yticklabels = faces.target_names)
plt.xlabel('real label')
plt.ylabel('predict label')
plt.show()



















