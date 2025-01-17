import socket

HOST = 'httpbin.org'
resource = '/image/png'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, 80))

req = ('GET '+resource+' HTTP/1.1\r\n'+
       'Host: '+HOST+'\r\n'+
       '\r\n').encode()
       
sock.sendall(req)

resp = sock.recv(4096)
while b'\r\n\r\n' not in resp:
    resp += sock.recv(4096)
    
data = resp.split(b'\r\n\r\n')
headers = data[0]
body = data[1]

headers = headers.split(b'\r\n')
statusLine = headers[0]
headers = headers[1:]

print (statusLine)
print (headers)

toRead = 0
for header in headers:
    header = header.split(b':')
    if header[0] == b'Content-Length':
        toRead = int(header[1])

if toRead > 0:
    while len(body) < toRead:
        body += sock.recv(4096)
    
    fd = open ('out.bin', 'wb')
    fd.write(body)
    fd.close()
sock.close()