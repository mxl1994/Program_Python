#!/usr/bin/Python
# -*- coding: gbk -*-

import socket

def main():

    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 绑定端口
    tcp_socket.bind(("192.168.199.213",7890))
    # 监听
    tcp_socket.listen(128)

    #循环为多个客户端提供服务
    while True:
        print("waiting new client....")
        # new_tcp_socket是一个新的socket对象
        new_tcp_socket,client_addr = tcp_socket.accept()

        print("new client come...")
        while True:
            # # 接收消息
            recv_data = new_tcp_socket.recv(1024)
            print("msg of client send %s" %(recv_data))

            if recv_data:
                #反馈消息给客户端
                new_tcp_socket.send(b"dsfds")
            else:
                break

        # 关闭链接
        new_tcp_socket.close()
        print("server done")

    # 关闭链接
    tcp_socket.close()

if __name__ == '__main__':
    main()