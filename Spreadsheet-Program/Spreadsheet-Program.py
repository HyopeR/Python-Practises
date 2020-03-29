from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
import urllib.request
import ctypes
myappid = 'Tablo Program'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class tabloEkle(QDialog):
    def __init__(self):
        super(tabloEkle,self).__init__()

        stylesheet = """
        QWidget#Form {background-image: url(tp-background.png);}
        QLabel#label {font:"Tahoma"; font-size:13pt; color:#000;}
        QLabel#kisiEkle {font:"Tahoma"; font-size:10pt; color:#000; }
        QLineEdit#lineEdit {height:30px; border: 5px solid #fff; border-radius:20px;}
        QTableWidget#tablo {border: 10px solid #fff; border-radius:20px; padding-left:0px; background-color:#fff;}
        QPushButton#charEkle {border: 2px solid #000; border-radius:10px; height:20px; font:"Tahoma"; font-size:10pt; margin-bottom:10px;}
        QPushButton#charEkle:hover {border: 3px solid #000; border-radius:10px; height:20px; font:"Tahoma"; font-size:10pt;}
        QPushButton#charEkle2 {border: 2px solid #000; border-radius:10px; height:20px; font:"Tahoma"; font-size:10pt;}
        QPushButton#charEkle2:hover {border: 3px solid #000; border-radius:10px; height:20px; font:"Tahoma"; font-size:10pt;}
        """
        QtGui.qApp.setStyleSheet(stylesheet)
                
        self.grid=QGridLayout()
        self.grid.setColumnMinimumWidth(1,350)
        self.grid.setAlignment(Qt.AlignTop)

        self.tabloBox = QVBoxLayout()
        self.tabloBox.setContentsMargins(0,0,0,0)
        self.grid.addLayout(self.tabloBox,0,0,1,0)

        #Tablo oluştu ve gride eklendi.
        self.startRow=0
        self.defaulRow=3
        self.tablo=QTableWidget()
        self.tablo.setObjectName('tablo')
        self.tablo.setFixedWidth(370)
        self.tablo.setFixedHeight(350)
        self.tablo.setRowCount(self.defaulRow+self.startRow)
        self.tablo.setColumnCount(3)
        self.tablo.setHorizontalHeaderLabels(['İsim', 'Soyisim', 'Bölüm'])
        self.tabloBox.addWidget(self.tablo)

        #Listeden veriler çekilerek tabloya aktarma.
        self.liste=[["Can", "Aydın", "YBS"], ["Semih","Yarar","YBS"],["Büşra","Demirgüreşçi","İktisat"]]
        self.tabloRow=0
        tabloColumn=0
        for step1 in self.liste:
            for step2 in step1:
                if self.tabloRow == 0:
                    self.tablo.setItem(self.tabloRow,tabloColumn, QTableWidgetItem(step2))
                    tabloColumn=tabloColumn+1
                    if tabloColumn == 3:
                        self.tabloRow=self.tabloRow+1
                        tabloColumn=0
                elif self.tabloRow == 1:
                    self.tablo.setItem(self.tabloRow,tabloColumn, QTableWidgetItem(step2))
                    tabloColumn=tabloColumn+1
                    if tabloColumn == 3:
                        self.tabloRow=self.tabloRow+1
                        tabloColumn=0
                elif self.tabloRow == 2:
                    self.tablo.setItem(self.tabloRow,tabloColumn, QTableWidgetItem(step2))
                    tabloColumn=tabloColumn+1
                    if tabloColumn == 3:
                        self.tabloRow=self.tabloRow+1
                        tabloColumn=0

        self.gridChar = QGridLayout()
        self.gridChar.setAlignment(Qt.AlignTop)
        self.gridChar.setContentsMargins(0,0,40,0)
        self.grid.addLayout(self.gridChar,0,2)
        
        self.addChar = QLabel('<center><font>Tabloya Yeni Kişi Ekle</font></center>')
        self.gridChar.addWidget(self.addChar,0,0)
        self.addChar.setObjectName('label')
        self.addChar.setFixedHeight(60)
        self.addChar.setFixedWidth(200)
        self.addChar.setContentsMargins(0,0,0,0)
        
        self.alan1 = QHBoxLayout()
        self.alan1.setContentsMargins(0,55,0,0)
        self.gridChar.addLayout(self.alan1,0,0,2,0)
        self.lab1 = QLabel('<center><font>İsim:</font></center>')
        self.lab1.setObjectName('kisiEkle')
        self.lab1.setFixedWidth(60)
        self.char1= QLineEdit()
        self.char1.setObjectName('lineEdit')
        self.char1.setFixedWidth(130)
        self.alan1.addWidget(self.lab1)
        self.alan1.addWidget(self.char1)

        self.alan2 = QHBoxLayout()
        self.alan2.setContentsMargins(0,105,0,00)
        self.gridChar.addLayout(self.alan2,0,0,3,0)
        self.lab2 = QLabel('<center><font>Soyisim:</font></center>')
        self.lab2.setObjectName('kisiEkle')
        self.lab2.setFixedWidth(60)
        self.char2= QLineEdit()
        self.char2.setObjectName('lineEdit')
        self.char2.setFixedWidth(130)
        self.alan2.addWidget(self.lab2)
        self.alan2.addWidget(self.char2)

        self.alan3 = QHBoxLayout()
        self.alan3.setContentsMargins(0,155,0,0)
        self.gridChar.addLayout(self.alan3,0,0,4,0)
        self.lab3 = QLabel('<center><font>Bölüm:</font></center>')
        self.lab3.setObjectName('kisiEkle')
        self.lab3.setFixedWidth(60)
        self.char3= QLineEdit()
        self.char3.setObjectName('lineEdit')
        self.char3.setFixedWidth(130)
        self.alan3.addWidget(self.lab3)
        self.alan3.addWidget(self.char3)

        self.buttonChar = QPushButton("Tabloya Ekle")
        self.buttonChar.setObjectName("charEkle2")
        self.buttonChar.setFixedWidth(200)
        self.gridChar.addWidget(self.buttonChar,4,0)
        self.connect(self.buttonChar,SIGNAL('clicked()'),self.kisiEkle)

        self.buttonChar2 = QPushButton("Satır Ekle")
        self.buttonChar2.setObjectName("charEkle2")
        self.buttonChar2.setFixedWidth(200)
        self.gridChar.addWidget(self.buttonChar2,5,0)
        self.connect(self.buttonChar2,SIGNAL('clicked()'),self.rowEkle)

        self.buttonChar3 = QPushButton("Satır Sil")
        self.buttonChar3.setObjectName("charEkle")
        self.buttonChar3.setFixedWidth(200)
        self.gridChar.addWidget(self.buttonChar3,6,0)
        self.connect(self.buttonChar3,SIGNAL('clicked()'),self.rowSil)
        
        self.setLayout(self.grid)
        self.tablo.show()
        self.setWindowTitle("Tablo Program")

    def kisiEkle(self):
        self.c1=self.char1.text()
        self.c2=self.char2.text()
        self.c3=self.char3.text()
        if self.char1.text() != '' and self.char2.text() != '' and self.char3.text() != '':
            self.startRow=self.startRow+1
            self.numberRow=self.defaulRow+self.startRow
            self.tablo.setRowCount(self.defaulRow+self.startRow)
            self.tablo.setItem(self.defaulRow+self.startRow-1,0, QTableWidgetItem(self.c1))
            self.tablo.setItem(self.defaulRow+self.startRow-1,1, QTableWidgetItem(self.c2))
            self.tablo.setItem(self.defaulRow+self.startRow-1,2, QTableWidgetItem(self.c3))
            self.char1.clear()
            self.char2.clear()
            self.char3.clear()

    def rowEkle(self):
        self.startRow=self.startRow+1
        self.tablo.setRowCount(self.defaulRow+self.startRow)
    def rowSil(self):
        if self.defaulRow+self.startRow >= 1:
            self.startRow=self.startRow-1
            self.tablo.setRowCount(self.defaulRow+self.startRow)
        elif self.defaulRow+self.startRow <= 0:
            print("Silinecek satır kalmadı")
            
        
uyg=QApplication([])
pencere=tabloEkle()
pencere.setFixedWidth(700)
pencere.setFixedHeight(380)
url = 'https://img.webme.com/pic/c/creative-blog/python-13.png'
data = urllib.request.urlopen(url).read()
image = QtGui.QImage()
image.loadFromData(data)
pencere.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(image)))
pencere.setObjectName('Form')
pencere.show()
uyg.exec_
