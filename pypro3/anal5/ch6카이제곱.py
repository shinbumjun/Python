'''
이원카이제곱
동질성 검정 - 두 집단의 분포가 동일한가? 다른 분포인가? 를 검증하는 방법이다. 두 집단 이상에서 각 버무(집단) 간의 비울이 
동일한가를 검정하게 된다. 두 개 이상의 범주형 자료가 동일한 분포를 갖는 모집단에서 추출된 것인지 검정하는 방법이다

동질성 검정실습1) 교육방법에 따른 교육생들의 만족도 분석 - 동질성 검정 survey_method.cs
귀무 : 교육방법에 따른 교육생들의 만족도에 차이가 없다. 동질이다. 분포가 같다.
대립 : 교육방법에 따른 교육생들의 만족도에 차이가 있다. 동질이 아니다. 분포가 다르다.
'''
import pandas as pd
import scipy.stats as stats

data = pd.read_csv("../testdata/survey_method.csv")
print(data.head(5))
#    no  method  survey
# 0   1       1       1
# 1   2       2       2
# ...

print(data['method'].unique()) # [1 2 3]
print(data['survey'].unique()) # [1 2 3 4 5]

# 교차표
ctab = pd.crosstab(index = data['method'], columns = data['survey'])
ctab.columns = ['매우만족','만족','보통','불만족','매우불만족']
ctab.index = ['방법1', '방법2', '방법3']
print(ctab)

chi2, p, df, _ = stats.chi2_contingency(ctab)
print('chi2:{}, p:{}, ddof:{}'.format(chi2, p, df))
# 해석 : p:0.586457 > 0.05 이므로 귀무 채택 (정설이 맞음), 대립 기각
# 귀무 : 교육방법에 따른 교육생들의 만족도에 차이가 없다

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 동질성 검정 실습2) 연령대별 sns 이용률의 동질성 검정 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
'''
# 20대에서 40대까지 연령대별로 서로 조금씩 그 특성이 다른 SNS 서비스들에 대해 이용 현황을 조사한 자료를 바탕으로 연령대별로 홍보
# 전략을 세우고자 한다.
# 연령대별로 이용 현황이 서로 동일한지 검정해 보도록 하자.
# 귀무 : 연령대별로 sns 이용률은 동일하다.
# 대립 : 연령대별로 sns 이용률은 동일하지 않다.
'''
data2 = pd.read_csv("../testdata/snsbyage.csv")
print(data2.head(3), len(data2)) # 1439

print(data2['age'].unique()) # [1 2 3]
print(data2['service'].unique()) # ['F' 'T' 'K' 'C' 'E']

# 교차표 
ctab2 = pd.crosstab(index = data2['age'], columns = data2['service'])
print(ctab2)

chi2, p, df, _ = stats.chi2_contingency(ctab2)
print('chi2:{}, p:{}, ddof:{}'.format(chi2, p, df))
# chi2:102.75202494484225 (카이제곱)
# 해석 : p:1.1679064204212775e-18 < 0.05 이므로 귀무 기각
# 대립 : 연령대별로 sns 이용률은 동일하지 않다.

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ  ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
# 만약에 snsbyage.csv 데이터가 모집단(1439 행)이라면 표본 추출 후 가설검정을 진행한다.
sample_data = data2.sample(n = 500, replace = False)
print(sample_data.head(3), len(sample_data))

ctab3 = pd.crosstab(index = sample_data['age'], columns = data2['service'])
print(ctab2)

chi2, p, df, _ = stats.chi2_contingency(ctab3)
print('chi2:{}, p:{}, ddof:{}'.format(chi2, p, df))
# 해석 : p:6.607126251165985e-08 < 0.05 이므로 귀무 기각.





