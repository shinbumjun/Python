'''
JSON 처리
JSON 객체를 dict로 JSON 디코딩
dict 객체를 JSON로 JSON 인코딩
'''
import json
dict = {'name':'tom','age':22, 'score':['90','80','100']}
print(dict, type(dict)) # <class 'dict'>

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 인코딩(dict -> str) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
str_val = json.dumps(dict)
print(str_val, type(str_val)) # <class 'str'>
print(str_val[0:20]) # str이 할 수 있는 것만 작업이 가능 
# print(str_val['name']) # TypeError : string indices must be integers

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 디코딩(str -> dict) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
json_val = json.loads(str_val)
print(json_val, type(json_val))
print(json_val['name']) # dict type이 할 수 있는 명령을 사용할 수 있다

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ json 문서 읽기 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
json_data = {}

def read_data(filename):
    f = open(filename, 'r', encoding='UTF-8')
    lines = f.read()
    f.close()
    
    jdata = json.loads(lines) # decoding   str -> dict
    return jdata

def main():
    global json_data
    json_data = read_data('pan012.json')
    print(json_data, type(json_data))

    d1 = json_data['직원']['이름']
    d2 = json_data['직원']['직급']
    d3 = json_data['직원']['전화']
    print(d1,d2,d3)
    d4 = json_data['웹사이트']['카페명']
    d5 = json_data['웹사이트']['userid']
    print(d4,d5)


if __name__ == "__main__":
    main()

















