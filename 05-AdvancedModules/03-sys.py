import sys

# Programı sonlandırmak
# a = int(input("a:"))
# sys.exit()
# b = int(input("b:"))

# Sys input, output, error olaylarının kontrolü
# sys.stderr.write("Bu bir hata mesajıdır!\n")
# sys.stderr.flush()
#
# sys.stdout.write("Bu normal bir yazıdır.\n")

# Terminal üzerinden dosyayı çalıştırırken ekstra paremetler geçerek
# Sys modulü ile bunları yakalayabiliriz.
print(sys.argv)

def calc_root(a, b, c):
    delta = b ** 2 - 4 * a * c

    if (delta < 0):
        print("Reel kök yok.")
    else:
        x1 = (-b - delta ** 0.5) / (2*a)
        x2 = (-b + delta ** 0.5) / (2*a)
        return x1, x2

if len(sys.argv) == 4:
    print("Root: ", calc_root(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
else:
    sys.stderr.write("Lütfen doğru değerler girin!")
    sys.stderr.flush()