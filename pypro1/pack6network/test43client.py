'''
1회용
단순 Client
'''
from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8888))
clientSock.send('안녕 반가워'.encode(encoding = 'UTF-8', errors = 'strict'))
clientSock.close()

# Client에서 socket - connect 하면 Server에서 accept가 문다
# send(인코드) - recv(디코드) - close
































