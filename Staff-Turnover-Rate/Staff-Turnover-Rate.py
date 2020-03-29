from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
import urllib.request
import ctypes
myappid = 'PerDev Uygulaması'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class perDevir(QDialog):
    def __init__(self,ebeveyn=None):
        super(perDevir,self).__init__(ebeveyn)

        stylesheet = """
        QWidget#Form {background-image: url(perDev-back.png);}
        QLabel#labDuzen{font:10pt; font-family:verdana; color:#000; }
        QLabel#labDuzen2{font:9pt; font-family:verdana; color:#000; }
        QLabel#labDuzen3{font:9pt; font-family:verdana; color:#000; }
        QPushButton#ustButon{font:9pt; font-family:verdana; background-color: #79b9e2; border: 2px solid #79b9e2; border-top-right-radius: 10px;border-top-left-radius: 10px; height:25px; margin-left:90px; margin-top:25px;}
        QPushButton#ustButon:hover{ font:9pt; font-family:verdana; background-color: #79b9e2; border: 2px solid #79b9e2; margin-top:18}
        QPushButton#altButon{font:9pt; font-family:verdana; background-color: #79b9e2; border: 2px solid #34617e; height:15px; margin-left:90px;}
        """
        QtGui.qApp.setStyleSheet(stylesheet) 

        self.anaGrid = QGridLayout()
        self.anaGrid.setContentsMargins(10,110,10,10)
        self.anaGrid.setAlignment(Qt.AlignTop)
        self.islemSay=0
        self.islemSay2=0
        self.listeStrBoom=["","q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s","d","f","g","h","j","k","l","ş","i","z","x","c","v","b","n","m","ö","ç","/","*","-","+","<",">","|",",","'",'"',"{","[","]","}","=","(",")","?","\",","$","#","£","½","%","&","!","^","~","`",":",";","é","@","ß","æ","€",".",'_']
        self.listeStr=["1","2","3","4","5","6","7","8","9","10","11","12"]
        self.aylar=["1.  AY:","2.  AY:","3.  AY:","4.  AY:","5.  AY:","6.  AY:","7.  AY:","8.  AY:","9.  AY:","10. AY:","11. AY:","12. AY:"]
        self.listeDeep = ["self.creLine1", "self.creLine2", "self.creLine3", "self.creLine4", "self.creLine5", "self.creLine6", "self.creLine7", "self.creLine8", "self.creLine9" ,"self.creLine10", "self.creLine11", "self.creLine12"]
        ##
        self.soruBox = QHBoxLayout()
        self.anaGrid.addLayout(self.soruBox,1,0,1,1)

        self.ayLab = QLabel("Hesaplanacak olan ay sayısı (Max12):")
        self.ayLab.setObjectName('labDuzen')
        self.ayBelirle = QLineEdit("12")

        self.soruBox.addWidget(self.ayLab)
        self.soruBox.addWidget(self.ayBelirle)

        self.oneButton = QPushButton("AY SAYISINI UYGULA", default=False, autoDefault=False)
        self.oneButton.setFixedWidth(350)
        self.oneButton.setObjectName('ustButon')
        self.anaGrid.addWidget(self.oneButton,2,0)
        self.connect(self.oneButton,SIGNAL("clicked()"),self.alanOlustur)
        ##

        self.altContent = QLabel('<center><font></font></center>')
        self.altContent.setObjectName('labDuzen3')
        self.altContent.setContentsMargins(0,20,0,10)
        self.anaGrid.addWidget(self.altContent,3,0)
        self.altButon = QPushButton("HESAPLA", default=False, autoDefault=True)
        self.altButon.setFixedWidth(350)
        self.altButon.setObjectName('altButon')
        self.clearButon = QPushButton("SIFIRLA", default=False, autoDefault=True)
        self.clearButon.setFixedWidth(350)
        self.clearButon.setObjectName('altButon')
        self.sonDuzen = QLabel("Personel Devir Hızınız:")
        self.sonDuzen.setFixedWidth(160)
        self.sonDuzen.setObjectName('labDuzen2')
        self.sonDuzenSag = QLabel("")

        self.setWindowTitle("PerDev Programı")
        self.setLayout(self.anaGrid)

    def alanOlustur(self):
        if (self.listeStr.count(self.ayBelirle.text()) < 1 ):
            if self.islemSay == 0:
                self.altContent.setText('<center><font color="red"><b>1 ile 12 arasında bir sayı giriniz.</b></font></center>')
            elif self.islemSay >= 1:
                self.altContent.setText('<center><font color="red"><b>1 ile 12 arasında bir sayı giriniz.</b></font></center>')
                self.deleteLayout()
                self.altButon.setParent(None)
                self.clearButon.setParent(None)
        elif 1 <= int(self.ayBelirle.text()) <= 12:
            self.altContent.setText('<center><font color="red"> Aşağıdaki alanlara aylık olarak <b>çalışan sayınızı</b> girmelisiniz.</font></center>')
            self.aktar=0
            if self.islemSay == 0:
                self.islemSay=self.islemSay+1
                self.altGrid = QGridLayout()
                self.altGrid.setContentsMargins(10,0,0,0)
                self.anaGrid.addLayout(self.altGrid,4,0)
                while True:
                    if self.aktar < int(self.ayBelirle.text()) and int(self.ayBelirle.text()) <= 12:
                        self.creLab = QLabel(self.aylar[self.aktar])
                        self.creLab.setFixedWidth(160)
                        self.creLab.setObjectName('labDuzen2')
                        self.aktar=self.aktar + 1
                        self.listeDeep[self.aktar-1] = QLineEdit()
                        self.listeDeep[self.aktar-1].setFixedWidth(150)
                        self.altGrid.addWidget(self.listeDeep[self.aktar-1],self.aktar-1,1)
                        self.altGrid.addWidget(self.creLab,self.aktar-1,0)
                    else:
                        self.closeLab = QLabel("İşten Çıkan Sayısı:")
                        self.closeLab.setObjectName('labDuzen2')
                        self.closeLab.setFixedWidth(160)
                        self.perClose = QSpinBox()
                        self.perClose.setFixedWidth(150)
                        self.altGrid.addWidget(self.closeLab,self.aktar,0)
                        self.perClose.setRange(0,5000)
                        self.altGrid.addWidget(self.perClose,self.aktar,1)
                        self.anaGrid.addWidget(self.altButon,5,0)
                        self.connect(self.altButon,SIGNAL("clicked()"),self.devirHesap)
                        self.anaGrid.addWidget(self.clearButon,6,0)
                        self.connect(self.clearButon,SIGNAL("clicked()"),self.alanOlustur)
                        break
                
            elif self.islemSay > 0:
                self.deleteLayout()
                self.altGrid = QGridLayout()
                self.altGrid.setContentsMargins(10,0,0,0)
                self.anaGrid.addLayout(self.altGrid,4,0)
                while True:
                    if self.aktar < int(self.ayBelirle.text()) and int(self.ayBelirle.text()) <= 12:
                        self.creLab = QLabel(self.aylar[self.aktar])
                        self.creLab.setFixedWidth(160)
                        self.creLab.setObjectName('labDuzen2')
                        self.aktar=self.aktar + 1
                        self.listeDeep[self.aktar-1] = QLineEdit()
                        self.listeDeep[self.aktar-1].setFixedWidth(150)
                        self.altGrid.addWidget(self.listeDeep[self.aktar-1],self.aktar-1,1)
                        self.altGrid.addWidget(self.creLab,self.aktar-1,0)
                    else:
                        self.closeLab = QLabel("İşten Çıkan Sayısı:")
                        self.closeLab.setObjectName('labDuzen2')
                        self.closeLab.setFixedWidth(160)
                        self.perClose = QSpinBox()
                        self.perClose.setFixedWidth(150)
                        self.altGrid.addWidget(self.closeLab,self.aktar,0)
                        self.perClose.setRange(0,5000)
                        self.altGrid.addWidget(self.perClose,self.aktar,1)
                        self.anaGrid.addWidget(self.altButon,5,0)
                        self.connect(self.altButon,SIGNAL("clicked()"),self.devirHesap)
                        self.anaGrid.addWidget(self.clearButon,6,0)
                        self.connect(self.clearButon,SIGNAL("clicked()"),self.alanOlustur)
                        self.sonDuzen = QLabel("Personel Devir Hızınız:")
                        self.sonDuzen.setFixedWidth(160)
                        self.sonDuzen.setObjectName('labDuzen2')
                        self.sonDuzenSag = QLabel("")
                        break
            
    def devirHesap(self):
        self.islemSay2=0
        self.premium=self.aktar
        while self.islemSay2 < self.premium:
            if self.listeStrBoom.count(self.listeDeep[self.islemSay2].text().lower()) <= 0:
                self.islemSay2=self.islemSay2+1
                if self.islemSay2 == self.premium:
                    self.sonDuzen.setText("Personel Devir Hızınız:")
                    self.sonDuzenSag.clear()
                    self.perToplam=0
                    self.ayToplam=self.aktar
                    self.childAktar=self.aktar
                    while True:
                        if self.childAktar > 0:
                            self.perToplam = self.perToplam + int(self.listeDeep[self.childAktar-1].text())
                            self.childAktar=self.childAktar-1
                        elif self.childAktar == 0:
                            self.sonuc = self.perToplam / self.ayToplam
                            self.sonuc2 = (int(self.perClose.text()) / self.sonuc)*100
                            self.sonuc=format(self.sonuc2, ".2f")
                            self.sonDuzenSag.setText(str(self.sonuc))
                            self.altGrid.addWidget(self.sonDuzen,self.aktar+1,0)
                            self.altGrid.addWidget(self.sonDuzenSag,self.aktar+1,1)
                            self.altContent.setText('<center><font color="red"><b></b></font></center>')
                            break
            else:
                self.altContent.setText('<center><font color="red"><b>Lütfen verilerinizi kontrol ediniz!</b></font></center>')
                break

    def deleteLayout(self):
        if self.altGrid is not None:
            while self.altGrid.count():
                item = self.altGrid.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    deleteLayout(item.layout())

perUyg=QApplication([])
perDev = perDevir()
perDev.setObjectName('Form')
perDev.setFixedWidth(460)
perDev.setFixedHeight(710)
url = 'https://img.webme.com/pic/c/creative-blog/python-15.png'
data = urllib.request.urlopen(url).read()
image = QtGui.QImage()
image.loadFromData(data)
perDev.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(image)))
perDev.show()
perUyg.exec_
