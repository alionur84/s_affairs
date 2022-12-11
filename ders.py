
	# Ders class. Ders sadece ad vererek initiate edilebilir. 
class Ders:
	# Ders class'ın init methodu. 
	def __init__(self, ad, derslik=None, ogrenci_listesi=None):
		self.ad = ad
		self.derslik = derslik
		if ogrenci_listesi is None:
			self.ogrenci_listesi = []
		else:
			self.ogrenci_listesi = ogrenci_listesi
	'''
	Bir ogrencinin derse kayitli olup olmadığını kontrol eden fonk
	Eğer kayıtlıysa true, değilse false döndürür
	'''
	def ogrenci_kayitli_mi(self, ogrenci):
		if ogrenci in self.ogrenci_listesi:
			return True
		else:
			return False
	'''
	derslik kapasitesini öğrenci listesinin uzunluğu ile karşılaştıran fonk.
	Kapasite yeterli ise True değil ise False Döndürür
	'''
	def kapasite_yeterli_mi(self):
		if self.derslik.kapasite > len(self.ogrenci_listesi):
			return True
		else:
			return False

	'''
	Öğrenciyi derse kaydetmek için kullanılan fonk.
	Önce derslik atanmış mı kontrol eder.
	Atanmış ise kapasitenin yeterli olup olmadığını ve öğrencinin derse zaten
	kayıtlı olup olmadığını kontrol eder. 
	Derslik var ise ve öğrenci derse kayıtlı değil ise öğrenciyi derse kaydeder.
	Yöntem aynı zamanda ogrenci objectinin ders_listesi attribute'una eklenen
	Ders object i kaydeder. 
	'''
	def ogrenci_kaydet(self, ogrenci):
		if self.derslik is None:
			print("Öğrenci Kaydetmek İçin Önce Derslik Atayınız")
		else:
			if self.kapasite_yeterli_mi() and not self.ogrenci_kayitli_mi(ogrenci):
				self.ogrenci_listesi.append(ogrenci)
				ogrenci.ders_listesi.append(self)
			elif not self.kapasite_yeterli_mi() and not self.ogrenci_kayitli_mi(ogrenci):
				print("Derslik Kapasitesi Dolu")
			elif self.kapasite_yeterli_mi() and self.ogrenci_kayitli_mi(ogrenci):
				print("Ogrenci Zaten Derse Kayıtlı")
			else:
				print("Öğrenci Zaten Derse Kayıtlı ve Derslik Kapasitesi Dolu")

	'''
	Öğrenci kaydını dersten silen fonk.
	Eğer öğrenci derse kayıtlı ise çağırıldığında öğrencinin kaydını siler.
	'''	
	def ogrenci_kayit_sil(self, ogrenci):
		if self.ogrenci_kayitli_mi(ogrenci):
			print(f"{self.ogrenci_listesi.pop(self.ogrenci_listesi.index(ogrenci))} İsimli Öğrencinin Dersten Kaydı Silinmiştir")
		else:
			print(f"{ogrenci} Bu Derse Kayıtlı Değil")

	'''
	Derse kayıtlı öğrenci listesini yazdırmak için kullanılan fonk.
	'''
	def ogrenci_listesi_yazdir(self):
		print(self.ogrenci_listesi)

	'''
	Derse kayıtlı öğrenci sayısını yazdırmak için kullanılan fonk. 
	'''
	def kayitli_ogrenci_sayisi(self):
		print(len(self.ogrenci_listesi))

	'''
	Derse derslik atamak için kullanılan fonk. 
	Eğer derslik atanmamışsa ve atanacak derslik boş ise derse dersliği atar.
	Derslik instance'ının derslik_bos_mu() fonk. kullanarak dersliğin boş olup olmadığını
	kontrol eder
	'''
	def derslik_ata(self, atanacak_derslik):
		if self.derslik is None and atanacak_derslik.derslik_bos_mu():
			self.derslik = atanacak_derslik
			atanacak_derslik.atanan_ders = self
		elif self.derslik is None and not atanacak_derslik.derslik_bos_mu():
			print(f"Bu Dersliğe Zaten {atanacak_derslik.atanan_ders} Dersi Atanmış, Yeni Ders Atamadan Önce Bu Dersi Kaldırmalısınız")
		elif self.derslik is not None:
			print("Derslik Zaten Atanmış")
		
	# Derse derslik atanmışsa çağrıldığında dersliği silen fonk. 
	def derslik_sil(self):
		if self.derslik is not None:
			self.derslik = None
		else:
			print("Henüz Derslik Atanmamış")
	# representation of Ders class.
	def __repr__(self):
		return f"{self.ad}"

	'''
	Seçmeli_Ders, Ders class'ının bir sub-class'ıdır. init yönteminde ana class a ek olarak 
	kontenjanı argument olarak alır. Böylelikle bir öğrenciyi derse kaydetmeden önce
	derste kontenjan olup olmadığını kontrol eder. 

	Ayrıca Ders class'ın ogrenci_kaydet fonksiyonuna yeni bir özellik daha kazandırarak
	öğrencinin seçmeli ders alma hakkı olup olmadığını kontrol eder.
	Bunu ogrenci class'ının secmeli_ders_alabilir() yöntemini kullanarak kontrol eder. 
	'''
