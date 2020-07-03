# -*- coding: utf-8 -*-
import os, socket


# file = r'\\192.168.1.5\DiskA\OpenCNC\NcFiles'
# print(open(file))

def get_ip_status():
    host = '192.168.1.5'
    port = 9992
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect(host, port)
        print(server.recv(2048))

    except Exception as err:
        print("{0} port {1} 没有打开".format(host, port))
    finally:
        server.close()


if __name__ == '__main__':
    get_ip_status()
