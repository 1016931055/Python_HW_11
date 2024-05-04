class GeomRange:
    def __init__(self, *args):
        if len(args) == 1:
            self.start = 1
            self.stop = args[0]
            self.step = 2
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 2
        else:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]

    def __iter__(self):
        return self.GeomRangeIterator(self.start, self.stop, self.step)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError("index cannot be negative")

        value = self.start * (self.step ** index)
        if value < self.stop:
            return value
        else:
            raise IndexError("index is out of the progression")

    class GeomRangeIterator:
        def __init__(self, start, stop, step):
            self.start = start
            self.stop = stop
            self.step = step
            self.current = start

        def __next__(self):
            if self.current < self.stop:
                result = self.current
                self.current *= self.step
                return result
            else:
                raise StopIteration