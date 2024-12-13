import socket

host = input('\nInforme o nome do HOST ou URL do site: ')


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

open = set()
for port in range (20, 10000):
    try:
        sock.connect((host, port))
        open.add(port)
        sock.close()    
    except:
        None

print (f"Portas abertas em {host}: {open}")