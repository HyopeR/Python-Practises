from tkinter import *
import urllib.request
import base64

class araclar(object):
   def __init__(self):
      arac = Tk()
   def buton(self, isim, olay):
      Btn = Button(text=isim, command=olay)
      Btn.pack(side="top",pady=3)
      Btn.config(width=20,height=3)
      
a=araclar()
URL = "https://img.webme.com/pic/c/creative-blog/Python-1.gif"
t = urllib.request.urlopen(URL)
raw_input = t.read()
t.close()
c = base64.encodestring(raw_input)
image = PhotoImage(data=c)
label = Label(image=image)


def gelir():
   fg=(int(input("Finansman gelirlerini giriniz:")))
   pg=(int(input("Pazar gelirlerini giriniz:")))
   kg=(int(input("Kira gelirlerini giriniz:")))
   tgel=fg+pg+kg
   print("Toplam geliriniz=", tgel)

def gider():
   ucret=(int(input("Ücret giderlerini giriniz:")))
   fg=(int(input("Finansman giderlerini giriniz:")))
   pg=(int(input("Pazar giderlerini giriniz:")))
   kg=(int(input("Kira giderlerini giriniz:")))
   mg=(int(input("Muhasebe giderlerini giriniz:")))
   tgid=ucret+fg+pg+kg+mg
   print("Toplam giderleriniz=", tgid)

def kar():
   tgel=(int(input("Toplam geliri giriniz:")))
   tgid=(int(input("Toplam gideri giriniz:")))
   tk=tgel-tgid
   print("Toplam karınız=",tk)
   if tk > 1000:
      print("İşletme karlılığı iyi durumda.")
   else:
      print("İşletme batıyor!")

def kullan():
   pus=(int(input("Planlanmış üretim süresini giriniz:")))
   pd=(int(input("Plansız duruşu giriniz:")))
   kul=(pus - pd)/pus
   print("Kullanılabilirlik oranınız=",kul)

def performans():
   scz=(int(input("Standart çevrim zamanını giriniz:")))
   um=(int(input("Üretim miktarını giriniz:")))
   pus=(int(input("Planlanmış üretim süresini giriniz:")))
   pd=(int(input("Plansız duruşu giriniz:")))
   per=(scz*um)/(pus-pd)
   print("Performans oranınız=",per)

def kalite():
   sm=(int(input("Sağlam ürün miktarını giriniz:")))
   tu=(int(input("Toplam üretim miktarını giriniz:")))
   kal=sm/tu
   print("Kalite oranınız=",kal)

def oee():
   kul=(int(input("Kullanılabilirlik oranınızı giriniz:")))
   pr=(int(input("Performans oranınızı giriniz:")))
   kal=(int(input("Kalite oranınızı giriniz:")))
   oran=100/100
   eeo=kul*pr*kal*oran
   print("İşletmenin ekipman etkinlik oranı=",eeo)

def ciro():
   sm=(int(input("Satış miktarını giriniz:")))
   bsf=(int(input("Birim satış fiyatını giriniz:")))
   tc=sm*bsf
   print("Toplam cironuz=",tc)

def abasiciro():
   tc=(int(input("Toplam cironuzu giriniz:")))
   tcs=25
   abc=tc/tcs
   print("Adam başı cironuz=",abc)

label.pack()
a.buton("Toplam Gelir",gelir)
a.buton("Toplam Gider",gider)
a.buton("Kar",kar)
a.buton("Kullanılabilirlik Oranı",kullan)
a.buton("Performans Oranı",performans)
a.buton("Kalite Oranı",kalite)
a.buton("Ekipman Etkinlik Oranı",oee)
a.buton("Toplam Ciro",ciro)
a.buton("Adam Başı Ciro",abasiciro)

mainloop()
