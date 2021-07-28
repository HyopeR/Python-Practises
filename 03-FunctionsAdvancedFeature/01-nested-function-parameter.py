# Fonksiyonlara çoklu parametre göndermek için args kullanırız
def argFunction(*args):
    for i in args:
        print(i)


argFunction(1, 2, 3)


def argFunction(name, *args):
    print(name)

    for i in args:
        print(i)


argFunction('John', 1, 2, 3)


# kwargs itemlere isim vererek göndermek için kullanılır
def kwargFunction(**kwargs):
    for i, j in kwargs.items():
        print(i, j)


kwargFunction(name="John", surname="Sun", no=123123)


# args and kwargs parametreleri birlikte kullanılabilir.
def combine(*args, **kwargs):
    for i in args:
        print(i)

    print('--------------')

    for i, j in kwargs.items():
        print(i, j)


combine(1, 2, 3, 4, 5, name="John", surname="Sun", no=123123)


