from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

# First solution time - 5 mins, but now working with large nums
@timeit
def simple_sum_of_intervals(intervals):
    res = []
    for start, end in intervals:
        for num in range(start, end):
            res.append(num)

    return len(set(res))


# Second solution time - 23 mins
@timeit
def normal_sum_of_intervals(intervals):
    sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
    curr_start, curr_end = sorted_intervals[0]
    res = 0
    for start, end in sorted_intervals[1:]:
        if start <= curr_end:
            curr_end = max(curr_end, end)
        else:
            res += curr_end - curr_start
            curr_start, curr_end = start, end
    else:
        res += curr_end - curr_start

    return res



assert (simple_sum_of_intervals([(1, 5)]) == 4)
assert (simple_sum_of_intervals([(1, 5), (6, 10)]) == 8)
assert (simple_sum_of_intervals([(1, 5), (1, 5)]) == 4)
assert (simple_sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7)
# PC crashing XD
# assert (simple_sum_of_intervals([(-1_000_000_000, 1_000_000_000)]) == 2_000_000_000)
# assert (simple_sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]) == 100_000_030)

assert (normal_sum_of_intervals([(1, 5)]) == 4)
assert (normal_sum_of_intervals([(1, 5), (6, 10)]) == 8)
assert (normal_sum_of_intervals([(1, 5), (1, 5)]) == 4)
assert (normal_sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7)
assert (normal_sum_of_intervals([(-1_000_000_000, 1_000_000_000)]) == 2_000_000_000)
assert (normal_sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]) == 100_000_030)