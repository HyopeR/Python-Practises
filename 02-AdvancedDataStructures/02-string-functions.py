# All String Methods -> https://www.tutorialspoint.com/python3/python_strings.htm

# Tüm karakterleri büyüt
print('python'.upper())

# Tüm karakterleri küçült
print('PYthon'.lower())

# Replace
print('Hello world!'.replace('world', 'Jupyter'))
print('Welcome name'.replace('name', 'John'))
print('Python Software Language'.replace(' ', '-'))

# String başlangıç ve bitişinde kontroller
print('Python'.startswith('py'))
print('Python'.lower().startswith('py'))
print('Python'.endswith('on'))

# String to List with split
str1 = 'Elma,Armut,Kiraz,Karpuz,Vişne'
list1 = str1.split(',')
print(list1)

print('Tolgahan Çelik'.split(' '))

# Stringler içerisindeki gereksiz karakterlerini temizlemek.

# Sağ ve sol
print("----------------Python----------------".strip('-'))

# Sol
print("----------------Python----------------".lstrip('-'))

# Sağ
print("----------------Python----------------".rstrip('-'))

# Listedeki elemanların her birinin yanına string eklemesi yap
list2 = ['21', '02', '2014']
print('/'.join(list2))

# Bir stringdeki karakterleri saydır
print('World is good place'.count('o'))
print('World is good place'.count('o', 5))

# String içerisinde arama ve index elde etmek

# Soldan aramaya başlar
print('World is good place'.find('good'))
print('World is good place'.find('better'))

# Sağdan aramaya başlar
print('World is good place'.rfind('good'))