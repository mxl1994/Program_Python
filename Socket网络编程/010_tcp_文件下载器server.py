#!/usr/bin/Python
# -*- coding: gbk -*-

import socket


def send_file_2_client(new_client_socket):
    # ���տͻ��˷�������Ϣ
    file_name = new_client_socket.recv(1024)

    print("client want to doenload file��%s" % (file_name))

    file_content = None
    # ���ļ�����ȡ����
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except:
        print("not found file")

    # �����ļ����ݸ��ͻ���
    if file_content:
        new_client_socket.send(file_content)


def main():

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # �󶨶˿�
    tcp_server_socket.bind(("192.168.199.213",7890))
    # ����
    tcp_server_socket.listen(128)


    while True:
        # �����¿ͻ���
        new_client_socket, client_addr = tcp_server_socket.accept()

        # ���ú���
        send_file_2_client(new_client_socket)

        # �ر��׽���
        new_client_socket.close()

    # �ر��׽���
    tcp_server_socket.close()


if __name__ == '__main__':
    main()