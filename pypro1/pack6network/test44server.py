'''
무한루프
Echo Server : 서비스를 계속 유지
https://webnautes.tistory.com/1381 참고
'''
import socket
import sys

# HOST = '127.0.0.1'
HOST = '' # 내 ip어드레스가 자동으로 적용됨 (서버에서만)
PORT = 7878

serSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 1) 객체 생성 : socket(소켓종류, 소켓유형) 

try:
    serSock.bind((HOST, PORT)) # 2) 튜플타입
    serSock.listen(5) # 3) 동시 최대 접속 수 : 1 ~ 5 (동시에)
    print('서버 서비스 중 ...')

    while True:
        conn, addr = serSock.accept() # 4) 서버, 클라이언트 (해당 클라이언트 승인)
        print('client info :', addr[0], addr[1])
        print(conn.recv(1024).decode()) # 메시지를 수신 디코딩(송신은 인코딩), send - recv
        
        # 메시지 송신
        conn.send(('from server : ' + str(addr[0]) + ', 너도 잘 지내라 ~').encode('UTF_8'))

except Exception as e:
    print('err : ', e)
    sys.exit()
    
finally:
    serSock.close()
    conn.close()















