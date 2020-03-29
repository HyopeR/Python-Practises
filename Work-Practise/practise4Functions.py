from tkinter import *
      
class araclar(object):
   def __init__(self):
      arac = Tk()
      arac.title("Simple Prog")
   def buton(self, isim, olay):
      Btn = Button(text=isim, command=olay)
      Btn.pack(side="top",pady=3)
      Btn.config(width=26,height=1)

#Örnek 1'de kullanılan fonksiyonlar;
def iKar():
    gelir=int(input("İşletme gelirlerini giriniz:"))
    gider=int(input("İşletme giderlerini giriniz:"))
    kar=gelir-gider
    if (kar>0):
        print("İşletme karınız:",kar)
    elif (kar<0):
        print("İşletmeniz zarardadır:",kar)
    else:
        print("İşletmeniz başabaş noktasındadır.")

def aCiro():
    topCiro=int(input("Toplam cironuzu giriniz:"))
    topCs=int(input("Toplam çalışan sayınızı giriniz:"))
    adamCiro=topCiro/topCs
    print("Adam başı cironuz:",adamCiro)

#Örnek 2'de kullanılan fonksiyonlar;
aktifSay=0
pasifSay=0

def doVarlik():
    global donenVarlik
    kasaHesap=20000
    alCekler=10000
    bankHesap=5000
    alSenetHesap=28000
    ticMalHesap=65000
    donenVarlik=kasaHesap+alCekler+bankHesap+alSenetHesap+ticMalHesap

def duVarlik():
    global duranVarlik
    binaHesap=150000
    tasitHesap=25000
    demirbas=8000
    duranVarlik=binaHesap+tasitHesap+demirbas

def aktifHesap():
    global aktifSay
    global aktifToplam
    doVarlik()
    duVarlik()
    aktifToplam=donenVarlik+duranVarlik
    aktifSay=aktifSay+1
    print("Dönen varlıklarınızın toplamı:",donenVarlik)
    print("Duran varlıklarınızın toplamı:",duranVarlik)
    print("Bilançonun aktiflerinin toplamı:",aktifToplam)
   
def kisaVade():
    global kvyk
    bKredi=42000
    satHesap=60000
    kvyk=bKredi+satHesap

def uzunVade():
    global uvyk
    bKredi=35000
    borcSenet=115000
    uvyk=bKredi+borcSenet

def ozKaynak():
    global sermaye
    sermaye=59000
    
def pasifHesap():
    global pasifSay
    global pasifToplam
    kisaVade()
    uzunVade()
    ozKaynak()
    pasifToplam=kvyk+uvyk+sermaye
    pasifSay=pasifSay+1
    print("Kısa vadeli yabancı kaynak toplamı:",kvyk)
    print("Uzun vadeli yabancı kaynak toplamı:",uvyk)
    print("Özkaynak toplamınız:",sermaye)
    print("Bilançonun pasiflerinin toplamı:",pasifToplam)

def bilancoHesap():
    while True:
        if (aktifSay>=1) and (pasifSay>=1):
            if(aktifToplam==pasifToplam):
                print(aktifToplam,"=",pasifToplam,"Bilanço doğru hesaplanmıştır.")
                break
            else:
                print("Bilanço yanlış hesaplanmıştır.")
                break
        elif (aktifSay>=1) and (pasifSay<1):
            print("Lütfen 'Bilanço Pasif Bilgilerini' hesaplattıktan sonra deneyiniz.")
            break
        elif (aktifSay<1) and (pasifSay>=1):
            print("Lütfen 'Bilanço Aktif Bilgilerini' hesaplattıktan sonra deneyiniz.")
            break
        else:
            print("Diğer adımları yapmadan bu adım görüntülenemez.")
            break
            
#Örnek 3'de kullanılan fonksiyonlar;
class veri():   
    def __init__(self, begenSay, yorumSay, paySay, icerikSay, takipSay):
        self.begenSay=begenSay
        self.yorumSay=yorumSay
        self.paySay=paySay
        self.icerikSay=icerikSay
        self.takipSay=takipSay
        self.eoHesapla()
    def eoHesapla(self):
        etkiOran=(((self.begenSay+self.yorumSay+self.paySay)/self.icerikSay)/self.takipSay)*100
        if (etkiOran>20/100):
           print("Etkileşim oranı:",format(etkiOran, ".3f"),"Başarılıdır.")
        else:
           print("Etkileşim oranı:",format(etkiOran, ".3f"),"Başarısız.")
           print("Not: Etkileşim oranınızın başarılı duruma gelmesi için %20'nin üstünde olmalıdır.")

#Üst alandaki ana sınıfı oluşturulduktan sonra butonlara atanacak olan fonksiyonları oluşturuyoruz.            
def ybs1():
   print("Ybs 1 grubu için:")
   ybs1=veri(365000, 65000, 870, 500, 1125000)
def ybs2():
   print("Ybs 2 grubu için:")
   ybs2=veri(450000, 25000, 380, 100, 1450000)
def ybs3():
   print("Ybs 3 grubu için:")
   ybs3=veri(582000, 52000, 1200, 650, 2000000)
