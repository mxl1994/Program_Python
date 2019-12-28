#!/usr/bin/Python
# -*- coding: UTF-8 -*-
import socket

def main():
    # 1、创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 2、绑定端口
    udp_socket.bind(("192.168.199.213", 7890))

    # 3、接收消息
    data_msg = udp_socket.recvfrom(1024)

    # 4、打印接收到的信息
    revc_msg = data_msg[0]
    revc_addr = data_msg[1]
    # print(data_msg)    # 结果('hello', ('192.168.199.213', 8080))
    print(revc_addr)
    print(revc_msg.decode("gbk"))

    # 5、关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()