import socket

DIRBASE = "files/"

# Configurações do servidor
host = "127.0.0.1"
port = 3456

# Criação do socket e conexão com o servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((host, port))
    print("Conectado ao servidor.")

    # Solicita o nome do arquivo
    arq = input('Digite o nome do arquivo: ')

    # Converte o nome do arquivo para bytes e envia o comprimento e o nome
    lenNameArq = len(arq.encode('utf-8')).to_bytes(2, 'big')
    msg = lenNameArq + arq.encode()  # Concatena o comprimento e o nome do arquivo
    sock.send(msg)  

    '''    
    # Espera pela resposta do servidor
    msgServer = sock.recv(4000)  # Recebe até 4000 bytes da resposta    
    if msgServer == b'0':  
        print('OK')
        fd = open('msgServer', 'r')
        tam = fd.read(4)
        print(tam)
        arq = fd.read(tam)
        print('Esse é o aqruivo:.......................................')
        print (arq)
    '''
    # Espera pela resposta do servidor
    fileIsOk = int.from_bytes(sock.recv(2), 'big')  
    if fileIsOk == 0:
        tam = int.from_bytes(sock.recv(4), 'big')
        fd = open (DIRBASE+arq, 'wb')
        while tam > 0: 
            recBytes = sock.recv(4096)
            fd.write(recBytes)
            tam -= len(recBytes)
        fd.close()
    else:
        print('Arquivo inacessível')

except socket.error as e:
    print(f'Erro de conexão: {e}')
finally:
    sock.close()
    print("Conexão encerrada.")