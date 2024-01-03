class Dekorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, x, y, a=1, *args):
        self.mathemthree = self.func(x, y) * a
        return self.mathemthree


@Dekorator
def delete(x, y):
    return x - y


print(delete(10, 5, 10))


class Counter:
    def __init__(self):
        self.counter = 0

    def __call__(self, step=1):
        self.counter += step
        return self.counter

    def zero(self):
        self.counter = 0

c = Counter()
c()
c()
print(c.counter)
c.zero()
c(5)
c(3)
print(c.counter)
