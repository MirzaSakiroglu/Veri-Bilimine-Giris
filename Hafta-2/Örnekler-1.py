class Insan:
    def __init__(self, isim, yas, cinsiyet):
        self.isim = isim
        self.__yas = yas 
        self.cinsiyet = cinsiyet

    def bilgi_ver(self):
        print(f"İsim: {self.isim}, Yaş: {self.__yas}, Cinsiyet: {self.cinsiyet}")

    def get_yas(self):
        return self.__yas

    def set_yas(self, yeni_yas):
        self.__yas = yeni_yas

    def konus(self):
        print("İnsan konuşuyor...")

class Hoca(Insan):
    def __init__(self, isim, yas, cinsiyet, brans):
        super().__init__(isim, yas, cinsiyet)
        self.brans = brans

    def konus(self):
        return f"{self.isim} adlı hoca {self.brans} dersini anlatıyor."

class Ogrenci(Insan):
    def __init__(self, isim, yas, cinsiyet, sinif, okul_no):
        super().__init__(isim, yas, cinsiyet)
        self.sinif = sinif
        self.__okul_no = okul_no

    def katil(self):
        return f"{self.isim} adlı öğrenci {self.sinif} sınıfında derse katılıyor."

    def konus(self):
        print("Öğrenci konuşuyor...")

    def get_okul_no(self):
        return self.__okul_no

    def set_okul_no(self, yeni_okul_no):
        self.__okul_no = yeni_okul_no

class Sekreter(Insan):
    def __init__(self, isim, yas, cinsiyet, departman):
        super().__init__(isim, yas, cinsiyet)
        self.departman = departman

    def evrak_isle(self):
        return f"{self.isim} adlı sekreter {self.departman} departmanında evrak işlerini yürütüyor."
    
    def konus(self):
        print("Sekreter konuşuyor...")

# Ana Program
insan1 = Insan("Ali", 30, "Erkek")
hoca1 = Hoca("Ayşe", 45, "Kadın", "Matematik")
ogrenci1 = Ogrenci("Fatma", 15, "Kadın", "10-A", 125)
sekreter1 = Sekreter("Zeynep", 35, "Kadın", "İnsan Kaynakları")

insan1.bilgi_ver()
insan1.konus()

hoca1.bilgi_ver()
print(hoca1.konus())

ogrenci1.bilgi_ver()
print(ogrenci1.katil())

sekreter1.bilgi_ver()
print(sekreter1.evrak_isle())

try:
    print(ogrenci1.__okul_no)
except AttributeError as e:
    print(f"Hata: {e} - Gizli özelliğe doğrudan erişilemez.")

print(f"Öğrencinin okul numarası: {ogrenci1.get_okul_no()}")
ogrenci1.set_okul_no(250)
print(f"Güncellenmiş okul numarası: {ogrenci1.get_okul_no()}")

hoca1.konus() 
ogrenci1.konus() 
sekreter1.konus()