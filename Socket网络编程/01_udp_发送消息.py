#encoding:utf-8

import socket

def main():
    # 1、创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    dest_ip = "192.168.199.213"
    dest_port = 8080

    # 2、发送消息
    udp_socket.sendto(b"ahjdshf",(dest_ip,dest_port))

    #3、关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()