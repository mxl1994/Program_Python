#!/usr/bin/Python
# -*- coding: gbk -*-

import socket

def main():

    # �����׽���
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # ���ӷ�����
    tcp_socket.connect(("192.168.199.213",8080))

    # ������Ϣ
    send_data = raw_input("please input word:")
    tcp_socket.send(send_data)

    # # ������Ϣ
    # recv_data = tcp_socket.recv(1024)
    # print recv_data
    # �ر�����
    tcp_socket.close()

if __name__ == '__main__':
    main()