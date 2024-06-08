import time
import inspect

class Timer:
    def __init__(self):
        self._func_name = inspect.stack()[1].function
        self._start_time = time.time_ns()

    def tick(self):
        end_time = time.time_ns()
        print(f"qihe time tracking:: {self._func_name}@@{(end_time - self._start_time) // 1_000_000.0} ms")

