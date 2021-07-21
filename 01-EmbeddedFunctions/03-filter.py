# Liste, demet vb verilere uygulanır.
# İçerisine aldığı  fonksiyon boolean döndürmek zorundadır.

list_default = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(lambda x: x % 2 == 0, list_default)))

def isPrimeNumber(x):
    minPrimeNumber = 2

    if (x == 1):
        return False
    elif (x == 2):
        return True
    else:
        while(minPrimeNumber < x):
            if (x % minPrimeNumber == 0):
                return False
            minPrimeNumber += 1
        return True

print(isPrimeNumber(7))
print(isPrimeNumber(100))

print(list(filter(isPrimeNumber, range(1, 100))))