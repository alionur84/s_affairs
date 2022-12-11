from ders import Ders, Secmeli_Ders, Derslik, Ogrenci, Zorunlu_Ders


# Derslikleri deklare edelim --> Derslik(derslik adı, kapasite)
sinif1 = Derslik("D-101", 50)
sinif2 = Derslik("D-102", 15)
sinif3 = Derslik("D-103", 30)
sinif4 = Derslik("D-104", 10)
sinif5 = Derslik("D-105", 10)
sinif6 = Derslik("D-106", 15)

# Ogrencileri deklare edelim --> Ogrenci(öğrenci adı, soyadı, numarası)
# Default olarak max_secmeli_ders = 2 olarak geliyor. 
ogrenci1 = Ogrenci("Ali Onur", "Tepeciklioğlu", 123456)
ogrenci2 = Ogrenci("Ahmet", "Yılmaz", 654321)
ogrenci3 = Ogrenci("Ayşe", "Öztürk", 321654)
ogrenci4 = Ogrenci("Mehmet", "Demir", 111222)
ogrenci5 = Ogrenci("Fatma", "Çelik", 222111)
ogrenci6 = Ogrenci("Osman", "Tuğrul", 235647)
ogrenci7 = Ogrenci("Aylin", "Gül", 542183)
ogrenci8 = Ogrenci("Rıza", "Öz", 545874)
ogrenci9 = Ogrenci("Gürkan", "Dinç", 212121)
ogrenci10 = Ogrenci("Sezen", "Çolak", 635218)
ogrenci11 = Ogrenci("Aytaç Erim", "Yenilmez", 457126)
ogrenci12 = Ogrenci("Nurullah", "Durmaz", 258741)
ogrenci13 = Ogrenci("Güneş", "Korkmaz", 785412)
ogrenci14 = Ogrenci("Muhammet", "Kozan", 553399)
ogrenci15 = Ogrenci("Faik", "Aydemir", 247815)


# ogrencileri topluca kayıt etmek için listeler oluşturalım
ogrenci_listesi1 = [ogrenci1, ogrenci2, ogrenci3, ogrenci4, ogrenci5, ogrenci6, ogrenci7, ogrenci8, ogrenci9]
ogrenci_listesi2 = [ogrenci10, ogrenci11, ogrenci12, ogrenci13, ogrenci14, ogrenci15]
ogrenci_listesi3 = ogrenci_listesi1 + ogrenci_listesi2

# iki tane zorunlu ders deklare edelim. mat2'nin ön koşulu mat1'dir.

mat1 = Zorunlu_Ders("Matematik1")
mat2 = Zorunlu_Ders("Matematik2", mat1)

# iki sınıfa da derslik atayalım

mat1.derslik_ata(sinif1)
mat2.derslik_ata(sinif2)

# ogrenci_listesi1'deki ogrencileri mat1'e kaydedelim.
for i in ogrenci_listesi1:
	mat1.ogrenci_kaydet(i)

# mat1 için öğrenci listesini ekrana yazdıralım
print("mat1 öğrenci listesi:-->")
mat1.ogrenci_listesi_yazdir()

# mat1 için atanan dersliği yazdıralım
print("mat1 derslik:-->")
print(mat1.derslik)

# ogrenci_listesi1'deki ogrencileri mat2'ye kaydedelim

for i in ogrenci_listesi1:
	mat2.ogrenci_kaydet(i)

# mat2 için öğrenci listesini ekrana yazdıralım
print("mat2 öğrenci listesi-->")
mat2.ogrenci_listesi_yazdir()

# mat2 için atanan dersliği yazdıralım
print("mat2 derslik:-->")
print(mat2.derslik)

# ogrenci_listesi2'de bulunan 0'ıncı elemanı mat2'ye kaydetmeyi deneyelim.
print("ogrenci_listesi2'de bulunan 0'ıncı elemanı mat2'ye kaydetmeyi deneyelim-->")
mat2.ogrenci_kaydet(ogrenci_listesi2[0])

# üç adet seçmeli ders tanımlayalım --> Secmeli_Ders(ad, kontenjan)
muzik = Secmeli_Ders("Müzik", 10)
resim = Secmeli_Ders("Resim", 15)
beden_egitimi = Secmeli_Ders("Beden Eğitimi", 10)

# Seçmeli Derslere derslik atayalım
muzik.derslik_ata(sinif3)
# bu dersin kontenjanı 15 sınıf kapasitesi 10 olduğu için derslik atanmayacaktır.
print("resim dersinin kontenjanı 15 sınıf kapasitesi 10 olduğu için derslik atanmayacaktır. -->")
resim.derslik_ata(sinif4) 
beden_egitimi.derslik_ata(sinif5)

