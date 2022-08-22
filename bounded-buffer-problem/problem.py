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
from utils import close_poem, get_cancao_do_exilio, open_poem

MAX_STACKS = 4
FILENAME = "poem.txt"

isEOF = False


def execute_producer_thread(text: str):
    global isEOF
    file = open_poem(FILENAME, 'w')
    lines = text.split('\n')
    for line in lines:
        file_data = file.read()
        current_rows_length = len(file_data.split('\n'))
        while current_rows_length == MAX_STACKS:
            file_data = file.read()
            current_rows_length = len(file_data.split('\n'))
        file.write(line)
    isEOF = True
    close_poem(file)


def execute_consumer_thread():
    global isEOF
    file = open_poem(FILENAME, 'r')
    file_data = file.read()
    current_rows_length = len(file_data.split('\n'))
    while not isEOF:
        while current_rows_length == 1:
            file_data = file.read()
            current_rows_length = len(file_data.split('\n'))
        print(file_data)
    close_poem(file)


def main():
    poem = get_cancao_do_exilio()
    producer = Thread(target=execute_producer_thread,
                      args=[poem])
    consumer = Thread(target=execute_consumer_thread)
    producer.start()
    consumer.start()


main()
