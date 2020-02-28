from socket import *
host = "192.168.250.193"
port = 9999
s = socket(AF_INET,SOCK_STREAM)
s.connect((host,port))
msg = "this is from client"
s.send("msg.encode ('ascii'))
R_msg = s.recv(1024)
print(R_msg.decode('ascii'))
s.close()




