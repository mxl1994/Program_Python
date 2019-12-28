#!/usr/bin/Python
# -*- coding: gbk -*-

import socket

def sendmsg(udp_socket):
    '''发送消息'''
    # 输入接收方的信息
    dest_ip = raw_input("请输入接收方ip:")
    dest_port = int(raw_input("请输入接收方port:"))
    # 输入发送的信息
    send_data = raw_input("请输入要发送的信息：")

    # 发送信息
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recvmsg(udp_socket):
    '''接收数据'''
    revc_data = udp_socket.recvfrom(1024)
    print("msg of from %s:%s" % (revc_data[1], revc_data[0].decode("gbk")))

def main():

    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 绑定端口
    udp_socket.bind(("",7890))

    while True:
        # 功能选择
        print("1、发送消息")
        print("2、接收消息")
        print("3、退出程序")
        num = raw_input("请输入选择的序号：")

        if num == "1":
            sendmsg(udp_socket)

        elif num == "2":
            recvmsg(udp_socket)

        elif num =="3":
            break
        else:
            print("输入有误！")
            break
    # 关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()