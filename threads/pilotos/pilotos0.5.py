# Threads - faz em "paralelo", mas o programa principal termina

import threading, time

def carro_f1 (nome_piloto, velocidade):
    voltas = 0
    while voltas < 3:
        time.sleep(1/velocidade)
        voltas += 1
        print(f'{nome_piloto}: {time.ctime(time.time())} .... {voltas}')
    meuprint (f"{nome_piloto} concluiu a prova!!!")

def meuprint(msg):
    print (msg)

# Criando as threads:
try:
    piloto1 = threading.Thread(target=carro_f1, args=('Lewis Hamilton', 2))
    piloto2 = threading.Thread(target=carro_f1, args=('Sebastian Vettel', 4))
    piloto3 = threading.Thread(target=carro_f1, args=('Max Verstappen', 1))

    piloto1.start()
    piloto2.start()
    piloto3.start()

    print ("A corrida terminou!!!")
except:
    print('ERRO: nao foi possivel iniciar a corrida.')

