# -*- coding: utf-8 -*-
from ftplib import FTP

# ip = '192.168.1.5'
# ftp = ftplib.FTP()
# ftp.encoding = 'ascii'
# ftp.connect(ip, port=21)
# ftp.login('', '')
# files = ftp.nlst('/')
# for file in files:
#     print(file)
# # ftp.delete("1.NC")
# # file = open('1.NC', mode='rb')
# # file_handle = open(file, mode="wb").write
# # cmd = 'STOR /1.NC'
# # ftp.storbinary(cmd, file)
#
# # file = r'\\192.168.1.5\DiskA\OpenCNC\NcFiles'
# # print(open(file))
encode = ['UTF-8', 'gbk', 'GB2312', 'GB18030', 'Big5', 'HZ']

def logFTP(code):
    ftp = FTP('192.168.1.5')
    try:
        ftp.login()
        ftp.encoding('ascii').decode(code)
        ftp.cwd('/')
        lst = ftp.nlst()
        for s in lst:
            print(s)
    except(UnicodeDecodeError):
        pass
    finally:
        print(code)
        # t = input('Is this?:')
        ftp.quit()


for enc in encode:
    logFTP(enc)
