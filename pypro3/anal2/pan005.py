'''
file i/o
파일 형식으로 저장, 읽기
'''
import pandas as pd
# 읽기
df = pd.read_csv('../testdata/ex1.csv')
print(df, type(df)) # <class 'pandas.core.frame.DataFrame'>

print()
print(pd.read_table('../testdata/ex1.csv', sep=',', skipinitialspace=True))

print()
print(pd.read_csv('../testdata/ex2.csv', header=None))

print(pd.read_csv('../testdata/ex2.csv', header=None, names=list('korea'))) # korea열 이름

print()
print(pd.read_csv('../testdata/ex3.txt'))

print(pd.read_csv('../testdata/ex3.txt').describe())

print(pd.read_csv('../testdata/ex3.txt', sep='\s+')) # sep=' '

# print(pd.read_v('../testdata/ex3.txt', sep='\s+').describe())

print(pd.read_csv('../testdata/ex3.txt', sep='\s+', skiprows=[1,3]))

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 데이터가 붙어 있을때 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(pd.read_fwf('../testdata/data_fwt.txt', header=None, 
                  widths=(10,3,5), names=('data', 'name', 'price'), encoding='UTF-8')) # 혹시 깨진다면

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ chunk : 대 용량의 파일인 경우에는 chunk 단위로 부분 씩 읽어 들일 수 있다 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
test = pd.read_csv("../testdata/data_csv2.csv", header=None, chunksize=3)
print(test) # TextFileReader object

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 2번째 칼럼을 내림차순 정렬해서 chunk 단위로 읽음 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
for p in test:
    #print(p)
    print(p.sort_values(by=2, ascending = True)) # 2번째 칼럼을 내림차순 정렬해서 chunk 단위로 읽음

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 저장 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
items = {'apple':{'count':10,'price':1500}, 'orange':{'count':5, 'price':1000}}
df = pd.DataFrame(items)
print(df)
# df.to_clipboard() # 클립보드로 저장
# print(df.to_html()) # [중요]데이터 분석 후 쟝고에 뿌려주는것
# print(df.to_json) # json 저장
# print(df.to_xml()) # xml 저장

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 엑셀 저장 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
df.to_csv('pan5ex1.csv', sep=',') # csv(엑셀)로 저장
df.to_csv('pan5ex1.csv', sep=',', index=False) # 색인은 제외
df.to_csv('pan5ex1.csv', sep=',', index=False, header=False) # 색인, 칼럼명은 제외

# 기타 다른 파일 형식으로 저장 가능










