#!/usr/bin/Python
# -*- coding: gbk -*-

import socket

def main():

    # �����׽���
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # �󶨶˿�
    tcp_socket.bind(("192.168.199.213",7890))
    # ����
    tcp_socket.listen(128)

    #ѭ��Ϊ����ͻ����ṩ����
    while True:
        print("waiting new client....")
        # new_tcp_socket��һ���µ�socket����
        new_tcp_socket,client_addr = tcp_socket.accept()

        print("new client come...")
        while True:
            # # ������Ϣ
            recv_data = new_tcp_socket.recv(1024)
            print("msg of client send %s" %(recv_data))

            if recv_data:
                #������Ϣ���ͻ���
                new_tcp_socket.send(b"dsfds")
            else:
                break

        # �ر�����
        new_tcp_socket.close()
        print("server done")

    # �ر�����
    tcp_socket.close()

if __name__ == '__main__':
    main()