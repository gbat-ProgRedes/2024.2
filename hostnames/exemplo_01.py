import socket

host    = input('Informe o nome do HOST ou URL do site: ')

ip_host = socket.gethostbyname(host)

print(f'\nO IP é {ip_host}')