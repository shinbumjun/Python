'''
ols 사용 : 가장 기본적인 결정론적 선형회귀 방법. 불확실성이 있다.

참고 : https://www.youtube.com/watch?v=87aGAIqUSQ4&feature=youtu.be
'''
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("../testdata/drinking_water.csv")
print(df.head(3)) # 행3

print(df.corr()) # 상관관계 : 적절성과 만족도 (양의 상관관계가 제일 높다)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('회귀분석 : "만족도와 적절성은 인과관계가 있다"라는 가정하에')
model = smf.ols(formula = '만족도 ~ 적절성', data = df).fit()
print(model.summary())

print(0.766853 ** 2) # 0.58 (높은것)
print('결정계수 : ', model.rsquared) # *결정계수 :  0.58 (설명력)

print('p-value : ', model.pvalues)

print('예측값 : ', model.predict()[:5]) # [3.73596305 2.99668687 3.73596305 2.25741069 2.25741069]
print('실제값 : ', df.만족도[:5].values) # [3 2 4 2 2]
'''
print(model.summary()) # 이 표를 설명할 수 있어야 한다
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                    만족도   R-squared:                       0.588
Model:                            OLS   Adj. R-squared:                  0.586
Method:                 Least Squares   F-statistic:                     374.0
Date:                Tue, 03 May 2022   Prob (F-statistic):           2.24e-52
Time:                        10:20:12   Log-Likelihood:                -207.44
No. Observations:                 264   AIC:                             418.9
Df Residuals:                     262   BIC:                             426.0
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      0.7789      0.124      6.273      0.000       0.534       1.023
적절성            0.7393      0.038     19.340      0.000       0.664       0.815
==============================================================================
Omnibus:                       11.674   Durbin-Watson:                   2.185
Prob(Omnibus):                  0.003   Jarque-Bera (JB):               16.003
Skew:                          -0.328   Prob(JB):                     0.000335
Kurtosis:                       4.012   Cond. No.                         13.4
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
'''
# y = ax + b
# 절편 : 0.7789(b)
# 기울기 : 0.7393(a)

# 설명력 : Adj. R-squared
# 표준오차 낮으면 분산(데이터의 퍼짐정도)의 설명력이 높다는것

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('시각화')
import numpy as np
import matplotlib.pyplot as plt
plt.scatter(df.적절성, df.만족도)
slope, intercept = np.polyfit(df.적절성, df.만족도, 1)
plt.plot(df.적절성, df.적절성 * slope + intercept, 'b')
plt.show()







