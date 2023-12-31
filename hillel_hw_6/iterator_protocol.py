# 1. Створити frange ітератор. Який буде працювати з float.

class frange:
    def __init__(self, start, stop=None, step=1.0):
        self.start = start
        self.step = step
        self.stop = stop
        if self.stop is None:
            self.start, self.stop = 0.0, self.start
        self._current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        current = self._current
        if self.step > 0 and current >= self.stop:
            raise StopIteration()
        elif self.step < 0 and current <= self.stop:
            raise StopIteration()
        else:
            self._current += self.step
        return current



# Перевірка за допомогою assert
assert(list(frange(5)) == [0, 1, 2, 3, 4])
assert(list(frange(2, 5)) == [2, 3, 4])
assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert(list(frange(1, 5)) == [1, 2, 3, 4])
assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(frange(0, 0)) == [])
assert(list(frange(100, 0)) == [])

print('SUCCESS!')