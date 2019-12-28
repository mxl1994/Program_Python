#!/usr/bin/Python
# -*- coding: gbk -*-

import socket


def send_file_2_client(new_client_socket):
    # 接收客户端发来的消息
    file_name = new_client_socket.recv(1024)

    print("client want to doenload file：%s" % (file_name))

    file_content = None
    # 打开文件，读取数据
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except:
        print("not found file")

    # 发送文件内容给客户端
    if file_content:
        new_client_socket.send(file_content)


def main():

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口
    tcp_server_socket.bind(("192.168.199.213",7890))
    # 监听
    tcp_server_socket.listen(128)


    while True:
        # 接收新客户端
        new_client_socket, client_addr = tcp_server_socket.accept()

        # 调用函数
        send_file_2_client(new_client_socket)

        # 关闭套接字
        new_client_socket.close()

    # 关闭套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()