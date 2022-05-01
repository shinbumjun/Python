'''
웹용 파이썬 모듈 : 요청시 정보를 달고 넘어옴
이름과 나이가 넘어옴
get방식
'''
import cgi

form = cgi.FieldStorage() # 객체생성

# cgi-bin/my.py?name=tom&age=23
irum = form['name'].value # 링크에 걸려있는것 가져오기
age = form['age'].value # 링크에 걸려있는것 가져오기

print('Content-Type:text/html; charset=utf-8\n') # 브라우저에게 알려줌

print('''
<html>
<head>
<meta charset='UTF-8'>
<title>Insert title here</title>
</head>
<body>
<h2>반가워요</h2>
이름은 {0}, 나이는{1}
<br>
<a href='../main.html'>메인으로</a>
</body>
'''.format(irum, age))


















