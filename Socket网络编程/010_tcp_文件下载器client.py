#!/usr/bin/Python
# -*- coding: gbk -*-

import socket

def main():
    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # ��ȡ��������ip\port
    dest_ip = raw_input("pleas input ip:")
    dest_port = int(raw_input("pleas input port:"))
    # ���ӷ�����
    tcp_client_socket.connect((dest_ip,dest_port))
    # ��ȡҪ���ص��ļ�����
    download_file_name = raw_input("please input filename:")

    # �����ļ�����������
    tcp_client_socket.send(download_file_name)

    # ���շ��������ص�����
    recv_data = tcp_client_socket.recv(1024)

    if recv_data:
        # ������д���ļ�
        with open("[��]"+download_file_name,"wb") as f:
            f.write(recv_data)

    # �ر��׽���
    tcp_client_socket.close()


if __name__ == '__main__':
    main()