# Generatorlar iterator oluşturmaya yaramaktadır.
# Bellekte yer kaplamayan iterator oluşturuculardır.
# Çok fazla olan verileri bellekte tutmadan oluşturmak için yararlıdır.

def calc_square():
    result = []

    for i in range(1, 6):
        result.append(i ** 2)

    return result


print(calc_square())


def generator_calc_square():
    for i in range(1, 6):
        yield i ** 2


generator = generator_calc_square()
print(generator)

iterator = iter(generator)
for i in iterator:
    print(i)

# Bir listeyi generator olarak oluşturmak.
listOne = [i * 3 for i in range(5)]
print(listOne)

generatorOne = (i * 3 for i in range(5))
iterator = iter(generatorOne)
print(next(iterator))

# Çarpım tablosunun generator ile oluşturulması.
def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            yield "{} x {} = {}".format(i, j, i * j)


for i in multiplication_table():
    print(i)