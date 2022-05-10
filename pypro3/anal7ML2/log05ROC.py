'''
# ROC curve : 
ROC(Receiver Operating Characteristic) curve는 
다양한 threshold에 대한 이진분류기의 성능을 한번에 표시한 것이다.

이진 분류의 성능은 True Positive Rate와 False Positive Rate 두 가지를 이용해서 표현하게 된다.
ROC curve를 한 마디로 이야기하자면 ROC 커브는 좌상단에 붙어있는 커브가 더 좋은 분류기를 의미한다고 생각할 수 있다.
'''
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('분류 연습용 샘플 데이터 작석')
x, y = make_classification(100, n_features = 2,n_redundant = 0, random_state = 123)
print(x[:3])
print(y[:3])

model = LogisticRegression().fit(x, y)
y_hat = model.predict(x)
print('y_hat : ', y_hat[:3]) # y_hat :  [0 0 0]

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('결정함수(판별함수) : 불확실성 추정함수 - 판별 경계선 설정을 위함')
f_value = model.decision_function(x) 
print('f_value : ', f_value[:10])
df = pd.DataFrame(np.vstack([f_value, y_hat, y]).T, columns = ['f', 'y_hat', 'y'])
print(df.head(3))

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y, y_hat))
acc = (44 + 44) / 100       # TP + TN / 전체수 정확도
recall = 44 / (44 + 4)      # TP / TP + FN (재현도, 민감도)
specificity = 44 / (8 + 44) # TN / FP + TN (특이도)
fallout = 8 / (8 + 44)      # FP / (FP + TN)  # 위양성율 

print('acc(정확도) : ', acc)
print('recall(재현도) : ', recall) # TPR : 전체 양성 샘플 중에 양성으로 예측된 것의 비율
print('specificity(특이도) : ', specificity)
print('fallout(위양성율) : ', fallout) # FPR(1 - 특이도) : 전체 음성 샘플 중에 양성으로 잘못 예측된 것의 비율
# TPR은 1에 가까울수록 좋고, FPR은 0에 가까울수록 좋음

# acc(정확도) :  0.88
# recall(재현도) :  0.9166666666666666
# specificity(특이도) :  0.8461538461538461
# fallout(위양성율) :  0.15384615384615385

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('실제로는 이렇게 구하기~')
from sklearn import metrics
ac_sco = metrics.accuracy_score(y, y_hat)
print('ac_sco : ', ac_sco)
cl_rep = metrics.classification_report(y, y_hat)
print('cl_rep : ', cl_rep)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('분류결정 임계값 thresholds')
fpr, tpr, thresholds = metrics.roc_curve(y, model.decision_function(x))
print('fpr : ', fpr)
print('tpr : ', tpr)
print('분류결정 임계값 thresholds : ', thresholds)
# 값이 점점 작아질수록 좋은 모델 

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ROC curve 시각화')
import matplotlib.pyplot as plt
plt.plot(fpr, tpr, 'o-', label = 'LogisticRegression')
plt.plot([0, 1 ], [0, 1], 'k--', label = 'random classifier line(AUC:0.5)') # 검정색 파선
# plt.plot([fallout], [recall], 'r+', ms = 20)
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('ROC curve')
plt.legend()
plt.show()

# AUC (Area Under the ROC Curve)는 ROC curve의 밑면적을 말한다.
# 성능 평가에 있어 수치적인 기준이 될 수 있는 값으로, 1에 가까울수록 그래프가 좌상단에 근접하게 되므로 좋은 모델이라고 할 수 있다.
print('AUC : ', metrics.auc(fpr, tpr)) # 0.954727

# 해석 : ... 
















