#!/usr/bin/Python
# -*- coding: gbk -*-

import socket

def sendmsg(udp_socket):
    '''������Ϣ'''
    # ������շ�����Ϣ
    dest_ip = raw_input("��������շ�ip:")
    dest_port = int(raw_input("��������շ�port:"))
    # ���뷢�͵���Ϣ
    send_data = raw_input("������Ҫ���͵���Ϣ��")

    # ������Ϣ
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recvmsg(udp_socket):
    '''��������'''
    revc_data = udp_socket.recvfrom(1024)
    print("msg of from %s:%s" % (revc_data[1], revc_data[0].decode("gbk")))

def main():

    # �����׽���
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # �󶨶˿�
    udp_socket.bind(("",7890))

    while True:
        # ����ѡ��
        print("1��������Ϣ")
        print("2��������Ϣ")
        print("3���˳�����")
        num = raw_input("������ѡ�����ţ�")

        if num == "1":
            sendmsg(udp_socket)

        elif num == "2":
            recvmsg(udp_socket)

        elif num =="3":
            break
        else:
            print("��������")
            break
    # �ر��׽���
    udp_socket.close()

if __name__ == '__main__':
    main()