# Threads - faz em "paralelo", programa principal aguarda.
#           Agora temos um vencedor.

import threading, time, random

NVOLTAS = 5
def carro_f1 (nome_piloto, velocidade):
    global vencedor
    voltas = 0
    while voltas < NVOLTAS:
        time.sleep(1/velocidade)

        lck.acquire()
        voltas += 1
        if voltas == NVOLTAS and vencedor == None:
            vencedor = nome_piloto
        lck.release()

        print(f'{nome_piloto[0]}{voltas:02d}', end='.')

    print (f"\n{nome_piloto} concluiu a prova", end='!!!!!!!!!!!!')

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

