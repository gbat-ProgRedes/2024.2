import socket, time

INTERFACE = '127.0.0.1'
PORT = 12345
sock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((INTERFACE, PORT))

interval = float(input("Intervalo entre recebimento de pacotes (ms): "))
sizeData  = int(input("Tamanho pacote a receber: "))
numPack  = int(input("Número de pacotes a receber: "))
showAt   = int(input("Mostra recebido a cada qtos pacotes: "))
num = 1

print ("Escutando em ...", (INTERFACE, PORT))
while num <= numPack:
    packet, source = sock.recvfrom (sizeData)
    if num == 1 or num % showAt == 0:
        print (f"{num:5} <<", source, packet[0:28]+b'...')
    num += 1
    time.sleep(interval/1000)
sock.close()
