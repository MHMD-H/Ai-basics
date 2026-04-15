import socket

mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #we make a socket 
mysocket.connect(('data.pr4e.org',80))#connect between sochet & web
cmd = 'GET //www.dr-chuck.com/page2.htm HTTP/1.0\r\n\r\n'.encode()#get data information
mysocket.send(cmd)

while True :
 data = mysocket.recv(512)
 if len(data) < 1:
    break
 print(data.decode(),end= '')

