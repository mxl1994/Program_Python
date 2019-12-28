#!/usr/bin/Python
# -*- coding: gbk -*-

import socket

def main():
    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 获取服务器的ip\port
    dest_ip = raw_input("pleas input ip:")
    dest_port = int(raw_input("pleas input port:"))
    # 链接服务器
    tcp_client_socket.connect((dest_ip,dest_port))
    # 获取要下载的文件文字
    download_file_name = raw_input("please input filename:")

    # 发送文件名给服务器
    tcp_client_socket.send(download_file_name)

    # 接收服务器返回的数据
    recv_data = tcp_client_socket.recv(1024)

    if recv_data:
        # 将数据写进文件
        with open("[新]"+download_file_name,"wb") as f:
            f.write(recv_data)

    # 关闭套接字
    tcp_client_socket.close()


if __name__ == '__main__':
    main()