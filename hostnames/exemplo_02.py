import socket

host = input('\nInforme o nome do HOST ou URL do site: ')

retorno = socket.gethostbyname_ex(host)

print(retorno)
