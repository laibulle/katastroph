
import threading
from concurrent.futures import ThreadPoolExecutor

SALUT_STRING = "Salut "
TOTO_STRING = "Toto "

def alternating_salut_toto(repetitions: int) -> str:
    printer = SalutTotoPrinter(repetitions)
    printer.start()
    return printer.res[::-1]


class SalutTotoPrinter:
    def __init__(self, repetitions: int):
        self.thread_lock = threading.Lock()
        self.res = ""
        self.next_value = SALUT_STRING
        self.current_index = 0
        self.repetitions = repetitions

    def start(self):
        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(self.print_salut_thread)
            executor.submit(self.print_toto_thread)

    def set_next_print(self) -> None:
        self.thread_lock.acquire()
        self.res = self.res + self.next_value
        print(self.res)
        if self.next_value == SALUT_STRING:
            self.next_value = TOTO_STRING
            self.current_index += 1
        else:
            self.next_value = SALUT_STRING
        self.thread_lock.release()

    def print_salut_thread(self) -> None:
        while self.not_finished():
            if self.next_value == SALUT_STRING:
                self.set_next_print()

    def print_toto_thread(self) -> None:
        while self.not_finished():
            if self.next_value == TOTO_STRING:
                self.set_next_print()

    def not_finished(self) -> bool:
        return self.current_index < self.repetitions


