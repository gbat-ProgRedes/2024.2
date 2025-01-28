# Threads - faz em "paralelo", programa principal aguarda.
#           Agora temos um vencedor. Será?
import threading, time

def carro_f1 (nome_piloto, velocidade):
    global vencedor
    lck.acquire()
    voltas = 0
    while voltas < 5:
        time.sleep(1/velocidade)
        voltas += 1
        print(f'{nome_piloto[0]}{voltas:02d}', end='.')

    print (f"\n{nome_piloto} concluiu a prova!!!")
    if vencedor == None:
        vencedor = nome_piloto
    lck.release()

# Criando as threads:
try:
    vencedor = None
    pilotos = []
    lck = threading.Lock()

    # E se as velocidades acima estiverem muito próximas ...
    pilotos.append (threading.Thread(target=carro_f1, args=('Lewis Hamilton', 2.002)))
    pilotos.append (threading.Thread(target=carro_f1, args=('Sebastian Vettel', 2.001)))
    pilotos.append (threading.Thread(target=carro_f1, args=('Max Verstappen', 2.003)))

    for piloto in pilotos:
        piloto.start()

    for piloto in pilotos:
        piloto.join()

    print (f"A prova terminou ....{vencedor} VENCEEEUUUU!!!")
except Exception as e:
    print('ERRO: nao foi possivel iniciar a corrida.', e)

