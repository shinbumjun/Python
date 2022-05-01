'''
[중요]
멀티 채팅 클라이언트 : socket, thread
'''
import socket
import threading
import sys

def handle(socket): #파이썬의 표준 출력은 버퍼링이 된다
    while True:
        data = socket.recv(1024)
        
        if not data:continue # 넘어오는 데이터가 없으면 찍지않는다
        print(data.decode('UTF_8'))

sys.stdout.flush() # 파이썬의 표준 출력은 버퍼링이 된다

name = input('채팅명 입력 : ')
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 1) 소켓 객체
# cs.connect(('192.168.0.10', 9510))
cs.connect(('192.168.0.12', 5555)) # 해당컴퓨터 접속
cs.send(name.encode('UTF_8'))

th = threading.Thread(target=handle, args=(cs,))
th.start()

while True: # 무한 루프로~
    msg = input() # 채팅 메세지 (수다) 입력
    sys.stdout.flush() # 비우기
    if not msg:continue # 넘어오는 데이터가 없으면 send하지 않는다
    cs.send(msg.encode('UTF_8'))
    
cs.close()

















