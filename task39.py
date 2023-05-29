import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if self.start_time is not None:
            end_time = time.time()
            self.elapsed_time += end_time - self.start_time
            self.start_time = None

    def reset(self):
        self.elapsed_time = 0
        self.start_time = None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()


with Timer() as t:
    time.sleep(1)
print(t.elapsed_time)
time.sleep(1)
with t:
    time.sleep(2)
print(t.elapsed_time)

with Timer() as t2:
    time.sleep(1)
print(t2.elapsed_time)
t2.reset()
with t2:
    time.sleep(2)
print(t2.elapsed_time)