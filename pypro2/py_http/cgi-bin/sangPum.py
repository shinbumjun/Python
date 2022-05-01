'''
[중요한 영역]DB 자료 출력
'''
import MySQLdb # DB
import pickle
# 123456
# mydb.dat 넣기
with open('mydb.dat', 'rb') as obj:
    config = pickle.load(obj)

print('Content-Type:text/html; charset=utf-8\n') # 브라우저에게 알려줌

# 자료 여러개
print('<head><body>')
print('<h2>상품 정보</h2>')
print('<table border="1"><tr><th>코드</th><th>상품명</th><th>수량</th><th>단가</th></tr>') # 테이블

# DB 읽어오기
try:
    conn = MySQLdb.connect(**config) # connect가 dict를 원함 **
    cursor = conn.cursor() # 커서
    
    cursor.execute("select * from sangdata") # sql작성
    datas = cursor.fetchall() # 모두 불러오기
    
    for code, sang, su, dan in datas:
        print('''
        <tr>
            <td>{0}</td>
            <td>{1}</td>
            <td>{2}</td>
            <td>{3}</td>
        </tr>
        '''.format(code, sang, su, dan))
    
except Exception as e:
    print('처리 오류:', e)
finally:
    cursor.close()
    conn.close()
     
print('</table>')
print('<br>')
print("<a href='../main.html'>메인으로</a>")
print('</head></body>')











