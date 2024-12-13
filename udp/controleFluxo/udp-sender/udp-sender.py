import socket, time

SERVER = '127.0.0.1'
PORT   = 12345

sock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)

interval = float(input("Intervalo entre envio de pacotes (ms): "))
sizeData = int(input("tamanho de cada envio: "))
numPack  = int(input("Número de pacotes a enviar: "))
showAt   = int(input("Mostra enviado a cada qtos pacotes: "))
num = 1

while num <= numPack:
    # Recebe o nome do arquivo a servir
    data = (f"{num:06d}-" * (sizeData // 6 + 1))[:sizeData]
    packet = data.encode('utf-8')
    sock.sendto (packet, (SERVER, PORT))
    if num == 1 or num % showAt == 0:
        print (f">> {num:5}", packet[0:42]+b'...')
    num += 1
    time.sleep(interval/1000)
sock.close()