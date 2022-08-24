# |---------------------------------------------------------------------------------------------------------------------|
# |Problema - Bounded Buffer - Implementação por Gabriel Lima (github.com/gabrielSantosLima)                            |
# |--------------------------|------------------------------------------------------------------------------------------|
# |Resumo: Há dois ou mais processos que concorrem pelo acesso a um mesmo buffer limitado. Na estratégia                |
# |produtos/consumidor:                                                                                                 |
# | 1. O produtor produz informações que são colocados no buffer                                                        |
# | 2. O Consumidor consome as informações do buffer                                                                    |
# |Caso as Threads não estejam sincronizadas, o processo de produção/consumo pode entrar em conflito. Sendo necessário a|
# |utilização de Semáforos.                                                                                             |
# ----------------------------------------------------------------------------------------------------------------------|
from threading import Thread
from time import sleep
from utils import get_cancao_do_exilio

MAX_STACKS = 5

isEOF = False
poem = []


def execute_producer_thread(text: str):
    global isEOF, poem
    splitted_text = text.split(' ')
    for text_set in splitted_text:
        print('[Producer] Current State: ' + str(poem))
        while len(poem) == MAX_STACKS:
            print("[Producer] Awaiting...")
        poem.append(text_set + ' ')
        sleep(0.5)
    isEOF = True


def execute_consumer_thread():
    global isEOF, poem
    result = ''
    while not isEOF or len(poem) > 0:
        print('[Consumer] Current State: ' + str(poem))
        while len(poem) == 0:
            print("[Consumer] Awaiting...")
        result += poem[0]
        sleep(0.5)
        poem.pop(0)
    print(result)


def main():
    poem_text = get_cancao_do_exilio()
    producer = Thread(target=execute_producer_thread,
                      args=[poem_text])
    consumer = Thread(target=execute_consumer_thread)
    producer.start()
    consumer.start()


main()
