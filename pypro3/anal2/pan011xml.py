'''
BeautifulSoup으로 XML 문서 처리
'''
from bs4 import BeautifulSoup
import pandas as pd

'''
<?xml version="1.0" encoding="UTF-8"?>
<items>
    <item>
        <name id="ks1">홍길동</name>
        <tel>010-111-1111</tel>
        <exam kor="100" eng="90" />
    </item>
    <item>
        <name id="ks2">고길동</name>
        <tel>010-111-2222</tel>
        <exam kor="88" eng="92" />
    </item>
</items>

 <class 'str'>
'''

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ XML파일 읽기 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
with open('../testdata/my.xml', mode='r', encoding="UTF-8") as f:
    xmlfile = f.read()

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ  <class 'str'> 타입 ")
print(xmlfile, type(xmlfile))

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ  <class 'bs4.BeautifulSoup'> 타입 ")
soup = BeautifulSoup(xmlfile, 'lxml') # BeautifulSoup 객체생성 (타입을 변경)
print(soup, type(soup)) 

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ findAll 첫번째 전부 출력 (item)")
# print(soup.prettify())
itemTag = soup.findAll('item')
print(itemTag[0])

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ findAll 출력 (name 0번째 id)")
nameTag = soup.findAll('name')
print(nameTag[0]['id'])

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ id 출력 (전부)")
for i in nameTag:
    print(i['id'])
    
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ 정리해서 출력")
for i in itemTag:
    nameTag = i.findAll('name')    
    for j in nameTag:
        print('id:' + j['id'] + ', name:' + j.string)
    tel = i.find('tel')
    print('tel:' + tel.string)
    for j in i.find_all('exam'):
        print('kor' + j['kor'] + ', eng:' + j['eng'])
    
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ 기상청 제공 날씨정보 읽기 ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# https://cafe.daum.net/flowlife/HqLj/33
try:
    import urllib.request as req
    url = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"    
    plainText = req.urlopen(url).read().decode('UTF-8')
    # print(plainText) # 전체 읽어오기
    
    soup = BeautifulSoup(plainText, 'lxml') # BeautifulSoup 객체 생성
    # print(soup) # BeautifulSoup 타입으로 전체 출력
    title = soup.find('title').string 
    print(title) # 기상청 육상 중기예보
    
    wf = soup.find('wf') # 첫번째 wf 읽기
    print(wf)
    
    city = soup.find_all('city') # city 전체 읽기
    print(city)
    
    cityDatas = []
    for c in city:
        cityDatas.append(c.string)
    df = pd.DataFrame() # 판다스 import
    df['city'] = cityDatas
    # print(df) # 41개의 city 값
    # tempMins = soup.select("selectoir", namespaces, limit)
    tempMins = soup.select("location > province + city +data > tmn") # +(형제 아래방향), -(형제 위방향)
    # print(tempMins)
    
    tempDatas = []
    for t in tempMins:
        tempDatas.append(t.string)
    df['temp_min'] = tempDatas
    df.columns=['지역', '최저기온']
    print(df.head(2))
    print(df.tail(2))
    
    # df를 file로 저장
    df.to_csv("날씨.csv", index = False)
    #print(pd.read_csv("날씨.csv"))
    
    print('-----'*10)       # 슬라이싱으로 나누기
    print(df[0:2])          # 앞 에서 2개
    print(df[-2:len(df)])   # 뒤 에서 2개
    
    print('-----'*10)
    print(df.iloc[0], type(df.iloc[0]))     # Series
          
    print('-----'*10)
    print(df.iloc[0:2,:])
    print(df.iloc[0:2, 0:1])
    print(df.iloc[0:2, 0:2])

    print('-----'*10)
    print(df.loc[1:3])
    print(df.loc[[1,3]])
    
    print('-----'*10)
    print(df.loc[1:3,['최저기온','지역']])
    
    print('-----'*10)
    print(df['최저기온'].mean())
    print(df['최저기온'].describe())
    
    print('-----'*10)
    df = df.astype({'최저기온':int})    # 문자를 int 를 형 변환
    print(df.loc[df['최저기온'] >= 10])
    print(df.loc[(df['최저기온'] >= 10) & (df['최저기온'] >=12)])
                 
    print('-----'*10)
    print(df.sort_values(['최저기온'], ascending = True))
    
except Exception as e:
    print('err : ', e)
#    지역 최저기온
# 0  서울   10
# 1  인천   10
# 2  수원    9    
    