resim.derslik_ata(sinif6)

# ogrenci_listesi3'teki ögrencileri müzik dersine atayalım
# kontenjan olmadığından son 5 öğrenci derse kayıt edilemeyecektir
print("ogrenci_listesi3'teki ögrencileri müzik dersine atayalım \nkontenjan olmadığından son 5 öğrenci derse kayıt edilemeyecektir-->")
for i in ogrenci_listesi3:
	muzik.ogrenci_kaydet(i)

# muzik dersi ogrenci listesi	
print("muzik dersi ogrenci listesi-->")
muzik.ogrenci_listesi_yazdir()

# muzik dersinin kontenjanını 5 arttıralım
for i in range(5):
	muzik.kontenjan_arttir()

# kontenjan arttırdıktan sonra kalan ogrencileri derse ekleyelim.
for i in ogrenci_listesi3[10:]:
	muzik.ogrenci_kaydet(i)

print("kontenjan arttırıldıktan sonra muzik dersi ogrenci listesi-->")
muzik.ogrenci_listesi_yazdir()

# ogrenci 15'i resim ve beden eğitimi derslerine de kaydetmeyi deneyelim.
resim.ogrenci_kaydet(ogrenci15)
print("ogrenci 15'i resim ve beden eğitimi derslerine de kaydetmeyi deneyelim -->")
beden_egitimi.ogrenci_kaydet(ogrenci15)


# ogrenci15'i mat1 ve mat2 derslerine de kaydedelim.
mat1.ogrenci_kaydet(ogrenci15)
mat2.ogrenci_kaydet(ogrenci15)

# ogrenci 15'in ders listesini görüntüleyelim
print("ogrenci 15'in ders listesini görüntüleyelim-->")
ogrenci15.ogrenci_ders_listesi_yazdir()

# output:

'''

alionur@alihome:~/Dropbox/s_affairs$ python test1.py
mat1 öğrenci listesi:-->
[Ali Onur Tepeciklioğlu, Ahmet Yılmaz, Ayşe Öztürk, Mehmet Demir, Fatma Çelik, Osman Tuğrul, Aylin Gül, Rıza Öz, Gürkan Dinç]

mat1 derslik:-->
D-101

mat2 öğrenci listesi-->
[Ali Onur Tepeciklioğlu, Ahmet Yılmaz, Ayşe Öztürk, Mehmet Demir, Fatma Çelik, Osman Tuğrul, Aylin Gül, Rıza Öz, Gürkan Dinç]

mat2 derslik:-->
D-102

ogrenci_listesi2'de bulunan 0'ıncı elemanı mat2'ye kaydetmeyi deneyelim-->
Öğrenci Dersin Ön Koşulunu Sağlamıyor

resim dersinin kontenjanı 15 sınıf kapasitesi 10 olduğu için derslik atanmayacaktır. -->
Atanmaya Çalışılan Derslik Kapasitesi Kontenjandan Az Olamaz

ogrenci_listesi3'teki ögrencileri müzik dersine atayalım 
kontenjan olmadığından son 5 öğrenci derse kayıt edilemeyecektir-->
Kontenjan Dolu
Kontenjan Dolu
Kontenjan Dolu
Kontenjan Dolu
Kontenjan Dolu

muzik dersi ogrenci listesi-->
[Ali Onur Tepeciklioğlu, Ahmet Yılmaz, Ayşe Öztürk, Mehmet Demir, Fatma Çelik, Osman Tuğrul, Aylin Gül, Rıza Öz, Gürkan Dinç, Sezen Çolak]

kontenjan arttırıldıktan sonra muzik dersi ogrenci listesi-->
[Ali Onur Tepeciklioğlu, Ahmet Yılmaz, Ayşe Öztürk, Mehmet Demir, Fatma Çelik, Osman Tuğrul, Aylin Gül, Rıza Öz, Gürkan Dinç, Sezen Çolak, Aytaç Erim Yenilmez, Nurullah Durmaz, Güneş Korkmaz, Muhammet Kozan, Faik Aydemir]

ogrenci 15'i resim ve beden eğitimi derslerine de kaydetmeyi deneyelim -->
Öğrenci Alabileceği Maksimum Seçmeli Ders Sayısına Ulaşmış

ogrenci 15'in ders listesini görüntüleyelim-->
Faik Aydemir İsimli öğrencinin Kayıtlı Olduğu Dersler: 
[Müzik, Resim, Matematik1, Matematik2]

'''

