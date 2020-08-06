#encoding:utf-8
import  socket

tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port =12345

tcp_socket.connect((host,port))

msg = tcp_socket.recv(1024)
print msg
tcp_socket.close()
