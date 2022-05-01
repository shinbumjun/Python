# 멀티 채팅 서버 : socket, thread

import socket
import threading

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 1) 서버 소켓 객체를 생성한다
# ss.bind(('192.168.0.10', 5555))
ss.bind(('192.168.0.12', 5555)) # 2) 접속 서버의 IP 주소와 포트 번호를 설정한다

ss.listen(5) # 3) 클라이언트의 요청을 기다린다
print('채팅 서버 서비스 시작 ...')

users = []  # 모든 클라이언트와의 연결 객체를 저장하는 리스트 변수

def chatUser(conn): # 각 클라이언트와 연결 및 데이터 송수신 처리 함수
    name = conn.recv(1024) # 클라이언트로부터 채팅명을 수신한다
    data = '^i^ ' + name.decode('UTF_8') + '님 입장 ^^' # 채팅 접속자의 입장 알림 송신 메시지
    print(data)
    
    try:
        for p in users:
            p.send(data.encode('UTF_8'))  # 접속 중인 모든 클라이언트에게 채팅명을 송신한다
        
        while True:    # 수다 떨기 메세지를 받아 모든 접속자에게 수다 메세지를 전송
            msg = conn.recv(1024) # 접속 중인 클라이언트로부터 지속적인 메시지를 수신한다
            data = name.decode('UTF_8') + '님 메세지:' + msg.decode('UTF_8')
            print(data)
            for p in users:
                p.send(data.encode('UTF_8')) # 모든 클라이언트에게 지속적으로 메시지를 송신한다
    except:
        users.remove(conn)  # 채팅을 끝낸 클라이언트 연결 객체를 users에서 삭제한다
        data = '~~ ' + name.decode('UTF_8') + '님 퇴장 ~~'
        print(data)
        
        if users:
            for p in users:
                p.send(data.encode('UTF_8')) # 모든 클라이언트에게 특정 접속자의 퇴장을 알린다
        else:
            print('exit')

while True:
    conn, addr = ss.accept()
    users.append(conn)
    th = threading.Thread(target=chatUser, args=(conn,))
    th.start()
