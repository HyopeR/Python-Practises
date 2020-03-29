import practise4Functions
from practise4Functions import araclar
from practise4Functions import veri
from tkinter import *
import urllib.request
import base64

a=araclar()

resim1 = "https://img.webme.com/pic/c/creative-blog/Python-7.gif"
t1 = urllib.request.urlopen(resim1)
raw_input = t1.read()
t1.close()
c1 = base64.encodestring(raw_input)
image1 = PhotoImage(data=c1)
label1 = Label(image=image1)

resim2 = "https://img.webme.com/pic/c/creative-blog/Python-8.gif"
t2 = urllib.request.urlopen(resim2)
raw_input = t2.read()
t2.close()
c2 = base64.encodestring(raw_input)
image2 = PhotoImage(data=c2)
label2 = Label(image=image2)

resim3 = "https://img.webme.com/pic/c/creative-blog/Python-9.gif"
t3 = urllib.request.urlopen(resim3)
raw_input = t3.read()
t3.close()
c3 = base64.encodestring(raw_input)
image3 = PhotoImage(data=c3)
label3 = Label(image=image3)   

label1.pack()
a.buton("İşletme Karı",practise4Functions.iKar)
a.buton("Adam Başı Ciro",practise4Functions.aCiro)
label2.pack()
write=Label()
write.pack(expand=NO, fill=BOTH, pady=7)
write.config(text="Örnek 2 adımlarını sırasıyla hesaplatınız.", fg="red")
a.buton("Bilanço Aktif Bilgileri",practise4Functions.aktifHesap)
a.buton("Bilanço Pasif Bilgileri",practise4Functions.pasifHesap)
a.buton("Bilanço Hesap",practise4Functions.bilancoHesap)
label3.pack()
a.buton("Ybs 1",practise4Functions.ybs1)
a.buton("Ybs 2",practise4Functions.ybs2)
a.buton("Ybs 3",practise4Functions.ybs3)
mainloop()
