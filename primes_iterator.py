class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def get_next(self):

        i = 2
        while i < self.current:
            if self.current % i == 0:
                self.current += 1
                return self.get_next()

            i += 1

        return self.current

    def __next__(self):
        if self.current == 1:
            self.current += 1
            return 1
        if self.current == 2:
            self.current += 1
            return 2

        if self.current > self.n:
            raise StopIteration

        res = self.get_next()
        self.current += 1
        return res


prime_iterator = PrimeIterator(50)
iterator = iter(prime_iterator)
print(next(iterator))
