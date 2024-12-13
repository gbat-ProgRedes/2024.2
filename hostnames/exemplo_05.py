import socket

host = input('\nInforme o nome do HOST ou URL do site: ')
port = 80 # Porta HTTP

server_conn = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
   sock.connect(server_conn)
except socket.gaierror:
   print('\nErro de Conexão')
else:
   print('\nConexão OK')
   sock.close()