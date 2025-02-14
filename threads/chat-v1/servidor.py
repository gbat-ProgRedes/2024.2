import socket
import threading
import sys

def broadCastMensage(myConn, mensagem):
    tam_mensagem = len(mensagem).to_bytes(2, 'big')
    mensagem = tam_mensagem+mensagem
    
    for conexao in conexoes:
        if conexao != myConn: #nao manda a mensagem para o proprio cliente que esta enviando
            try:
                conexao.send(mensagem)
            except:
                print(f"falha no envio a {(conexao, addr)}")


def client (myConn, myAddr): #adrr ip e porta conn = concexao atual
    print(f'Novo cliente conectado: {myAddr}')
    conexoes.append(myConn)
    prefix = f"{myAddr} digitou: ".encode('utf-8')
    
    while True:
        try:
            tam_mensagem = myConn.recv(2) #2 bytes do tamanho
            tam_mensagem = int.from_bytes(tam_mensagem,'big')
            mensagem = prefix + myConn.recv(tam_mensagem)
            broadCastMensage(myConn, mensagem)
        except:
            print ("Falha no processamento do cliente ", myAddr, "saindo.")
            break
        
    print(f"Cliente {myAddr} desconectado.") 
    conexoes.remove(myConn)
    myConn.close()

host = 'localhost' 
porta = 8080
threads = []
conexoes = []

def startServer():
    try:
        sock = socket.socket() #flexibilidade de endereço
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #definida em socket e reutiliza portas ja conectadas (1 true)
        sock.bind((host, porta))
        sock.listen()
        print("Aguardando conexões...")
    except OSError:
        print("Erro, endereço em uso.") #tratamento para o erro de endereço do terminal
        sys.exit(2)
    return sock

def main():
    sock = startServer()

    while True:
        try:
            conn, addr = sock.accept()
            t = threading.Thread(target=client, args=(conn, addr)) #config das threads
            threads.append(t)
            t.start()
        except: 
            break
        
    for t in threads:
        t.join() #recolhe os processors antes de fecha  sock.close()
    sock.close()

main()        
