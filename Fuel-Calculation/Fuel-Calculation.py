import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
import urllib.request
import ctypes
import time
myappid = 'Yakıt Hesaplayıcısı'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

global num1
global num2
global num3

liste1=[]
liste2=[]
liste3=[]
listeStr=["1","2","3","4","5","6","7","8","9","0","."]
listeStrBoom=["q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s","d","f","g","h","j","k","l","ş","i","z","x","c","v","b","n","m","ö","ç","/","*","-","+","<",">","|",",","'",'"',"{","[","]","}","=","(",")","?","\",","$","#","£","½","%","&","!","^","~","`",":",";","é","@","ß","æ","€",".",'_']
listeTop=[]

def fonk1():
   if len(liste1) and len(liste2) and len(liste3) != 0:
      listeTop.append(liste1[len(liste1)-1])
      listeTop.append(liste2[len(liste2)-1])
      listeTop.append(liste3[len(liste3)-1])
      sonuc= (listeTop[(len(listeTop)-3)] / 100) * listeTop[(len(listeTop)-1)] * listeTop[(len(listeTop)-2)]
      sonuc=format(sonuc, ".2f")
      toplamtutar.setText(str(sonuc) + " TL")
      progNot.clear()
   else:
      progNot.setText('<center><font color="red">Lütfen gerekli verileri giriniz!</font><center>')

def temizle():
   if len(listeTop)>=3:
      listeTop.clear()
      liste1.clear()
      liste2.clear()
      liste3.clear()
      yol.clear( )
      yakitfiyat.clear( )
      tuketilenyakit.clear( )
      toplamtutar.clear( )
      progNot.setText('<center><font color="red">İşlemler sıfırlandı! Yeni verilerini girebilirsiniz.</font><center>')
   else:
      progNot.setText('<center><font color="red">Verileri tamamen girip işlem yaptırdıktan sonra sıfırlayabilirsiniz!</font><center>')
    
def number1(num1):
   for secure1 in num1:
      time.sleep(0)
   if num1=="":
      num1=0
   elif listeStrBoom.count(num1) == 1:
      progNot.setText('<center><font color="red">Verilen alanlara sayı veya rakam girilmelidir!</font><center>')
      yol.clear()
   elif listeStr.count(secure1) != 1:
      progNot.setText('<center><font color="red">Verilen alanlara sayı veya rakam girilmelidir!</font><center>')
      yol.clear()
      liste1.clear()
   elif num1.count(".") > 1:
      progNot.setText('<center><font color="red">Fazladan işaret kullandınız!</font><center>')
      yol.clear()
      liste1.clear()
   elif float(num1)>0:
      liste1.append(float(num1))

def number2(num2):
   for secure2 in num2:
      time.sleep(0)
   if num2=="":
      num2=0
   elif listeStrBoom.count(num2) == 1:
      progNot.setText('<center><font color="red">Verilen alanlara sayı veya rakam girilmelidir!</font><center>')
      yakitfiyat.clear()
   elif listeStr.count(secure2) != 1:
      progNot.setText('<center><font color="red">Verilen alanlara sayı veya rakam girilmelidir!</font><center>')
      yakitfiyat.clear()
      liste2.clear()
   elif num2.count(".") > 1:
      progNot.setText('<center><font color="red">Fazladan işaret kullandınız!</font><center>')
      yakitfiyat.clear()
      liste2.clear()
   elif float(num2)>0:
      liste2.append(float(num2))

def number3(num3):
   for secure3 in num3:
      time.sleep(0)
   if num3=="":
      num3=0
   elif listeStrBoom.count(num3) == 1:
      progNot.setText('<center><font color="red">Verilen alanlara sayı veya rakam girilmelidir!</font><center>')
      tuketilenyakit.clear()
   elif listeStr.count(secure3) != 1:
      progNot.setText('<center><font color="red">Verilen alanlara sayı veya rakam girilmelidir!</font><center>')
      tuketilenyakit.clear()
      liste3.clear()
   elif num3.count(".") > 1:
      progNot.setText('<center><font color="red">Fazladan işaret kullandınız!</font><center>')
      tuketilenyakit.clear()
      liste3.clear()
   elif float(num3)>0:
      liste3.append(float(num3))
    
uygulama=QApplication([])
pencere=QWidget()

hbox = QtGui.QHBoxLayout()
url = 'https://img.webme.com/pic/c/creative-blog/Python-11.png'
data = urllib.request.urlopen(url).read()
image = QtGui.QImage()
image.loadFromData(data)
led = QtGui.QLabel()
led.setPixmap(QtGui.QPixmap(image))
led.setFixedWidth(420)
led.setFixedHeight(65)

gidilecek=QLabel("Gideceğiniz Yol [KM]:")
gidilecek.setStyleSheet("font: 8.5pt; font-family:Tahoma; margin-top:2; font-weight:normal; color:#000;")
gidilecek.setFixedWidth(220)
gidilecek.setContentsMargins(5,0,0,0)

yakit=QLabel("Yakıtın Litre Fiyatı [TL]:")
yakit.setStyleSheet("font: 8.5pt; font-family:Tahoma; margin-top:2; font-weight:normal; color:#000;")
yakit.setFixedWidth(220)
yakit.setContentsMargins(5,0,0,0)

