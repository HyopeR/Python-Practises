# Birike birike ilerleyen aritmatik işlemler gerçekleştirilebilir
# Sonuçta tek bir sonuç döndürülür

from functools import reduce

default_list = [12, 18, 20, 10]

# Normal yazım
def addition(x, y):
    return x + y

print(reduce(addition, default_list))

# Lamda yazım
# Örneğin bu şekilde faktöriyel hesaplamak için kullanılabilir
print(reduce(lambda x,y : x * y, [1,2,3,4,5]))

# Örndeğin bir listede bulunan maksimum değeri bulmak için kullanılabilir
print(reduce(lambda x,y : x if x > y else y, [-10, 25, 11, -1, -2, 25.5]))