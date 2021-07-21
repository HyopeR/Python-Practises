# Map fonksiyonu hakkında açıklamaya gerek yok biliyorsunuz

default_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ayrı fonksiyon tanımlamalı kullanım.
def double(x):
    return x ** 2

print('Düz kullanım: ', list(map(double, default_list)))

# Lambda ile kullanım
print('Lamda kullanım: ', list(map(lambda x: x ** 2, default_list)))

# Çok parametreli lambda kullanım
list_one = [1, 2, 3, 4]
list_two = [5, 6, 7, 8]

print(list(map(lambda x, y: x * y, list_one, list_two)))
