# Threads - sem threads. Completamente sequencial

import time

def carro_f1 (nome_piloto, velocidade):
    voltas = 0
    while voltas < 3:
        time.sleep(1/velocidade)
        voltas += 1
        print(f'{nome_piloto}: {time.ctime(time.time())} .... {voltas}')
    meuprint (f"{nome_piloto} concluiu a prova!!!")

def meuprint(msg):
    print (msg)

try:
    carro_f1 ('Lewis Hamilton', 2)
    carro_f1 ('Sebastian Vettel', 4)
    carro_f1 ('Max Verstappen', 1)

    print ("A corrida terminou!!!")
    print ("Quem foi o vencedor?")
except:
    print('ERRO: nao foi possivel iniciar a corrida.')

