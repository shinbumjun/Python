'''
# Web server : 클라이언트와 통신이 가능

# CGI (Common Gateway Interface)
# : 웹 서버와 외부 프로그램 사이에서 정보를 주고 받는 방법이나 규약. 대화형 웹 페이지 작성 가능.
# : DB 자료 처리, form tag를 사용한 자료 전송 가능
'''
from http.server import HTTPServer, CGIHTTPRequestHandler # html 서비스, 파이썬
# 실무에서는 사용x, 아파치만큼의 기능은 없기 때문에

PORT = 8888 # 포트번호

class Handler(CGIHTTPRequestHandler): # 상속받고
    cgi_directories = ['/cgi-bin'] # 자바의 서블릿처럼 파이썬을 사용할 수 있음
    
serv = HTTPServer(('127.0.0.1', PORT), Handler) # http 서비스

print('웹 서비스 시작...')

serv.serve_forever() # 웹 서비스 시작...






































