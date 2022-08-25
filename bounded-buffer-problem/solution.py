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
# Biblioteca do Python para utilizar a funcionalidade de Threads
from threading import Thread, Semaphore
from time import sleep  # Biblioteca do Python para utilizar funcionalidades de tempo
# Arquivo local que possui funções de utilidade
from utils import get_cancao_do_exilio


isEOF = False
poem = []
semaphore = Semaphore()
full = Semaphore(0)
empty = Semaphore(5)


def execute_producer_thread(text: str):
    global isEOF, poem, empty, full, semaphore
    splitted_text = text.split(' ')
    for text_set in splitted_text:
        print('[Producer] Current State: ' + str(poem))
        empty.acquire()
        semaphore.acquire()
        poem.append(text_set + ' ')
        sleep(0.5)
        semaphore.release()
        full.release()
    isEOF = True


def execute_consumer_thread():
    global isEOF, poem, empty, full, semaphore
    result = ''
    while not isEOF or len(poem) > 0:
        print('[Consumer] Current State: ' + str(poem))
        full.acquire()
        semaphore.acquire()
        result += poem[0]
        sleep(0.5)
        poem.pop(0)
        semaphore.release()
        empty.release()
    print(result)


def main():
    poem_text = get_cancao_do_exilio()
    producer = Thread(target=execute_producer_thread,
                      args=[poem_text])
    consumer = Thread(target=execute_consumer_thread)
    producer.start()
    consumer.start()


main()
