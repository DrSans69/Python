from time import perf_counter
    
def benchmark(iter: int = 1) -> callable:
    def decorator(func: callable) -> callable:
        def wrapper(*args, **kwargs):
            all = 0
            for i in range(iters):
                start_time = perf_counter()
                func(*args, **kwargs)
                stop_time = perf_counter()
                all += stop_time - start_time
            print(all / iters)
        return wrapper
    return decorator
