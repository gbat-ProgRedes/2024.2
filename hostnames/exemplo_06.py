import socket, sys

host = input('Informe o nome do HOST ou URL do site: ')
port = 22 # Porta SSH

server_conn = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.settimeout(3)

try:
   sock.connect(server_conn)
except socket.gaierror:
   print('\nErro no HOST...')
except:
   print(sys.exc_info())
else:
   print('\nConexão OK...')
   sock.close()
