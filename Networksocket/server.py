from socket import *

host = "192.168.250.193"
port = 9999

s = socket(AF_INET,SOCK_STREAM)

s.bind((host,port))

s.listen(5)

while True:
   c,addr = s.accept()  
   print("[+]Got connecting from", addr)
   R_msg = c.recv(1024)
   print(R_msg.decode('ascii'))
   msg = "this is from server"
   c.send(msg.encode('ascii'))
   c.close()

