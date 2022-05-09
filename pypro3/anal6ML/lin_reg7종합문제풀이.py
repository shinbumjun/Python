'''
회귀분석 문제 3) 

kaggle.com에서 carseats.csv 파일을 다운 받아 Sales 변수에 영향을 주는 변수들을 선택하여 선형회귀분석을 실시한다.
변수 선택은 모델.summary() 함수를 활용하여 타당한 변수만 임의적으로 선택한다.
회귀분석모형의 적절성을 위한 조건도 체크하시오.
완성된 모델로 Sales를 예측.
'''
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
plt.rc('font', family = 'malgun gothic')

data = pd.read_csv("../testdata/carseats.csv")
dpdata = pd.DataFrame(data)

print(dpdata.info()) # dpdata 정보
 
print(dpdata.head(3), dpdata.shape) # (400, 11)
#    Sales  CompPrice  Income  Advertising  ...  Age  Education Urban   US
# 0   9.50        138      73           11  ...   42         17   Yes  Yes
# 1  11.22        111      48           16  ...   65         10   Yes  Yes
# 2  10.06        113      35           10  ...   59         12   Yes  Yes

print('corr : 상관관계')
print('상관계수(r) :\n', dpdata.loc[:,['Sales', 'CompPrice']].corr()) # 0.064079
print('상관계수(r) :\n', dpdata.loc[:,['Sales', 'Income']].corr()) # 0.151951
print('상관계수(r) :\n', dpdata.loc[:,['Sales', 'Advertising']].corr()) # 0.269507
print('상관계수(r) :\n', dpdata.loc[:,['Sales', 'Age']].corr()) # -0.231815
print('상관계수(r) :\n', dpdata.loc[:,['Sales', 'Education']].corr()) # -0.051955

lm = smf.ols(formula = 'Sales ~ Advertising', data = dpdata).fit()
print(lm) # Advertising : 0.269507
print(lm.summary()) 
print('설명력 : ', lm.rsquared) # 설명력 :  0.07263390520813728
print('p값 : ', lm.pvalues[1]) # p값 :  4.377677110302816e-08

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('시각화')
plt.scatter(dpdata.Advertising, dpdata.Sales)
plt.xlabel('Advertising')
plt.ylabel('Sales')
x = pd.DataFrame({'Advertising':[dpdata.Advertising.min(), dpdata.Advertising.max()]})
y_pred = lm.predict(x)
plt.plot(x, y_pred, c = 'red')
plt.show()

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('미지의 Advertising 광고에 따른 상품 판매량 추정')
x_new = pd.DataFrame({'Advertising':[220.12, 55.66, 10]})
pred_new = lm.predict(x_new)
print('상품 판매량 추정치 : ', pred_new.values) # 31.92, 13.10, 7.88











