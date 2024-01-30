class CustomMap:
    class CustomMapIter:
        def __init__(self, iterable):
            self._iterable = iterable
            self.pointer = 0

        def __next__(self):
            if self.pointer == len(self._iterable._keys):
                raise StopIteration
            key = self._iterable._keys[self.pointer]
            value = self._iterable._dict[key]
            self.pointer += 1
            return (self._iterable.keys_func(key), self._iterable.values_func(value))

    def __init__(self, _dict: dict, keys_func: callable, values_func: callable) -> None:
        self._dict = _dict
        self._keys = list(self._dict.keys())
        self.keys_func = keys_func
        self.values_func = values_func

    def __iter__(self):
        return self.CustomMapIter(self)


data = {'apple': 1, 'banana': 2, 'cherry': 3}
key_func = lambda x: x.title()
value_func = lambda x: x ** 2

custom_map_iter = CustomMap(data, key_func, value_func)

for key, value in custom_map_iter:
    print(f"{key}: {value}")