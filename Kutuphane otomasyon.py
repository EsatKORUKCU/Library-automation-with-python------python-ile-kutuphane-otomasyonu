# Sözlük (dict) ve Class yapısı kullanarak Kütüphanesi Otomasyonu Tasarımı
# Özgün Kod Paylaşımı GitLab
"""
1-Kitap Ekle
2-Kitap Listele
3-Kitap Ara
4-Yönetici Ekle
5-Yönetici Listele
6-Çıkış

"""
from time import sleep
import os

class Yonetici:
    yoneticiSozluk = {}
    
    def yoneticiEkleme(self):
        self.yoneticiSicil = input("Yonetici Sicil No Gir.: ")
        self.yoneticiAdi = input("Yonetici Adı Soyadı Girin.: ")
        self.yoneticiMaas = int(input("Yonetici Maaşı Girin.: "))
        
        self.yoneticiSozluk[self.yoneticiSicil] = {
            "yoneticiAdi": self.yoneticiAdi,
            "yoneticiMaas": self.yoneticiMaas
        }
        sleep(1)
        print("bilgiler Başarı İle Eklendi")
        sleep(1)
        os.system("cls")
    
    def yoneticileriListele(self):
        if (self.yoneticiSozluk == {}):
            print("Yonetici Bilgisi Bulunamadı")
            sleep(1)
        else:
            for yonetici in self.yoneticiSozluk:
                print(yonetici, self.yoneticiSozluk[yonetici])
                sleep(2)

class BenimKutuphanem(Yonetici):   
    kitaplarSozluk = dict()
    
    def __init__(self):
        while True:
            os.system("cls")
            print(" Kütüphane Otomasyonu ".center(30, "*"))
            print("""
    1- Kitap Ekle
    2- Kitap Listele
    3- Kitap Ara
    4- Kitap Sil
    5- Kitap Güncelle
    6- Yönetici Ekle
    7- Yönetici Listele
    8- Çıkış """)
            secim = int(input("Seçiminiz (1-8)\t: "))
            if(secim == 1):
                self.kitapEkle()
            elif secim == 2:
                self.kitapListele()
            elif secim == 3:
                self.kitapAra()
            elif secim == 4:
                self.kitapsil()
            elif secim == 5:
                self.kitapguncelle()
            elif secim == 6:
                super().yoneticiEkleme()
            elif secim == 7:
                super().yoneticileriListele()
            elif secim == 8:
                self.cikis()
            
            else:
                print("Hatalı Deger Girildi")
                continue
                       
    
    def kitapEkle(self):
        os.system("cls")
        tane = int(input("Kaç tane kitap girilecek.: "))
        for adet in range(tane):
            self.kitapID = input("Kitap ID Gir.: ")
            self.kitapAdi = input("Kitap Adı Gir: ")
            self.yazarAdi = input("Kitabın Yazarı.: ")
            self.kitapTuru = input("Kitap Türü Gir.: ")
            self.kitapFiyat = float(input("Kitap Fiyat Gir.: "))
            self.kitaplarSozluk[self.kitapID] = {
                "kitapAdi": self.kitapAdi,
                "yazarAdi": self.yazarAdi,
                "kitapTuru": self.kitapTuru,
                "kitapFiyat": self.kitapFiyat
            }
            sleep(0.5)
            print("Bilgiler Kaydedildi")
            
            
    def kitapListele(self):
  
        if len(self.kitaplarSozluk) == 0:
            print("Kayıtlı Kitap Bulunamadı")
            sleep(1)
        else:
            for kitap in self.kitaplarSozluk:
                print(kitap, self.kitaplarSozluk[kitap])
            sleep(2)
            
    
    def kitapAra(self):
        os.system("cls")
        self.kitapArama = input("Kitap ID sini Girin.: ")
        
        try:
            arama = self.kitaplarSozluk[str(self.kitapArama)]
            print(" Kitaplar Listeleniyor ".center(30,"═")) # Alt+205
            print("""
        Kitap Adı.......: {}
        Yazar Adı.......: {}
        Kitap Türü......: {}
        Kitap Fiyat.....: {}""".format( arama["kitapAdi"], arama["yazarAdi"], arama["kitapTuru"], arama["kitapFiyat"]))
            sleep(2)
        except:
            print("Kitap Bulunamadı")
            sleep(2)
    
    def kitapsil(self):
        os.system("cls")
        self.kitapgüncelleme = input("Silinecek Kitabın IDsini girin  : ")
        self.kitaplarSozluk[self.kitapgüncelleme] 
        self.kitaplarSozluk.pop(self.kitapgüncelleme)
       
    def kitapguncelle(self):
        self.kitapgüncelleme = input("Kitap ID sini Girin.: ")
        if len(self.kitaplarSozluk) == len(self.kitapgüncelleme):
        
            self.kitapAdi = input("Kitap Adı Gir: ")
            self.yazarAdi = input("Kitabın Yazarı.: ")
            self.kitapTuru = input("Kitap Türü Gir.: ")
            self.kitapFiyat = float(input("Kitap Fiyat Gir.: "))
            self.kitaplarSozluk[self.kitapID] = {
                "kitapAdi": self.kitapAdi,
                "yazarAdi": self.yazarAdi,
                "kitapTuru": self.kitapTuru,
                "kitapFiyat": self.kitapFiyat
            }
            sleep(1)
            print("Bilgiler güncellendi")
        else:
            print("Yanlış giriş yapıldı")
    def cikis(self):
        print("Program Sonlandırılıyor..")
        exit(0)
    
            
kutuphane = BenimKutuphanem()