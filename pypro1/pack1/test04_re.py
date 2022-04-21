'''
# 정규표현식 : 대량의 문자열에 대해 일정한 패턴을 부여해 원하는 문자열만 취할 수 있다
'''
import re

ss = "1234 abc 가나다abcABCfun_123555_6 Python if fun"
print(ss)
# 만족하는 문자열만 추출
print(re.findall('123', ss)) # ['123', '123'] 
aa = re.findall(r'123', ss)
print(aa[0]) # 123
print(re.findall('가나', ss)) # ['가나']
print(re.findall('[12]', ss)) # ['1', '2', '1', '2']
print(re.findall('[0-9]', ss)) # ['1', '2', '3', '4', '1', '2', '3', '5', '5', '5', '6']
print(re.findall('\d\d', ss)) # ['12', '34', '12', '35', '55']
# d s w
print()
print('한번더 보기')
print(re.findall('[0-9]+', ss)) # 1번 이상
print(re.findall('[0-9]?', ss)) # 0번 또는 1번 
print(re.findall('[0-9]*', ss)) # 0회 이상
print()
print('연속')
print(re.findall('[0-9]{2}', ss)) # 숫자 2자리 연속 ['12', '34', '12', '35', '55']
print(re.findall('[0-9]{2,3}', ss)) # 숫자 최소2, 최대3 연속 ['123', '123', '555']
print()
print('대소문자')
print(re.findall('[a-z]', ss)) # 소문자
print(re.findall('[a-zA-Z]', ss)) # 대소문자
print()
print('한글')
print(re.findall('[가-힣]', ss)) # 한글
print(re.findall('[^가-힣]', ss)) # 한글만 빼고
print()
print('매칭, 패턴')
print(re.findall('.bc', ss)) # 첫글자 아무거나 bc ['abc']
print(re.findall('a..', ss)) # ['asd', 'abc']
print()
print()
print(re.findall('^123', ss)) # ^:시작
print()
print()
print(re.findall('fun$', ss)) # fun으로 끝나는 ['fun']
print(re.findall('12|34', ss))
print()
print('그룹화')
print(re.findall('(ab)+(c)', ss)) # [('ab', 'c'), ('ab', 'c')]
print()
p = re.compile('abc')
print(re.findall(p, ss)) # ['abc', 'abc']
print()
p = re.compile('the', re.IGNORECASE) # IGNORECASE : 대소문자 분류 안함
print(p.findall('The DoG the dog')) # ['The', 'the']








