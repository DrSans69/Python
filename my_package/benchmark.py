from sys import stdout
from time import perf_counter


def benchmark(iters=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            all = 0
            for i in range(iters):
                start_time = perf_counter()
                func(*args, **kwargs)
                stop_time = perf_counter()
                all += stop_time - start_time
            stdout.write(str(all / iters))
        return wrapper
    return decorator
