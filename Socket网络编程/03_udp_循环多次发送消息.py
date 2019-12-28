#!/usr/bin/Python
# -*- coding: UTF-8 -*-
import socket

def main():
    # 1、创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # dest_ip = "192.168.199.213"
    # dest_port = 8080

    dest_addr = ("192.168.199.213", 8080)

    while True:
        send_data = raw_input("请输入要发送的消息：")

        if send_data == "exit":
            break
        # 2、发送消息
        udp_socket.sendto(send_data.encode("utf-8"), dest_addr)

    # 3、关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()