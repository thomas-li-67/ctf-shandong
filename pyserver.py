import socket
import base64

def encrypt(data, key):
    plain_data = ""
    for c in data:
        plain_data += chr(ord(c) ^ key)
    return plain_data

def decrypt(data, key):
    plain_data = ""
    for c in data:
        plain_data += chr(ord(c) ^ key)
    return plain_data
        
hostport = ('192.168.152.1',9999)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(hostport)

key = ord(s.recv(1).decode())

while 1:
    user_input = raw_input('>>>')
    if user_input == 'quit':
        s.close()
        break
    
    user_input = encrypt(user_input, key)
    s.send(base64.b64encode(user_input.encode('utf-8')))
    if len(user_input) == 0:
        continue
    server_reply = base64.b64decode(s.recv(1024)).decode()
    print (decrypt(server_reply, key))