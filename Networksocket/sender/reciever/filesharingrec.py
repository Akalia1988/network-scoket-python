from socket import *

host = "192.168.48.145"

port = 9999

s = socket(AF_INET,SOCK_STREAM)

s.bind((host,port))

s.listen(5)

while True:
    c,addr = s.accept()
    f_name = c.recv(1024).decode('ascii')
    f_type = c.recv(1024).decode('ascii')
    if(f_type == "txt"):
         file = open(f_name, "w")
         data = c.recv(1024).decode('ascii')
         file.write(data)
         file.close()
    elif(f_type =="binary"):
        file = open(f_name, "wb")
        data = c.recv(99999999).decode('ascii')
        file.write(data)
        file.close()
    else:
        print("File type is unknown")