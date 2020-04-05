x = (i for i in range(5))
x.__next__()
x.__next__()
for i in x:
    print(i)


class Range_example:
    def __init__(self, end, step):
        self.current = 0
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration()

        else:
            return_val = self.current
            self.current += self.step
            return return_val
