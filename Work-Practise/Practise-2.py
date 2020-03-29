from tkinter import *
from tkinter import ttk
import urllib.request
import base64

class araclar(object):
   def __init__(self):
      arac = Tk()
      arac.title("Simple Prog")
   def buton(self, isim, olay):
      Btn = Button(text=isim, command=olay)
      Btn.pack(side="top",pady=3)
      Btn.config(width=26,height=2)
      
a=araclar()
resim1 = "https://img.webme.com/pic/c/creative-blog/Python-2.gif"
t1 = urllib.request.urlopen(resim1)
raw_input = t1.read()
t1.close()
c1 = base64.encodestring(raw_input)
image1 = PhotoImage(data=c1)
label1 = Label(image=image1)

resim2 = "https://img.webme.com/pic/c/creative-blog/Python-3.gif"
t2 = urllib.request.urlopen(resim2)
raw_input = t2.read()
t2.close()
c2 = base64.encodestring(raw_input)
image2 = PhotoImage(data=c2)
label2 = Label(image=image2)

resim3 = "https://img.webme.com/pic/c/creative-blog/Python-4.gif"
t3 = urllib.request.urlopen(resim3)
raw_input = t3.read()
t3.close()
c3 = base64.encodestring(raw_input)
image3 = PhotoImage(data=c3)
label3 = Label(image=image3)

resim4 = "https://img.webme.com/pic/c/creative-blog/Python-5.gif"
t4 = urllib.request.urlopen(resim4)
raw_input = t4.read()
t4.close()
c4 = base64.encodestring(raw_input)
image4 = PhotoImage(data=c4)
label4 = Label(image=image4)


def katmaDC():
    global kdc
    tsm=int(input("Toplam satış miktarını giriniz:"))
    hmm=int(input("Hammadde maliyetini giriniz:"))
    bog=int(input("Bakım onarım giderlerini giriniz:"))
    sg=int(input("Sevkiyat gidelerini giriniz:"))
    sahg=int(input("Satın alınan hizmet giderlerini giriniz:"))
    kdc=tsm-(hmm+bog+sg+sahg)
    print("İşletme katma değer cironuz=",kdc)
    if kdc>=1000:
        print("İşletme katma değer cironuz yüksek.")
    elif 500<kdc<999:
        print("İşletme katma değer cironuz normal.")
    else:
        print("İşletme katma değer cironuz düşük.")

def mcs2016():
    global mcs6
    cs=170
    tms=50
    mcs6=cs/tms
    print("2016 müşteri çalışma süresi=",mcs6)

def mcs2017():
    global mcs7
    cs=220
    tms=70
    mcs7=cs/tms
    print("2017 müşteri çalışma süresi=",mcs7)

def mcsfark():
    mcsf=mcs7-mcs6
    print("2017 ve 2016 arasındaki fark=",mcsf)

def ilk6ay():
   global ilkay
   yg=int(input("Yazılım gelirinizi giriniz:"))
   fg=int(input("Finansman gelirinizi giriniz:"))
   usg=int(input("Ürün satış gelirinizi giriniz:"))
   cm=int(input("Toplam çalışan maaşlarını giriniz:"))
   kg=int(input("Kira giderlerinizi giriniz:"))
   dm=int(input("Donanım maliyetlerinizi giriniz:"))
   ilkay=(yg+fg+usg)-(cm+kg+dm)
   gelirKalemi=yg+fg+usg
   giderKalemi=cm+kg+dm
   if (ilkay>0):
      print("İlk 6 aylık geliriniz:", gelirKalemi)
      print("İlk 6 aylık gideriniz:", giderKalemi)
      print("İlk 6 aylık karınız:", ilkay)
   elif (ilkay==0):
      print("İlk 6 aylık geliriniz:", gelirKalemi)
      print("İlk 6 aylık gideriniz:", giderKalemi)
      print("Şirketiniz ilk 6 ay için başabaş noktasındadır.")
   else:
      print("İlk 6 aylık geliriniz:", gelirKalemi)
      print("İlk 6 aylık gideriniz:", giderKalemi)
      print("İlk 6 aylık zararınız:", ilkay)

def son6ay():
   global sonay
   yg=int(input("Yazılım gelirinizi giriniz:"))
   sg=int(input("Finansman gelirinizi giriniz:"))
   etg=int(input("E-ticaret gelirinizi giriniz:"))
   usg=int(input("Ürün satış gelirinizi giriniz:"))
   cm=int(input("Toplam çalışan maaşlarını giriniz:"))
   kg=int(input("Kira giderlerinizi giriniz:"))
   dm=int(input("Donanım maliyetlerinizi giriniz:"))
   sonay=(yg+sg+etg+usg)-(cm+kg+dm)
   gelirKalemi2=yg+sg+etg+usg
   giderKalemi2=cm+kg+dm
   if (sonay>0):
      print("Son 6 aylık geliriniz:", gelirKalemi2)
      print("Son 6 aylık gideriniz:", giderKalemi2)
      print("Son 6 aylık karınız:", sonay)
      ayKar()
   elif (sonay==0):
      print("Son 6 aylık geliriniz:", gelirKalemi2)
      print("Son 6 aylık gideriniz:", giderKalemi2)
      print("Şirketiniz başabaş noktasında karınız, giderinize eşit.")
      ayKar()
   else:
      print("Son 6 aylık geliriniz:", gelirKalemi2)
      print("Son 6 aylık gideriniz:", giderKalemi2)
      print("Son 6 aylık zararınız:", sonay)
      ayKar()

def ayKar():
   global karsilastir
   karsilastir=sonay-ilkay
   if (karsilastir>5000):
      print("İşletme çok karlıdır.")
   elif (1000<=karsilastir<=5000):
      print("İşletme karı normal.")
   else:
      print("İşletme yeterince karda değil.")

def dB():
   global dBstok
   global koltuk
   global yatak
   global dolap
   koltuk=50
   yatak=40
   dolap=20
   dBstok=koltuk+yatak+dolap
   print("Dönem başı stok toplamı:",dBstok, "Koltuk:",koltuk,"Yatak:",yatak, "Dolap:",dolap)

def dS():
   global dSstok
   ks=koltuk-25+10
   ys=yatak-20+15
   ds=dolap-10+5
   dSstok=ks+ys+ds
   print("Dönem sonu stok toplamı:", dSstok, "Koltuk:",ks,"Yatak:",ys, "Dolap:",ds,)
   a.buton("Ortalama Stok Değeriniz",dOrt)

def dOrt():
   os=(dBstok+dSstok)/2
   print("Dönem sonu stok miktarınız:", os)
   
   

label1.pack()
a.buton("Katma Değer Cirosu",katmaDC)
label2.pack()
a.buton("2016 Müşterilerle Çalışma Süresi",mcs2016)
a.buton("2017 Müşterilerle Çalışma Süresi",mcs2017)
a.buton("2017 ile 2016 Fark",mcsfark)
label3.pack()
a.buton("İlk 6 Aylık Durum",ilk6ay)
a.buton("Son 6 Aylık Durum",son6ay)
label4.pack()
a.buton("Dönem Başı Stok",dB)
a.buton("Dönem Sonu Stok",dS)
mainloop()
