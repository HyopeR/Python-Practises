# Localization datetime
import locale
from datetime import datetime
locale.setlocale(locale.LC_ALL, "")


print(datetime.now())

now = datetime.now()
print(datetime.ctime(now))
print("{}-{}-{}".format(now.year, now.month, now.day))

# Datetime içerisinde ay, gün isimleri almak için strftime() kullanılır.
print("Yıl Bilgisi", datetime.strftime(now, "%Y"))
print("Ay İsmi", datetime.strftime(now, "%B"))
print("Gün İsmi", datetime.strftime(now, "%A"))
print("Saat Bilgisi", datetime.strftime(now, "%X"))
print("Gün Bilgisi", datetime.strftime(now, "%D"))
print("Combine", datetime.strftime(now, "%B %Y"))

# Timestamp İşlemleri

# Date convert to Timestamp
timestamp = datetime.timestamp(now)
print(timestamp)

# Timestamp convert to Date
date = datetime.fromtimestamp(timestamp)
print(date)


# İki tarih arasındaki farkı bulmak
dateNow = datetime.now()
dateOld = datetime(2019, 12, 1)

print(dateNow - dateOld)
