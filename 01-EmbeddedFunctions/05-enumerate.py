# Sadece elemanların olduğu bir listede index verilerine ihtiyaç duyduğumuzda
# kullanışlıdır.

default_list = ['Elma', 'Armut', 'Karpuz', 'Çilek']

# Böylece hem değer, hemde index'e erişebiliriz.
print(list(enumerate(default_list)))

for i,j in enumerate(default_list):
    print("""Index: {}\nItem: {}""".format(i, j))