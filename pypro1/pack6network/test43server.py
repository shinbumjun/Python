'''
1회용
단순 Echo Server
'''
from socket import *

serverSock = socket(AF_INET, SOCK_STREAM) # 객체 생성 : socket(소켓종류, 소켓유형)
serverSock.bind(('127.0.0.1', 8888)) # 주소의 포트번호, 포켓을 주소에 바인딩한 것
serverSock.listen(1)
print('server start ...')

conn, addr = serverSock.accept() # 클라이언트 요청을 기다린다(무한루트)
print('client addr : ', addr)
print('from client message :', conn.recv(1024).decode()) # 클라이언트로부터 메세지를 받고 해석 후 출력
conn.close()
serverSock.close()

# Server의 socket - bind - listen - accept 과정
# recv - send - recv - close





















