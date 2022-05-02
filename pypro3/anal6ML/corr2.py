'''
공공 데이터(외국인 관광객 서울 관광지 관련)로 상관관계 분석

[참고]
https://www.data.go.kr/index.do
'''
import json # json
import matplotlib.pyplot as plt # 시각화
import pandas as pd # 판다스

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('한글 깨짐방지')
plt.rc('font', family= 'malgun gothic')

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print('산점도 그래프 작성 함수')

def setScatterGraph(tour_table, all_table, tourPoint):
    # print(tourPoint) # 창덕궁, 운현궁, 경복궁, 창경궁, 종묘
    # 계산할 관광지명에 해당하는 데이터만 뽑아 tour 변수에 저장하고 외국인 자료와 병합
    tour = tour_table[tour_table['resNm'] == tourPoint]
    # print(tour)
    merge_table = pd.merge(tour, all_table, left_index = True, right_index = True)
    # print(merge_table)
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print('시각화')
    fig = plt.figure() # 생성, 선택, 편집 
    fig.suptitle(tourPoint + ' 상관관계분석')
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print('중국인')
    plt.subplot(1, 3, 1) # 1행 3열 1행에는 
    plt.xlabel('중국인 입국 수')
    plt.ylabel('외국인 입장객 수')
    lamb1 = lambda p:merge_table['china'].corr(merge_table['ForNum']) # 람다로 상관계수 구하기
    r1 = lamb1(merge_table)
    print('r1:', r1)
    plt.title('r={:.3f}'.format(r1)) # 소수3자리까지
    plt.scatter(merge_table['ForNum'], merge_table['ForNum'], s=6, c='red', alpha=0.8)
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print('일본인')
    plt.subplot(1, 3, 2) # 1행 3열 1행에는 
    plt.xlabel('일본인 입국 수')
    plt.ylabel('외국인 입장객 수')
    lamb2 = lambda p:merge_table['japan'].corr(merge_table['ForNum']) # 람다로 상관계수 구하기
    r2 = lamb2(merge_table)
    print('r2:', r2)
    plt.title('r={:.3f}'.format(r2)) # 소수3자리까지
    plt.scatter(merge_table['japan'], merge_table['ForNum'], s=6, c='green', alpha=0.8)
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print('미국인')
    plt.subplot(1, 3, 3) # 1행 3열 1행에는 
    plt.xlabel('미국인 입국 수')
    plt.ylabel('외국인 입장객 수')
    lamb3 = lambda p:merge_table.usa.corr(merge_table.ForNum) # 람다로 상관계수 구하기
    r3 = lamb3(merge_table)
    print('r3:', r3)
    plt.title('r={:.3f}'.format(r3)) # 소수3자리까지
    plt.scatter(merge_table.usa, merge_table.ForNum, s=6, c='blue', alpha=0.8)
    
    plt.tight_layout() # 공백을 정리
    plt.show()
    # 미국인 : 창덕궁 , 운형궁, 경복국 , 창경궁 , 종로 
    
    return [tourPoint, r1, r2, r3] # 광관지 명과 3개
    
    
    
def chulbal(): # 함수
    # 서울시 관광지 정보 파일 읽기
    fname = "../testdata/서울특별시_관광지입장정보_2011_2016.json"
    
    # str(읽기) -> dict : json decoding
    jsonTP = json.loads(open(fname, 'r', encoding='utf-8').read()) 
    
    # dict를 list가 감쌈
    #print(jsonTP, type(jsonTP)) 
    
    # DataFrame 타입으로 (년월, 관광지명,입장객수)
    tour_table = pd.DataFrame(jsonTP, columns=('yyyymm','resNm','ForNum'))  # 년월, 관광지명, 입장객수
    tour_table = tour_table.set_index('yyyymm') # 인덱스 키
    #print(tour_table[:2]) # 201101        창덕궁   14137 ...
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print('한국 관광명소')
    resNm = tour_table.resNm.unique()
    print('관광지명 : ', resNm[:5])
    #         resNm  ForNum
    # yyyymm              
    # 201101   창덕궁   14137
    # 201101   운현궁       0
    
    # print('관광지명 : ', resNm[:5]) # ['창덕궁' '운현궁' '경복궁' '창경궁' '종묘']
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print('중국인 정보')
    cdf = '../testdata/중국인방문객.json'
    jdata = json.loads(open(cdf, 'r', encoding = 'utf-8').read())
    # print(jdata) # [{'nat_cd': '112', 'nat_name': '중국'...
    
    china_table = pd.DataFrame(jdata, columns = ('yyyymm','visit_cnt'))
    china_table = china_table.rename(columns = {'visit_cnt':'china'})
    china_table = china_table.set_index('yyyymm')
    print(china_table[:2])
    #          china
    # yyyymm        
    # 201101   91252
    # 201102  140571
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print('일본인 정보')
    cdf = '../testdata/일본인방문객.json'
    jdata = json.loads(open(cdf, 'r', encoding = 'utf-8').read())
    # print(jdata) # [{'nat_cd': '112', 'nat_name': '중국'...
    
    japan_table = pd.DataFrame(jdata, columns = ('yyyymm','visit_cnt'))
    japan_table = japan_table.rename(columns = {'visit_cnt':'japan'})
    japan_table = japan_table.set_index('yyyymm')
    print(japan_table[:2])
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print('미국인 정보')
    cdf = '../testdata/미국인방문객.json'
    jdata = json.loads(open(cdf, 'r', encoding = 'utf-8').read())
    # print(jdata) # [{'nat_cd': '112', 'nat_name': '중국'...
    
    usa_table = pd.DataFrame(jdata, columns=('yyyymm', 'visit_cnt'))
    usa_table = usa_table.rename(columns = {'visit_cnt':'usa'})
    usa_table = usa_table.set_index('yyyymm')
    print(usa_table[:2]) 
    
    print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print('merge : 합치기')
    all_table = pd.merge(china_table, japan_table, left_index = True, right_index = True)
    all_table = pd.merge(all_table, usa_table, left_index = True, right_index = True)
    print(all_table[:3])
    #          china   japan    usa
    # yyyymm                       
    # 201101   91252  209184  43065
    # 201102  140571  230362  41077
    # 201103  141457  306126  54610
    
    r_list = []
    for tourPoint in resNm[:5]:
        r_list.append(setScatterGraph(tour_table, all_table, tourPoint))
        
    # print(r_list) # [['창덕궁', -0.05879110406006314, 0.2774443570141011, 0.4028160633050156] ...
    r_df = pd.DataFrame(r_list, columns = ('고궁명','중국','일본','미국'))
    r_df = r_df.set_index('고궁명')
    print(r_df)
    #    고궁명       중국        일본       미국
    # 0  창덕궁 -0.058791  0.277444  0.402816
    # 1  운현궁  0.445945  0.302615  0.281258
    # 2  경복궁  0.525673 -0.435228  0.425137
    # 3  창경궁  0.451233 -0.164586  0.624540
    # 4   종묘 -0.583422  0.529870 -0.121127
    
    r_df.plot(kind = 'bar', rot = 60)
    plt.show()
    
if __name__ == '__main__': # 여기가 본진이면 실행
    chulbal()












