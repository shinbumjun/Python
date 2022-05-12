print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# 11번 [t테스트2] 참고
import pandas as pd
from numpy import average
from scipy import stats

blue = [70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80]
red = [60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66]
print(average(blue), ' ', average(red))     # 72.81818181818181   63.81818181818182

two_sample = stats.ttest_ind(blue, red)
print(two_sample)
# Ttest_indResult(statistic=2.9280203225212174, pvalue=0.008316545714784403)
# 해석 : pvalue=0.008316545 < 0.05 이므로 귀무 기각
# 귀무가설: 포장지 색상에 따른 매출액 차이가 없다.
# 대립가설: 포장지 색상에 따른 매출액 차이가 있다.
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# 12번 [t테스트1onesample문제] 참고
import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_csv("../testdata/babyboom.csv")
print(data)
fdata = data[data.gender == 2]
df = pd.DataFrame(data = fdata, columns = ['gender', 'weight'])
print(df)
print(stats.ttest_1samp(fdata.weight, popmean=3000))
# Ttest_1sampResult(statistic=4.47078356044109, pvalue=0.00014690296107439875)
# p-value : 0.0001 < 0.05이므로 귀무 가설 기각
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# 13번 [corr1상관관계분석] 참고
import numpy as np

x = (1,2,3,4,5)
y = (8,7,6,4,5)
print(np.corrcoef(x, y))
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# 14번 [eat_out.txt] 메모장
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
from sklearn.metrics import accuracy_score

# 데이터 가공1
# data = pd.read_csv("../testdata/eat_out.txt")
# print(data)
# st_data = data[data.요일 == '토']
# sd_data = data[data.요일 == '일']
# df = pd.concat([st_data, sd_data])
# print(df) 

# 시험 test
# 데이터 가공2
# data = pd.read_csv('../testdata/last_test.csv')
# print(data)
# eatout = data[(data.요일 == '토')| (data.요일 == '일')]
# print(eatout)

# [log01] 참고
data = pd.read_csv("../testdata/eat_out.txt")
print(data)
st_data = data[data.요일 == '토']
sd_data = data[data.요일 == '일']
df = pd.concat([st_data, sd_data])
print(df) # 데이터 가공

formula = '외식유무 ~ 소득수준' # 소득 수준이 외식에 영향
result = smf.glm(formula = formula, data = df, family = sm.families.Binomial()).fit() # 함수
print(result.summary())
pred = result.predict(df)
print(pred)
print('정확도 : ', accuracy_score(df['외식유무'], np.around(pred)))
key = int(input('소득 수준 입력 : '))
newdf = pd.DataFrame({'소득수준':[key]})
pred2 = result.predict(newdf)
print('외식 유무 : ', np.rint(pred2.values))
# 45입력 -> 외식 유무 :  [0.]
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# 15번 [dec01] 참고
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')











