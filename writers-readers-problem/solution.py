# |---------------------------------------------------------------------------------------------------------------------|
# |Problema - Leitores/Escritores - Implementação por Gabriel Lima (github.com/gabrielSantosLima)                       |
# |--------------------------|------------------------------------------------------------------------------------------|
# |Resumo: Problema que surge quando possuímos Threads leitoras e escritoras que compartilham determinado recurso (BD,  |
# |arquivos, estruturas de dados, etc). Portanto surge a questão: devemos bloquear todas as Threads leitoras quando uma |
# |Thread de leitura está executando? A resposta é não, uma vez que uma Thread não realiza escrita e atualização do RC  |
# |(recurso compartilhado). Porém, esse problema é identificado quando uma thread de leitura e outra de escrita precisam|
# |executar concorrentemente, fazendo necessário a utilização de semáforos.                                             |
# ----------------------------------------------------------------------------------------------------------------------|
from threading import Thread, Semaphore
from time import sleep

from utils import sort_daily_task

poem = []
readerSemaphore = Semaphore()
writerSemaphore = Semaphore()
resourceSemaphore = Semaphore()
queueSemaphore = Semaphore()
lenghtOfReaders = 0
lenghtOfWriters = 0


def execute_reader_thread(thread_title="Padrão"):
    global poem, readerSemaphore, writerSemaphore, lenghtOfReaders, resourceSemaphore, queueSemaphore
    while True:
        queueSemaphore.acquire()
        readerSemaphore.acquire()
        lenghtOfReaders += 1
        if lenghtOfReaders == 1:
            print("Locking writer")
            resourceSemaphore.acquire()
        readerSemaphore.release()
        queueSemaphore.release()

        sleep(1)
        print(f"[Reader - {thread_title}] Reading...")
        for day, task in poem:
            print(f"> Task of {day} is '{task}'")

        readerSemaphore.acquire()
        lenghtOfReaders -= 1
        if lenghtOfReaders == 0:
            print("Releasing writer")
            resourceSemaphore.release()
        readerSemaphore.release()


def execute_writer_thread():
    global poem, writerSemaphore, queueSemaphore, lenghtOfWriters, resourceSemaphore
    while True:
        writerSemaphore.acquire()
        lenghtOfWriters += 1
        if lenghtOfWriters == 1:
            queueSemaphore.acquire()
        writerSemaphore.release()

        resourceSemaphore.acquire()
        sleep(1)
        print("[Writer] Writing...")
        if len(poem) == 7:
            poem = []
        daily_task = sort_daily_task()
        poem.append(daily_task)
        resourceSemaphore.release()

        writerSemaphore.acquire()
        lenghtOfWriters -= 1
        if lenghtOfWriters == 0:
            queueSemaphore.release()
        writerSemaphore.release()


def main():
    reader = Thread(target=execute_reader_thread, args=["1"])
    another_reader = Thread(target=execute_reader_thread, args=["2"])
    writer = Thread(target=execute_writer_thread)
    reader.start()
    another_reader.start()
    writer.start()


main()
