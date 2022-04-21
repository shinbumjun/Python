'''
# 묶음 자료형
# 자료형 중에서 int, float, bool, complex : 객체 하나를 참조
# 자료형 중에서 str, list, tuple, set, dict : 객체값 여러 개를 요소로 참조
'''

print()
print('str')
'''
str : 문자열 자료형. 순서 O : 인덱싱(하나를 집어서), 슬라이싱 가능(어디서 어디까지), 수정 X
      str은 참조만 가능 (수정 불가)  
'''
s = 'sequence'
print('길이:', len(s)) # 8
print('특정문자 포함 위치 확인 : ', s.count('e'), s.count('m'), s.find('e')) # 3 0 1
# 다량의 문자열 관련 함수 (python 문자열 처리 함수 검색)
print(id(s))
s = 'bequence' # 새로운 객체를 치환
print(id(s))

print()
# 인덱싱, 슬라이싱 가능
s = 'sequence'
print(s, s[0], s[3], s[7] ,s[-1], s[-3]) # s u e e n
print(s[0:3]) # 0이상 3미만 : seq, [시작: 끝 : 간격]
print(s[-4:-1]) # enc
print(s[:3]) # seq
print(s[3:]) # uence
print(s[2:7:1]) # quenc
print(s[2:7:2]) # qec
print(s[::2]) # sqec
print(s[2:5] + '만세') # que만세

print()
ss= 'mbc kbs'
result = ss.split(sep=' ')
print(result) # ['mbc', 'kbs']
print(':'.join(result)) # mbc:kbs

print()
print('list')
'''
list : 순서 O, 수정 O, 요소값 중복 O, 요소들을 []로 감싸기, 주소 동일
       *append, insert, extend, remove, del
'''
a = [1, 2, 3, '문자열', 4.5, True, 1, 2, 3]
print(a, type(a))
b = [a, 100, 200] # 중복 리스트
print(b) # [[1, 2, 3, '문자열', 4.5, True], 100, 200]

print()
family = ['엄마', '아빠']
print(id(family))
family[0] = '어머니'
print(id(family))
family.append('나') # 뒤에 추가
family.insert(1, '여동생') # 1번에 추가
family.extend(['삼촌', '이모'])
family += ['고모']
print(family)

family.remove('나') # 값에 의한 삭제
del family[0]
del family[0] # 순서에 의한 삭제
print(family)
del family # 변수 삭제
# print(family)

print()
print('Tuple')
'''
Tuple : 리스트와 유사, *수정 X, 요소들을 ()로 감싸기
        빠른 검색 tuple, 속도 보단 수정을 하고 싶으면 list

'''
t = ('a', 10, 'b')
t = 'a', 10, 'b' # 위와 동일
print(t, type(t))
print(t[0])
# t[0] = 'k' # TypeError: 'tuple' object does not support item assignment
a = (1)
b = (1,)
print(type(a), type(b)) # int, tuple 요소값이 하나일때는 ,를 찍어야 tuple

print()
# 형변환
aa = [1,2,3]
bb = tuple(aa)
print(type(bb)) # tuple
aa = list(bb)
print(type(aa)) # list


print()
print('Set')
'''
Set : 순서 X, 수정 X, 중복 불가, 요소들을 {}로 감싸기
      중복을 제거할 때는 set에 넣었다 빼기
'''
a = {1, 2, 3, 1}
print(a, type(a))
# print(a[0]) # TypeError : 'set' object is not subscriptable
b = {3, 4}
print(a.union(b)) # 합집합 {1, 2, 3, 4}
print(a.intersection(b)) # 교집합 {3}
print(a-b, a | b, a & b)

print()
b.update({5, 6})
b.update([7, 8])
b.update((9, 10))
print(b)

print()
b.discard(6)
b.discard(6) # 해당 값 없으면 통과
b.remove(7)
# b.remove(7) # 해당 값 없으면 에러

print('중요')
aa = [1, 2, 2, 3, 5, 5]
print(aa, type(aa)) # list
bb = set(aa)
print(bb) # 중복을 제거할 때는 set에 넣었다 빼기
aa= list(bb)
print(aa, type(aa)) # list

print()
print('dict')
'''
dict : 순서 X, 수정 O, 요소들을 {"키" : "값"}로 감싸기
'''
mydic = dict(k1 = 1, k2 = 'abc', k3 = 3.4)
print(mydic, type(mydic))

print()
dic = {'파이썬':'뱀', '자바':'커피', '스프링':['용수철', '웹처리']}
print(dic)
print(dic['파이썬'])
# print(dic[0]) # err

dic['오라클'] = '예언자' # 추가
print(dic)
del dic['오라클'] # 삭제
print(dic)
dic['파이썬'] = '만능 언어' # 수정
print(dic)












