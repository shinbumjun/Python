'''
# iris dataset으로 선형회귀분석 (상관관계가 약한 경우와 강한 경우로 분석 모델을 작성해 비교)

상관관계가 약한 두 변수(단순 선형회귀)
상관관계가 강한 두 변수

새로운 값(petal_length)으로 미지의 sepal_length 값 얻기

다중 선형회귀 : 독립변수 복수
'''
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf

iris = sns.load_dataset('iris')
print(iris.head(3), iris.shape) # (150, 5)
#    sepal_length  sepal_width  petal_length  petal_width species
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa

print(iris.corr(method='pearson')) # 상관관계
#               sepal_length  sepal_width  petal_length  petal_width
# sepal_length      1.000000    -0.117570      0.871754     0.817941
# sepal_width      -0.117570     1.000000     -0.428440    -0.366126
# petal_length      0.871754    -0.428440      1.000000     0.962865
# petal_width       0.817941    -0.366126      0.962865     1.000000

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('단순 선형회귀')
print('1. 상관관계가 약한 두 변수')
result1 = smf.ols(formula = 'sepal_length ~ sepal_width', data = iris).fit()
print('요약결과1 : ', result1.summary())
"""
OLS Regression Results                            
==============================================================================
Dep. Variable:           sepal_length   R-squared:                       0.014
Model:                            OLS   Adj. R-squared:                  0.007
Method:                 Least Squares   F-statistic:                     2.074
Date:                Tue, 03 May 2022   Prob (F-statistic):              0.152
Time:                        11:43:17   Log-Likelihood:                -183.00
No. Observations:                 150   AIC:                             370.0
Df Residuals:                     148   BIC:                             376.0
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
===============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------
Intercept       6.5262      0.479     13.628      0.000       5.580       7.473
sepal_width    -0.2234      0.155     -1.440      0.152      -0.530       0.083
==============================================================================
Omnibus:                        4.389   Durbin-Watson:                   0.952
Prob(Omnibus):                  0.111   Jarque-Bera (JB):                4.237
Skew:                           0.360   Prob(JB):                        0.120
Kurtosis:                       2.600   Cond. No.                         24.2
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
"""
print('R squared : ', result1.rsquared) # 설명력 : 0.0138
print('p-value : ', result1.pvalues[1]) # p-value : 0.151

# 1 모델은 의미 없는 모델!

print('실제 값 : ', iris.sepal_length[:5].values) # [5.1 4.9 4.7 4.6 5. ]
print('예측 값 : ', result1.predict()[:5]) # [5.74445884 5.85613937 5.81146716 5.83380326 5.72212273]

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('2. 상관관계가 강한 두 변수')
result2 = smf.ols(formula = 'sepal_length ~ petal_length', data = iris).fit()
print('요약결과2 : ', result2.summary())

print('R squared : ', result2.rsquared) # 설명력 : 0.7599546457725153
print('p-value : ', result2.pvalues[1]) # p-value : 1.0386674194499606e-47

# 모델은 의미 있는 모델!

print('실제 값 : ', iris.sepal_length[:5].values) # [5.1 4.9 4.7 4.6 5. ]
print('예측 값 : ', result2.predict()[:5]) # [4.8790946  4.8790946  4.83820238 4.91998683 4.8790946 ]

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('새로운 값(petal_length)으로 미지의 sepal_length 값 얻기')
# 설명력 : 0.7599으로 예측
new_data = pd.DataFrame({'petal_length':[1.1, 0.5, 5.0]})
y_pred = result2.predict(new_data)
print('예측 결과 : ', y_pred.values) # [4.75641792 4.51106455 6.3512148 ] 

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('다중 선형회귀 : 독립변수 복수')
result3 = smf.ols(formula = 'sepal_length ~ petal_length+petal_width+sepal_width', data = iris).fit()
print('요약결과2:', result3.summary())
# 독립변수가 늘어나면 Adj. R-squared : 0.856

# 여러 개의 독립변수는 join을 사용
column_select = "+".join(iris.columns.difference(['sepal_length','species']))
print(column_select)
result3 = smf.ols(formula = 'sepal_length ~ ' + column_select, data = iris).fit()
print('요약결과2:', result3.summary())






