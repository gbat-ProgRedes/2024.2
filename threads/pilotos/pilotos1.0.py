# Threads - faz em "paralelo", programa principal aguarda.
#           Mas quem venceu?

import threading, time

def carro_f1 (nome_piloto, velocidade):
    voltas = 0
    while voltas < 5:
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

    piloto1.join()
    piloto2.join()
    piloto3.join()

    print ("A corrida terminou!!!")
except:
    print('ERRO: nao foi possivel iniciar a corrida.')

