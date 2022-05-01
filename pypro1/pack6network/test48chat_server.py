'''
[중요]
멀티 채팅 서버 : socket, thread 활용
'''
import socket
import threading

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 1) 소켓 객체
ss.bind(('192.168.0.12', 5555)) # 2) 바인딩, 튜플 타입으로 , 192.168.0.12
ss.listen(5) # 3) 동시에 5명 접속 가능

print('채팅 서버 서비스 시작 ...')

users = [] # 채팅 접속 컴의 ..., 클라이언트가 들어가는 곳 (공유자원)

def chatUser(conn): # 접속자의 갯수만큼 스래드가 이것을 부름
    name = conn.recv(1024) # 접속 명
    data = '^i^ ' + name.decode('UTF_8') + '님 입장 ^^'
    print(data)
    
    try:
        for p in users:
            p.send(data.encode('UTF_8')) # 모든 접속자에게 채팅명을 전송 (송신)
            
        while True: # 수다 떨기 메세지를 받아 모든 접속자에게 수다 메세지를 전송 (접속 후 수다)
            msg = conn.recv(1024)
            data = name.decode('UTF_8') + '님 메세지:' + msg.decode('UTF_8')
            print(data)
            for p in users:
                p.send(data.encode('UTF_8'))
    except:
        users.remove(conn)  # 채팅을 종료한 클라이언트 소켓을 제거
        data = '~~ ' + name.decode('UTF_8') + '님 퇴장 ~~'
        print(data)
        
        if users:
            for p in users:
                p.send(data.encode('UTF_8'))
        else:
            print('exit')

while True: # 무한루프 (접속할때마다)
    conn, addr = ss.accept() # 4) conn : 소켓
    users.append(conn)
    th = threading.Thread(target=chatUser, args=(conn,)) # 클라이언트가 접속을 하면 스레드가 만들어진다
    th.start() # chatUser 시작



































