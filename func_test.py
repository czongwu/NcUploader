# -*- coding: utf-8 -*-
import ftplib

ip = '192.168.1.5'
ftp = ftplib.FTP()
ftp.encoding = 'ascii'
ftp.connect(ip, port=21)
ftp.login('', '')
files = ftp.nlst('/')
for file in files:
    print(file)
# ftp.delete("1.NC")
# file = open('1.NC', mode='rb')
# file_handle = open(file, mode="wb").write
# cmd = 'STOR /1.NC'
# ftp.storbinary(cmd, file)

# file = r'\\192.168.1.5\DiskA\OpenCNC\NcFiles'
# print(open(file))
