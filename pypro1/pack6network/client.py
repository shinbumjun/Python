# 멀티 채팅 클라이언트 : socket, thread

import socket
import threading
import sys

def handle(socket): # 채팅 서버로부터 수신되는 메시지를 처리하는 함수
    while True:
        data = socket.recv(1024) # 서버가 전송한 메시지를 수신한다
        if not data:continue # 수신 메시지가 없으면 출력 없이 반복문을 수행한다
        print(data.decode('UTF_8')) # 채팅 서버로부터 수신된 메시지를 출력한다

sys.stdout.flush()  # 파이썬의 표준 출력은 버퍼링이 된다, 표준 출력장치를 비운다

name = input('채팅명 입력 :') # 키보드를 통해 채팅명을 입력받는다

# 채팅 서버와 통신을 위한 소켓 객체 생성
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# cs.connect(('192.168.0.10', 5555))
cs.connect(('192.168.0.12', 5555)) # 채팅 서버와 연결을 시도한다
cs.send(name.encode('UTF_8')) # 채팅 서버로 채팅명을 송신한다

th = threading.Thread(target=handle, args=(cs,)) # 스레드 객체를 생성한다
th.start() # 스레드 처리를 하는 Handle() 메소드 호출

while True: # 채팅 서버와의 지속적인 연결을 위한 무한루핑을 한다
    msg = input()  # 채팅 메세지(수다) 입력, 키보드를 통해 채팅 메시지를 입력받는다
    sys.stdout.flush() 
    if not msg:continue # 송신 메시지가 없으면 송신하지 않고 반복문을 수행한다
    cs.send(msg.encode('UTF_8')) # 채팅 서버로 메시지를 송신한다

cs.close()