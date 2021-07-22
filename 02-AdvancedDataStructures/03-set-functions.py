# Kümeler içerisindeki elemanlar Unique'dır.

stack = {1, 2, 3}
print(type(stack))

list1 = [1, 2, 3, 1, 1, 1, 3, 2, 4, 1, 1, 2]
stack1 = set(list1)

for i in stack1:
    print(i)

print(set('Python Programmer'))

# 2 küme içerisindeki farklı değerleri elde etmek
stack2 = { 1, 2, 3, 4, 5}
stack3 = { 3, 4, 5, 6, 7}
print(stack2.difference(stack3))

# Stack2'nin stack3'den farkını stack2'ye atamak
stack2.difference_update(stack3)
print(stack2)

# küme içerisine eleman eklemek
stack2.add(1)
stack2.add(6)
print(stack2)

# küme içerisinden eleman silmek
stack2.discard(1)
stack2.discard(100)
print(stack2)

# Kümelerin ortak elemanlarını bulmak
stack2 = { 1, 2, 3, 4, 5}
stack3 = { 3, 4, 5, 6, 7}

print(stack2.intersection(stack3))
stack2.intersection_update(stack3)
print(stack2)

# İki kümenin kesişimi boş küme mi?
print(stack2.isdisjoint(stack3))

# Birinci küme ikinci kümenin alt kümesi mi?
print(stack2.issubset(stack3))

# İki kümeyi birleştirmek
print(stack2.union(stack3))
stack2.update(stack3)
print(stack2)