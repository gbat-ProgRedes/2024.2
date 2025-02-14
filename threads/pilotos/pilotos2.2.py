# Threads - faz em "paralelo", programa principal aguarda.
#           Agora temos um vencedor. Será?

import threading, time

def carro_f1 (nome_piloto, velocidade, vencedores):
    voltas = 0
    while voltas < 5:
        time.sleep(1/velocidade)
        voltas += 1
        print(f'{nome_piloto[0]}{voltas:02d}', end='.')

    print (f"\n{nome_piloto} concluiu a prova!!!")
    vencedores.append(nome_piloto)

'''
#M1
   L: fez o teste vencedor == None e deu ok
#M2
   L: perde a CPU
   S: ganha a CPU e testa se vencedor == None e deu Ok
#M3
   V: ganha a CPU e ainda está correndo e faz alguma coisa
#M4
   L: ganha a CPU e faz vencedor = 'Louis ... '
   ....
#M5
   S: ganha a CPU e faz venceor = 'Sebastian ...'
....
'''


# Criando as threads:
try:
    vencedores = []
    pilotos = []

    # E se as velocidades acima estiverem muito próximas ...
    pilotos.append (threading.Thread(target=carro_f1, args=('Lewis Hamilton', 2.002, vencedores)))
    pilotos.append (threading.Thread(target=carro_f1, args=('Sebastian Vettel', 2.001, vencedores)))
    pilotos.append (threading.Thread(target=carro_f1, args=('Max Verstappen', 2.003, vencedores)))

    for piloto in pilotos:
        piloto.start()

    for piloto in pilotos:
        piloto.join()

    print (f"A ordem de chegada foi: {vencedores}")
except Exception as e:
    print('ERRO: nao foi possivel iniciar a corrida.', e)

