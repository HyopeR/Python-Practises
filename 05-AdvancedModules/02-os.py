import os
from datetime import datetime
# print(dir(os))

# Bulunduğumuz dizini getir
print(os.getcwd())

# Dizin değiştirmek
# os.chdir("C:/Users/tol_c/Desktop/PythonReminders")

# Dizindeki dosyaları listelemek
# print(os.listdir())

# Bulunulan dizinde klasör oluşturmak
# os.mkdir("02-os-file")
# os.makedirs("02-os-file/inside")

# Klasör silmek
# os.rmdir("02-os-file")
# os.removedirs("02-os-file/inside")

# Yeniden isimlendirmek
# os.mkdir("02-os-file")
# os.rename("02-os-file", "try")
# print(os.stat("try"))
# print(os.stat("try").st_mtime)
# print(datetime.fromtimestamp(os.stat("try").st_mtime))

# Klasörleri tek tek gezerek bir array getirmek
# generator = os.walk("C:/Users/tol_c/Desktop/PythonReminders")
# for folder_path, folder_name, file_name in generator:
#     print("Folder Path: ", folder_path)
#     print("Folder Name: ", folder_name)
#     print("File Name: ", file_name)
#     print("***********************")