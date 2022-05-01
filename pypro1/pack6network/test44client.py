'''
단순 Client
'''
import socket

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# clientSock.connect(('127.0.0.1', 7878)) 
clientSock.connect(('192.168.0.10', 7878)) # 학원주소
clientSock.sendall('신범준'.encode('UTF_8')) # 송신
re_msg = clientSock.recv(1024).decode() # 수신
print('수신 자료: ', re_msg)
clientSock.close() # 1회용이므로 닫는다





























