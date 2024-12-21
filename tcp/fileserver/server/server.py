import socket, os

DIRBASE = "files/"
INTERFACE = ""
PORT = 3456

myTCPsock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

myTCPsock.bind((INTERFACE, PORT))
myTCPsock.listen(1)

print ("Escutando em ...", (INTERFACE, PORT))

while True:
    # Recebe o nome do arquivo a servir
    con, cliente = myTCPsock.accept()
    print('Conectado por: ', cliente)

    while True:
        mensagem = con.recv(2)
        mensagem =  int.from_bytes(mensagem, 'big')
		# Abre o arquivo a servir ao cliente
        fileName = con.recv(mensagem).decode('utf-8')
        if not mensagem: break
        print ("Recebi pedido para o arquivo ", fileName)
        fileName = DIRBASE+fileName
        if os.path.exists(fileName):
            con.send(b'\x00\x00')
            fileSize = os.path.getsize(fileName)
            con.send(fileSize.to_bytes(4, 'big'))

            fd = open (fileName, 'rb')

            # Lê o conteúdo do arquivo a enviar ao cliente
            print ("Enviando arquivo ", fileName)
            fileData = fd.read(4096)
            while fileData != b'':
                con.send(fileData)
                fileData = fd.read(4096)
            # Fecha o arquivo
            fd.close()
        else:
            con.send(b'\x00\x01')
        con.close()
    myTCPsock.close()