class Secmeli_Ders(Ders):
	def __init__(self, ad, kontenjan, derslik=None, ogrenci_listesi=None):
		super().__init__(ad, derslik=None, ogrenci_listesi=None)
		self.kontenjan = kontenjan

	def ogrenci_kaydet(self, ogrenci):
		if len(self.ogrenci_listesi) < self.kontenjan and ogrenci.secmeli_ders_alabilir_mi():
			super().ogrenci_kaydet(ogrenci)
		elif len(self.ogrenci_listesi) < self.kontenjan and not ogrenci.secmeli_ders_alabilir_mi():
			print("Öğrenci Alabileceği Maksimum Seçmeli Ders Sayısına Ulaşmış")
		else:
			print("Kontenjan Dolu")
	'''
	Bu fonksiyon da Ders class ın derslik_ata yöntemine yeni bir özellik kazandırarak
	atanacak dersliğin kapasitesinin ders için belirlenen kontenjandan az olmadığını
	kontrol eder.
	''' 
	def derslik_ata(self, atanacak_derslik):
		if atanacak_derslik.kapasite >= self.kontenjan:
			super().derslik_ata(atanacak_derslik)
		else:
			print("Atanmaya Çalışılan Derslik Kapasitesi Kontenjandan Az Olamaz")
	'''
	Dersin kontenjanını arttırmak ve azaltmak için kullanılan yöntemler.
	kontenjan_azalt yöntemi dersin kontenjanının kayıtlı öğrenci listesinden
	az olmadığını ve kontenjanın 0 olmadığını kontrol eder. 
	kontenjan arttır yöntemi derslik kapasitesinin aşılıp aşılmadığını kontrol eder. 
	'''
	def kontenjan_arttir(self):
		if self.derslik is not None:
			if self.kontenjan < self.derslik.kapasite:
				self.kontenjan += 1
			else:
				print("Derslik Kapasitesi Dolu")
		else:
			print("Henüz Derslik Atanmamış. Önce Derslik Atayınız.")

	def kontenjan_azalt(self):
		if self.kontenjan != 0 and self.kontenjan > len(self.ogrenci_listesi):
			self.kontenjan -= 1
		elif self.kontenjan != 0 and self.kontenjan == len(self.ogrenci_listesi):
			print("Kontenjan ile Kayıtlı Öğrenci Sayısı Eşit \n Kontenjan Azaltmadan Önce Öğrenci Silmelisiniz!")
		else:
			print("Dersin Kontenjanı Sıfır")
		
	def __repr__(self):
		return f"{self.ad}"

	'''
	Zorunlu_Ders, Ders class'ının bir sub-class'ıdır. Dersin ön koşulunu kontrol etmek için
	kosullu_ders argümanını alır. Eğer dersin koşulu var ise ogrenci_kaydet fonksiyonu
	yeni bir özellik kaanarak dersin ön koşulunu öğrencinin sağlayıp sağlamadığını 
	kontrol eder. 
	'''
class Zorunlu_Ders(Ders):
	def __init__(self, ad,  kosullu_ders=None, derslik=None, ogrenci_listesi=None):
		super().__init__(ad, derslik=None, ogrenci_listesi=None)
		self.kosullu_ders = kosullu_ders

	def ogrenci_kaydet(self, ogrenci):
		if self.kosullu_ders is not None and self.kosullu_ders in ogrenci.ders_listesi:
			super().ogrenci_kaydet(ogrenci)
		elif self.kosullu_ders is None:
			super().ogrenci_kaydet(ogrenci)
		else:
			print("Öğrenci Dersin Ön Koşulunu Sağlamıyor")

	def __repr__(self):
		return f"{self.ad}"

	'''
	Derslik class derslerin yerini ve kapasitesini belirlemek için kullanılan
	class'tır. derslik_bos_mu yöntemi ile Derslik object'in boş olup olmadığı 
	kontrol edilir. Böylelikle derslik doluysa bu derslik başka bir Ders object'ine atanamaz.
	self.atanan_ders argümanı dersliğe atanan dersi object olarak tutar. 
	'''

class Derslik:
	def __init__(self, ad, kapasite, atanan_ders=None):
		self.ad = ad
		self.kapasite = kapasite
		self.atanan_ders = atanan_ders

	def derslik_bos_mu(self):
		if self.atanan_ders is None:
			return True
		else:
			return False
	# dersliğin durumunu, eğer dolu ise hangi dersin atandığını ekrana yazdıran fonk.
	def derslik_durumu_goruntule(self):
		if not self.derslik_bos_mu():
			print(f"Bu Dersliğe {self.atanan_ders} Dersi Atanmış")
		else:
			print("Bu Dersliğe Henüz Ders Atanmamış")

	def __repr__(self):
		return f"{self.ad}"

	'''
	Ogrenci class'ı derse kayıtlı öğrencileri temsil etmek için oluşturulmuş bir objecttir.
	max_secmeli_ders argümanı öğrencinin almasına izin verilen maximum ders sayısını belirlemek
	için kullanılır. Böylelikle öğrencinin izin verilenden fazla ders almasının önüne geçilmiş olur. 
	'''

class Ogrenci:
	def __init__(self, ad, soyad, numara, max_secmeli_ders=2, ders_listesi=None):
		self.ad = ad
		self.soyad = soyad
		self.numara = numara
		self.max_secmeli_ders = max_secmeli_ders
		if ders_listesi is None:
			self.ders_listesi = []
		else:
			self.ders_listesi = ders_listesi

	# ogrencinin seçmeli ders alma hakkı var mı kontrol eden yöntem. 
	def secmeli_ders_alabilir_mi(self):
		secmeli_ders_sayisi = 0
		for i in self.ders_listesi:
			if isinstance(i, Secmeli_Ders):
				secmeli_ders_sayisi += 1
			else:
				continue
		if secmeli_ders_sayisi < self.max_secmeli_ders:
			return True
		else:
			return False

	# öğrencinin kayıtlı olduğu dersleri ekrana yazdıran yöntem. 
	def ogrenci_ders_listesi_yazdir(self):
		print(f"{self.__repr__()} İsimli öğrencinin Kayıtlı Olduğu Dersler: \n{self.ders_listesi}")

	def __repr__(self):
		return f"{self.ad} {self.soyad}"