#!/usr/bin/Python
# -*- coding: gbk -*-

import socket

def main():

    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 链接服务器
    tcp_socket.connect(("192.168.199.213",8080))

    # 发送消息
    send_data = raw_input("please input word:")
    tcp_socket.send(send_data)

    # # 接收消息
    # recv_data = tcp_socket.recv(1024)
    # print recv_data
    # 关闭链接
    tcp_socket.close()

if __name__ == '__main__':
    main()