class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        else:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return result


fib = Fibonacci(10)


for num in fib:
    print(num)
