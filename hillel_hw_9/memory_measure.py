import tracemalloc
import functools


def separate_output(func):
    def wrapper(*args, **kwargs):
        print("-" * 30)
        result = func(*args, **kwargs)
        print("-" * 30)
        return result
    return wrapper


def memory_usage(func):
    @functools.wraps(func)
    @separate_output
    def wrapper(*args, **kwargs):
        tracemalloc.start()

        result = func(*args, **kwargs)

        current, peak = tracemalloc.get_traced_memory()

        tracemalloc.stop()
        print(f"\033[0mFunction Name       :\033[35;1m {func.__name__}\033[0m")
        print(f"\033[0mCurrent memory usage:\033[36m {current / 10 ** 6}MB\033[0m")
        print(f"\033[0mPeak                :\033[36m {peak / 10 ** 6}MB\033[0m")

        return result
    return wrapper


@memory_usage
def method(n=2, /):
    return list(range(10*n))


method()
method(10)
method(100)
method(1000)
method(10000)
