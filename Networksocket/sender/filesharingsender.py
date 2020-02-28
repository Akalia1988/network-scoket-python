from socket import *
from sys import *

host = argv[1]
port = 9999

s = socket(AF_INET,SOCK_STREAM)

s.connect((host,port))

while True:
    f_name = input("File Name >")
    f_type = input("File Type (txt, Binary)>")
    s.send(f_name.encode('ascii'))
    s.send(f_type.encode('ascii'))
    if(f_type =="txt"):
        file = open(f_name, "r")
        data = file.read(1024)
        s.send(data.encode('ascii'))
        print("[+] File has been sent !")
        s.close()
    elif(f_type =="binary"):
        file = open(f_name, "rb")
        data = file.read(99999999)
        s.send(data)
        print("[+] File has been sent !")
        s.close()
else:
    print("[+] File not Fouund !")
        