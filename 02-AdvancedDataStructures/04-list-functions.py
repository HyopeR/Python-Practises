list1 = [1,2,3,4,5]

# Eleman eklemek
list1.append(6)
print(list1)

# Bir listeyi başka bir listeyle genişlet
list1.extend([7,8,9])
print(list1)

# Index belirterek eleman eklemek
list1.insert(0, 0)
print(list1)

# Listeden eleman sil index ile
list1.pop()
print(list1)

list1.pop(0)
print(list1)

# Listeden eleman sil değer ile
list1.remove(1)
print(list1)

# Listeden eleman indexi bul değer ile
print(list1.index(5))

# Değerin listede kaç defa geçtiğini bulmak
print(list1.count(5))

# Listenin elemanlarını sıralamak
list1.sort()
list1.sort(reverse=True)