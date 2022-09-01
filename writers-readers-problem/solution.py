# |---------------------------------------------------------------------------------------------------------------------|
# |Problema - Leitores/Escritores - Implementação por Gabriel Lima (github.com/gabrielSantosLima)                       |
# |--------------------------|------------------------------------------------------------------------------------------|
# |Resumo: Problema que surge quando possuímos Threads leitoras e escritoras que compartilham determinado recurso (BD,  |
# |arquivos, estruturas de dados, etc). Portanto surge a questão: devemos bloquear todas as Threads leitoras quando uma |
# |Thread de leitura está executando? A resposta é não, uma vez que uma Thread não realiza escrita e atualização do RC  |
# |(recurso compartilhado). Porém, esse problema é identificado quando uma thread de leitura e outra de escrita precisam|
# |executar concorrentemente, fazendo necessário a utilização de semáforos.                                             |
# ----------------------------------------------------------------------------------------------------------------------|
from threading import Semaphore, Thread
from time import sleep

from utils import sort_daily_task

daily_tasks = []
reader_semaphore = Semaphore()
writer_semaphore = Semaphore()
resource_semaphore = Semaphore()
queue_semaphore = Semaphore()
readers_length = 0
writers_length = 0


def execute_reader_thread(thread_title="Padrão"):
    global daily_tasks, reader_semaphore, writer_semaphore, readers_length, resource_semaphore, queue_semaphore
    while True:
        queue_semaphore.acquire()
        reader_semaphore.acquire()
        readers_length += 1
        if readers_length == 1:
            print("Locking writer")
            resource_semaphore.acquire()
        reader_semaphore.release()
        queue_semaphore.release()

        sleep(1)
        print(f"[Reader - {thread_title}] Reading...")
        for day, task in daily_tasks:
            print(f"> Task of {day} is '{task}'")

        reader_semaphore.acquire()
        readers_length -= 1
        if readers_length == 0:
            print("Releasing writer")
            resource_semaphore.release()
        reader_semaphore.release()


def execute_writer_thread():
    global daily_tasks, writer_semaphore, queue_semaphore, writers_length, resource_semaphore
    while True:
        writer_semaphore.acquire()
        writers_length += 1
        if writers_length == 1:
            queue_semaphore.acquire()
        writer_semaphore.release()

        resource_semaphore.acquire()
        sleep(1)
        print("[Writer] Writing...")
        if len(daily_tasks) == 7:
            daily_tasks = []
        daily_task = sort_daily_task()
        daily_tasks.append(daily_task)
        resource_semaphore.release()

        writer_semaphore.acquire()
        writers_length -= 1
        if writers_length == 0:
            queue_semaphore.release()
        writer_semaphore.release()
        sleep(1)


def main():
    reader = Thread(target=execute_reader_thread, args=["1"])
    another_reader = Thread(target=execute_reader_thread, args=["2"])
    writer = Thread(target=execute_writer_thread)
    reader.start()
    another_reader.start()
    writer.start()


main()
