'''
웹에서 JSON 문서 읽기
pypro2 프로젝트 - httpserver.py 서버를 통해 library.json
'''
import json
import urllib.request as req

url = "http://127.0.0.1:8888/library.json"

# pypro2 - httpserver.py 서버를 통해 library.json 읽어오기
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ str타입 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
libdata = req.urlopen(url).read().decode()
print(libdata, type(libdata)) 
type(libdata) # <class 'str'>

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ dict타입 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
jsondata = json.loads(libdata)
print(jsondata, type(jsondata)) 
type(jsondata) # <class 'dict'>

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 0번째 찾기 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
print(jsondata['row'][0]['LIBRARY_NAME']) # LH강남 3단지 작은 도서관

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ dict의 기능을 이용해 원하는 자료 얻기 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
libData = jsondata.get('row')
print(libData)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ  ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
name = libData[0].get('LIBRARY_NAME')
print(name) # LH강남 3단지 작은 도서관

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ  ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
datas = []
for ele in libData:
    name = ele.get('LIBRARY_NAME')
    tel = ele.get('TEL_NO')
    addr = ele.get('ADRES')
    print(name + " " + tel + " " + addr)
    imsi = [name, tel, addr]
    datas.append(imsi)
    
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 테이블 형식으로 출력 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
import pandas as pd
df = pd.DataFrame(datas, columns=['도서관명', '전화', '주소'])
print(df)
    
    
    
    
    
    
    


