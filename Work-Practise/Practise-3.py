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
URL = "https://img.webme.com/pic/c/creative-blog/Python-6.gif"
t = urllib.request.urlopen(URL)
raw_input = t.read()
t.close()
c = base64.encodestring(raw_input)
image = PhotoImage(data=c)
label = Label(image=image)

def ornek1():
    sm=500
    bsf=20
    ciro=5000
    ay=0
    while True:
        sm=sm+200
        bsf=bsf+10
        ciro=ciro+sm*bsf
        ay=ay+1
        print(ay,". aydaki cironuz:", ciro)
        if(ciro>500000):
            print("Cironuz", ay, "ay sonunda 500.000 TL'yi geçiçektir.")
            break

def ornek2():
    stok=10000
    sat=500
    al=100
    ay=0
    while True:
        stok=stok-sat+al
        ay=ay+1
        print(ay,". ay stok miktarınız:", stok)
        if (stok<=0):
            print(ay,". ayda işletmenin stok miktarı sıfırlanacaktır.")
            break

def ornek3():
    giris=""
    islem=0
    global toplam
    toplam=0
    while(giris!=0):
        giris=int(input("3'e bölmek istediğiniz sayıyı girin. Programı sonlandırmak için [0]:"))
        islem=islem+1
        if (giris==0):
            print("Program sizin tarafınızdan sonlandırıldı.")
        else:
           kalan=giris%3
           print(islem, ". Girdiğiniz sayının 3'e bölümünden kalan:", kalan)
           toplam=toplam+kalan
           print("Girdiğiniz sayıların 3'e bölümünden kalanların toplamı:", toplam)

def ornek4():
    maas=90
    giris=""
    hafta=0
    ay=0
    mesai=0
    day=0
    while True:
        hafta=hafta+1
        day=day+7
        print(hafta, ". haftada ki;")
        giris=int(input("Mesai saatinizi giriniz:"))
        mesai=mesai+giris
        if(hafta==4 and mesai<=22):
            ay=ay+1
            toplamaas=(maas*day)+(mesai*(maas*10/100))
            print(ay, ". ay maaşınız:", toplamaas)
            print(ay, ". ay toplam mesai saatiniz:" ,mesai)
            mesai=0
            hafta=0
            day=0
        elif(mesai>22):
            print("Mesai saatiniz belirlenen prosedürün üstündedir. Lütfen bilgileri düzgün giriniz.")
            start=input("Programı yeniden başlatmak için [start]:")
            if (start=="start" or start=="START" or start=="Start"):
                print("Programı yeniden başlattınız...")
                ornek4()
            else:
                print("Program sonlandırıldı.")
                break


def ornek5():
    output=200
    day=0
    user=""
    global toplamuser     #Global olan veriler alttaki fonksiyonda kullanılmamıştır.
    toplamuser=0           #Eklenme amaçları işletme için gelecek dönemlerde;
    global toplamdone    #Toplamsağlam ürün sayısı ve toplam defolu ürün sayılarını,
    toplamdone=0          #Erişilebilir kılmak için yapılmıştır.
    while True:
        day=day+1
        print(day, ". gün için;")
        user=int(input("Günlük defolu ürün sayısını giriniz:"))
        defo=output*20/100
        toplamuser=toplamuser+user
        toplamdone=toplamdone+output-user
        if (200>user>40):
            print(day, ". günde ki defolu ürün sayınız üretiminizin %20'sinden fazladır!")
            print(day, ". günde ki defolu ürün oranınız:", user/output)
        elif (user<=40):
            print(day, ". günde ki defolu ürün sayınız:", user)
            print(day, ". günde ki defolu ürün oranınız:", user/output)
        else:
            print("200'den büyük bir değer girişi yaptınız lütfen bilgileri kontrol edin.")
            start=input("Programı yeniden başlatmak için [start]:")
            if (start=="start" or start=="START" or start=="Start"):
                ornek5()
            else:
                print("Program sonlandırıldı.")
                break
            
label.pack()
a.buton("Örnek 1",ornek1)
a.buton("Örnek 2",ornek2)
a.buton("Örnek 3",ornek3)
a.buton("Örnek 4",ornek4)
a.buton("Örnek 5",ornek5)

mainloop()
