# Listeleri gruplamaya yaramaktadır.

# Zip fonksiyonu olmadan liste gruplamak???
listOne = [1,2,3,4,5]
listTwo = [10,20,30,40,50]
listThree = ["A", "B", "C", "D", "F"]

i = 0
resultList = []
while (i < len(listOne) or i < len(listTwo)):
    resultList.append((listOne[i], listTwo[i]))
    i += 1

print(resultList)

# Zip kullanarak
print(list(zip(listOne, listTwo)))
print(list(zip(listOne, listTwo, listThree)))


# Döngü ile kullanım
for i,j in zip(listOne, listThree):
    print(i, j)

# Birden çok sözlük veri tipiyle veri kullanarak değerlerine erişmek
dictionaryOne = {'Elma': 1, 'Armut': 2, 'Kiraz': 3}
dictionaryTwo = {'Sıfır': 0, 'Bir': 1, 'İki': 2}

print(list(zip(dictionaryOne, dictionaryTwo)))
print(list(zip(dictionaryOne.values(), dictionaryTwo.values())))