tuketilen=QLabel("100KM'de tüketilen yakıt [L]:")
tuketilen.setStyleSheet("font: 8.5pt; font-family:Tahoma; margin-top:2; font-weight:normal; color:#000;")
tuketilen.setFixedWidth(220)
tuketilen.setContentsMargins(5,0,0,0)

tutar=QLabel("Toplam Tutar [TL]:")
tutar.setStyleSheet("font: 8.5pt; font-family:Tahoma; margin-top:2; font-weight:normal; color:#000;")
tutar.setFixedWidth(220)
tutar.setContentsMargins(5,0,0,0)

########

global yol
yol=QLineEdit()
yol.textChanged.connect(number1)
yol.setFixedWidth(200)
yol.setFixedHeight(30)

global yakitfiyat
yakitfiyat=QLineEdit()
yakitfiyat.textChanged.connect(number2)
yakitfiyat.setFixedWidth(200)
yakitfiyat.setFixedHeight(30)

global tuketilenyakit
tuketilenyakit=QLineEdit()
tuketilenyakit.textChanged.connect(number3)
tuketilenyakit.setFixedWidth(200)
tuketilenyakit.setFixedHeight(30)

toplamtutar=QLabel()
toplamtutar.setStyleSheet("font: 9pt; font-family:Tahoma; font-weight:normal; color:#000;")
toplamtutar.setFixedWidth(200)
toplamtutar.setFixedHeight(30)

hesapla=QPushButton("HESAPLA", default=False, autoDefault=True)
pencere.connect(hesapla,SIGNAL("clicked()"),fonk1)
hesapla.setStyleSheet("font: 10pt; font-family:Tahoma; color:#000; font-weight:normal;")
hesapla.setFixedWidth(420)
hesapla.setFixedHeight(30)

clear=QPushButton("TABLOYU SIFIRLA", default=False, autoDefault=True)
pencere.connect(clear,SIGNAL("clicked()"),temizle)
clear.setStyleSheet("font: 10pt; font-family:Tahoma; color:#000; font-weight:normal;")
clear.setFixedWidth(420)
clear.setFixedHeight(30)

progNot=QLabel("")
progNot.setStyleSheet("font: 8.5pt; font-family:Tahoma; margin-top:8; font-weight:normal; color:#000;")
progNot.setFixedWidth(420)
progNot.setFixedHeight(25)

########

kutuResim=QHBoxLayout()
kutuResim.setContentsMargins(5,10,5,10)
kutuResim.setSpacing(0)
kutuResim.setAlignment(Qt.AlignTop)
kutu1=QHBoxLayout()
kutu1.setContentsMargins(0,10,0,10)
kutu1.setSpacing(0)
kutu1.setAlignment(Qt.AlignTop)
kutu2=QHBoxLayout()
kutu2.setContentsMargins(0,10,0,10)
kutu2.setSpacing(0)
kutu2.setAlignment(Qt.AlignTop)
kutu3=QHBoxLayout()
kutu3.setContentsMargins(0,10,0,10)
kutu3.setSpacing(0)
kutu3.setAlignment(Qt.AlignTop)
kutu4=QHBoxLayout()
kutu4.setContentsMargins(0,10,0,10)
kutu4.setSpacing(0)
kutu4.setAlignment(Qt.AlignTop)
kutu5=QHBoxLayout()
kutu5.setContentsMargins(5,2,5,2)
kutu5.setSpacing(0)
kutu5.setAlignment(Qt.AlignTop)
kutu6=QHBoxLayout()
kutu6.setContentsMargins(5,2,5,2)
kutu6.setSpacing(0)
kutu6.setAlignment(Qt.AlignTop)
kutu7=QHBoxLayout()
kutu7.setContentsMargins(0,0,0,0)
kutu7.setSpacing(0)
kutu7.setAlignment(Qt.AlignTop)
allbox=QVBoxLayout()
allbox.setAlignment(Qt.AlignTop)

kutuResim.addWidget(led)
kutu1.addWidget(gidilecek)
kutu1.addWidget(yol)
kutu2.addWidget(yakit)
kutu2.addWidget(yakitfiyat)
kutu3.addWidget(tuketilen)
kutu3.addWidget(tuketilenyakit)
kutu4.addWidget(tutar)
kutu4.addWidget(toplamtutar)
kutu5.addWidget(hesapla)
kutu6.addWidget(clear)
kutu7.addWidget(progNot)

allbox.addLayout(kutuResim)
allbox.addLayout(kutu1)
allbox.addLayout(kutu2)
allbox.addLayout(kutu3)
allbox.addLayout(kutu4)
allbox.addLayout(kutu5)
allbox.addLayout(kutu6)
allbox.addLayout(kutu7)
pencere.setLayout(allbox)

pencere.setWindowTitle("Yakıt Hesaplayıcısı")
url2 = 'https://img.webme.com/pic/c/creative-blog/pyicon_64x64.png'
data2 = urllib.request.urlopen(url2).read()
image2 = QtGui.QImage()
image2.loadFromData(data2)
uygulama.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(image2)))
pencere.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(image2)))
pencere.setFixedWidth(460)
pencere.setFixedHeight(440)
pencere.show()
uygulama.exec_
