from function import Function
import threading
import time

class Base():
    def __init__(self, max_threads):
        self.max_threads = max_threads
        self.func_list = []
        self.started_thread = []

    def add_function(self, func, args):
        func_r = Function(func,args)
        self.func_list.append(func_r)
        print(func_r.args)

    def execute(self):
        while(self.func_list):
            self._execute_threads(self.func_list)
            self._poll_started_thread()

    def _execute_threads(self, func_list):
        for i in range(self.max_threads - len(self.started_thread)):
            if  func_list:
                func = self.func_list.pop(0)
                thread = threading.Thread(target=func.func, args=(func.args))
                thread.start()
                self.started_thread.append(thread)

    def _poll_started_thread(self):
        for thread in self.started_thread[:]:
            if not thread.is_alive():
                print(f"Removing thread {thread}")
                self.started_thread.remove(thread)
            else:
                print(f"Thread {thread} is still alive")
                time.sleep(0.1)
