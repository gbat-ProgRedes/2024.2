# Threads - faz em "paralelo", programa principal aguarda.
#           Agora temos um vencedor. Será?
import threading, time, random

def carro_f1 (nome_piloto, velocidade):
    global vencedor
    voltas = 0
    while voltas < 5:
        time.sleep(1/velocidade)
        voltas += 1
        print(f'{nome_piloto[0]}{voltas:02d}', end='.')

    lck.acquire()
    print (f"\n{nome_piloto} concluiu a prova", end='!!!!!!!!!!!!')
    if vencedor == None:
        vencedor = nome_piloto
    lck.release()

# Criando as threads:
try:
    vencedor = None
    pilotos = []
    lck = threading.Lock()

    pilotos.append (threading.Thread(target=carro_f1, args=('Lewis Hamilton', 2.00001)))
    pilotos.append (threading.Thread(target=carro_f1, args=('Sebastian Vettel', 2.00002)))
    pilotos.append (threading.Thread(target=carro_f1, args=('Max Verstappen', 2.000025)))

    for piloto in pilotos:
        piloto.start()

    for piloto in pilotos:
        piloto.join()

    print (f"\nA prova terminou ....{vencedor} VENCEEEUUUU!!!")
except Exception as e:
    print('ERRO: nao foi possivel iniciar a corrida.', e)

