from function import Function
from queue import PriorityQueue
import threading
import time

class Base():
    #Base class to execute thread and poll threads
    def __init__(self, max_threads):
        self.max_threads = max_threads
        self.func_list = PriorityQueue()
        self.started_thread = []

    def add_function(self, func, args, priority):
        func_r = Function(func,args, priority)
        self.func_list.put(func_r) #Put functions in priority queue by comparing func objects based on priority (min heap)
        print(func_r.args)

    def execute(self):
        while not self.func_list.empty():
            self._execute_threads(self.func_list)
            self._poll_started_thread()

    def _execute_threads(self, func_list):
        for i in range(self.max_threads - len(self.started_thread)):
            if not func_list.empty():
                func = self.func_list.get()
                thread = threading.Thread(target=func.func, args=(func.args))
                thread.start()
                self.started_thread.append(thread)

    def _poll_started_thread(self):
        for thread in self.started_thread[:]:
            if not thread.is_alive():
                print(f"Removing thread {thread}")
                self.started_thread.remove(thread)
            else:
                #print(f"Thread {thread} is still alive")
                time.sleep(0.1)
