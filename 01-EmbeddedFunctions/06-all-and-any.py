# Bütün değerlerin hepsinin True olması durumunda true
# Bütün değerlerden sadece birinin True olması durumunda true

listOne = [True, True, True, False, True]

print(all(listOne))
print(any(listOne))