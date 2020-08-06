#encoding:utf-8

import  socket

tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
print "host addr:",host
port=12345
tcp_socket.bind((host,port))
tcp_socket.listen(5)

c,addr = tcp_socket.accept()
print 'client id：',addr
c.sendall('xiaoli hello ')
c.close()


