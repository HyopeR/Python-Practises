# Iterator
class Force3():
    def __init__(self, maximum=0):

        self.maximum = maximum
        self.force = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.force <= self.maximum:
            result = 3 ** self.force
            self.force += 1

            return result
        else:
            self.force = 0
            raise StopIteration


force = Force3(6)

for i in force:
    print(i)

for j in force:
    print(j)


# Generator
def fibonacci():
    a = 1
    b = 1
    yield a
    yield b

    while True:
        a, b = b, a + b
        yield b

for num in fibonacci():
    if num > 100000:
        break
    else:
        print(num)
