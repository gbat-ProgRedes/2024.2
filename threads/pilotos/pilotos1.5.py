# Threads - faz em "paralelo", programa principal aguarda.
#           Agora temos um vencedor.
import threading, time

def carro_f1 (nome_piloto, velocidade):
    global vencedor
    voltas = 0
    while voltas < 5:
        time.sleep(1/velocidade)
        voltas += 1
        print(f'{nome_piloto[0]}{voltas:02d}', end='.')

    print (f"\n{nome_piloto} concluiu a prova!!!")
    if vencedor == None:
        vencedor = nome_piloto

# Criando as threads:
try:
    vencedor = None
    piloto1 = threading.Thread(target=carro_f1, args=('Lewis Hamilton', 2))
    piloto2 = threading.Thread(target=carro_f1, args=('Sebastian Vettel', 4))
    piloto3 = threading.Thread(target=carro_f1, args=('Max Verstappen', 1))

    piloto1.start()
    piloto2.start()
    piloto3.start()

    piloto1.join()
    piloto2.join()
    piloto3.join()

    print ("A corrida terminou!!!")

    print (f"A prova terminou ....{vencedor} VENCEEEUUUU!!!")
except Exception as e:
    print('ERRO: nao foi possivel iniciar a corrida.', e)

