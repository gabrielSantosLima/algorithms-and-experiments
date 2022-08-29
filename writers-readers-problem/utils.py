from random import randint

tasks = ["Ajudar em casa", "Estudar SO", "Estudar FTC",
         "Estudar PP", "Estudar PE", "Estudar AED1", "Estudar ED1"]
weekdays = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]


def sort_daily_task() -> str:
    task_index = randint(0, len(tasks) - 1)
    day_index = randint(0, len(weekdays) - 1)
    return weekdays[day_index], tasks[task_index]
