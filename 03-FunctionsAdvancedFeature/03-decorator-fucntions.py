import time


# Aşağıdaki 2 fonksiyondada zamanı saydırmak için bir kodu tekrarladık.
# Bu gibi durumlarda decorator fonksiyonlar yazarak birden fazla kodda
# kullandığımız satırları tek bir fonksiyonda halledebiliriz. Piece a Cake


def calculate_square(numbers):
    total = list()
    starting_time = time.time()

    for i in numbers:
        total.append(i ** 2)

    finishing_time = time.time()
    print("Square Time: {}".format(finishing_time - starting_time))

    return total


def calculate_cube(numbers):
    total = list()
    starting_time = time.time()

    for i in numbers:
        total.append(i ** 3)

    finishing_time = time.time()
    print("Cube Time: {}".format(finishing_time - starting_time))
    return total


# calculate_square(range(100000))
# calculate_cube(range(100000))

# DECORATOR FONKSIYOUNUNDA WRAPPER OLMASI GEREKIR
def calculate_time(func):
    def wrapper(numbers):
        starting_time = time.time()

        result = func(numbers)

        finishing_time = time.time()
        print("{} Time: {} seconds".format(func.__name__, finishing_time - starting_time))
        return result

    return wrapper


@calculate_time
def calculate_square_2(numbers):
    total = list()

    for i in numbers:
        total.append(i ** 2)

    return total


@calculate_time
def calculate_cube_2(numbers):
    total = list()

    for i in numbers:
        total.append(i ** 3)

    return total


calculate_square_2(range(100000))
calculate_cube_2(range(100000))