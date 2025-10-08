# Fonksiyon Oluşturma

**Soru:** Hangisi ile fonksiyon oluşturulur?

    __init__ fonksiyon1():
    func fonksiyon1():
    def fonksiyon1():
    const fonksiyon1():
    class fonksiyon1():

**Cevap:**\
`def fonksiyon1():`

------------------------------------------------------------------------

# Tür Dönüşümü

**Soru:** Aşağıdaki işlemlerin tür dönüşümü sonrası matematiksel
işlemlerde kullanılabilmesi ve tam sayı değer vermesi için boş bırakılan
yerlere ne gelmelidir?

``` python
a = .......................(input("vize notunuzu girin = "))
```

**Cevap:**\
`int(...)`

------------------------------------------------------------------------

# Karar Yapıları

**Soru:** Aşağıdakilerden hangisi karar yapılarında kullanılan
deyimlerden birisi değildir?

    while
    continue
    if... :  elif....:  else:
    break
    def

**Cevap:**\
`def`

------------------------------------------------------------------------

# Nesne Tabanlı Programlama Kavramları

## Encapsulation (Kılıflama-Sarmalama) Nedir?

Nesnelerin verilerini ve bu veriler üzerinde işlem yapan metotları bir
araya toplayarak dışarıdan direkt erişimi kısıtlama prensibidir. Bu,
veri güvenliğini artırır ve programın daha düzenli olmasını sağlar.

## Inheritance (Kalıtım) Nedir?

Bir sınıfın (alt sınıf/çocuk sınıf), başka bir sınıfın (üst sınıf/ata
sınıf) özelliklerini ve metotlarını miras almasıdır. Bu sayede kod
tekrarı önlenir ve daha düzenli bir yapı oluşturulur.

------------------------------------------------------------------------

# Nesne Tabanlı Programlama Örneği: İnsan, Öğrenci ve Hoca Sınıfları

Bu örnekte, **kalıtım (inheritance)**, **metot ezme (overriding)** ve
**çok biçimlilik (polymorphism)** prensipleri gösterilmiştir.

``` python
class Insan:
    def __init__(self, isim, yas, cinsiyet):
        self.isim = isim
        self.__yas = yas  # Kapsülleme (private attribute)
        self.cinsiyet = cinsiyet

    def bilgi_ver(self):
        print(f"İsim: {self.isim}, Yaş: {self.__yas}, Cinsiyet: {self.cinsiyet}")

    def konus(self):
        print("Genel bir insan konuşuyor.")

    def get_yas(self):
        return self.__yas

    def set_yas(self, yeni_yas):
        if yeni_yas > 0:
            self.__yas = yeni_yas

class Hoca(Insan):
    def __init__(self, isim, yas, cinsiyet, brans):
        super().__init__(isim, yas, cinsiyet)
        self.brans = brans

    def konus(self):  # Metot ezme (Overriding)
        print(f"{self.isim} adlı hoca {self.brans} dersini anlatıyor.")

class Ogrenci(Insan):
    def __init__(self, isim, yas, cinsiyet, okul_no):
        super().__init__(isim, yas, cinsiyet)
        self.okul_no = okul_no

    def konus(self):  # Metot ezme (Overriding)
        print(f"{self.isim} adlı öğrenci ders hakkında konuşuyor.")

# Çok biçimlilik (Polymorphism)
def konustur(nesne):
    nesne.konus()

# Nesneler
insan1 = Insan("Ahmet", 25, "Erkek")
hoca1 = Hoca("Ayşe", 40, "Kadın", "Matematik")
ogrenci1 = Ogrenci("Mehmet", 18, "Erkek", 123)

# Kullanım
print("--- Bilgi Verme ---")
insan1.bilgi_ver()
hoca1.bilgi_ver()
ogrenci1.bilgi_ver()

print("\n--- Çok Biçimlilik (Polymorphism) ---")
konustur(insan1)
konustur(hoca1)
konustur(ogrenci1)
```

------------------------------------------------------------------------

# Çalışan Sınıfları ve Soyut Sınıf Örneği

Bu örnekte, **kalıtım**, **metot ezme (overriding)** ve **soyut sınıflar
(abstract classes)** kullanılmıştır. Soyut sınıflar için `abc` modülünü
kullanıyoruz.

``` python
from abc import ABC, abstractmethod

# Soyut Sınıf
class Ozgecmis(ABC):
    @abstractmethod
    def doldur(self):
        pass

# Ata Sınıf
class Calisan(Ozgecmis):
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim

    def doldur(self):
        print(f"{self.isim} {self.soyisim} için özgeçmiş dolduruluyor.")

# Alt Sınıflar
class MaviYaka(Calisan):
    def __init__(self, isim, soyisim):
        super().__init__(isim, soyisim)
        self.vardiya_sayisi = 3

    def calis(self):  # Metot ezme (Overriding)
        print("Mavi yaka çalışan tezgahta/fabrika içinde çalışıyor.")

class BeyazYaka(Calisan):
    def __init__(self, isim, soyisim):
        super().__init__(isim, soyisim)
        self.vardiya_sayisi = 2

    def calis(self):  # Metot ezme (Overriding)
        print("Beyaz yaka çalışan masa başında çalışıyor.")

# Nesne Türetme
mavi_yaka1 = MaviYaka("Ali", "Yılmaz")
beyaz_yaka1 = BeyazYaka("Ayşe", "Kaya")

# Kullanım
print("--- Çalışanlar ---")
mavi_yaka1.doldur()
mavi_yaka1.calis()
print(f"Vardiya sayısı: {mavi_yaka1.vardiya_sayisi}")

print("\n--- Çalışanlar ---")
beyaz_yaka1.doldur()
beyaz_yaka1.calis()
print(f"Vardiya sayısı: {beyaz_yaka1.vardiya_sayisi}")
```

------------------------------------------------------------------------
