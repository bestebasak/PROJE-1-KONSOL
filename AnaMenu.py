import hesapMakinesi
import sporTurleriHakkindaBilgi 
import notOrtalamasi
import yasHesabi 
import boyKiloEndeksi 
import sicaklikCevirme
import oyun.Oyunlar 
import sys
import time
def anamenu(): 
    print("╔══════════════════*══════════════════╗")
    print("║               ANA MENÜ              ║")
    print("║                                     ║")
    print("║ 1-Hesap Makinesi                    ║")
    print("║ 2-Spor Türleri Hakkında Bilgi       ║")
    print("║ 3-Not Ortalaması                    ║")
    print("║ 4-Yaş Hesabı                        ║")
    print("║ 5-Boy Kilo Endeksi                  ║")
    print("║ 6-Sıcaklık Çevirme                  ║")
    print("║ 7-Oyunlar                           ║")
    print("║ 8-ÇIKIŞ                             ║")
    print("║                                     ║")
    print("║             SEÇİMİNİ YAP            ║")
    print("╚═════════════════════════════════════╝")

# def selection():
    secim=int(input("Seçiminizi yapın: "))
    print()
    if secim == 1 : 
        print("Hesap makinesini seçtiniz.")
        hesapMakinesi.hesapmenu()
    elif secim == 2 :
        print("Spor türleri hakkında bilgi almak istediniz.")
        sporTurleriHakkindaBilgi.spormenu()
    elif secim == 3 :
        print("Not ortalamanızı hesaplamak istediniz.")
        notOrtalamasi.notmenu()
    elif secim == 4 :
        print("Yaşınızı hesaplamak istediniz.")
        yasHesabi.yasmenu()
    elif secim == 5 :
        print("Boy kilo endeksinize bakmak istediniz.")
        boyKiloEndeksi.boykilo()
    elif secim == 6 : 
        print("Sıcaklığı öğrenmek istediniz.")
        sicaklikCevirme.sicaklikmenu()
    elif secim == 7 :
        print("Oyun oynamak istediniz.")
        oyun.Oyunlar.oyunmenu()
    elif secim ==  8 :
        print("Çıkış yapmak istediniz.")
        time.sleep(1)
        sys.exit()
    else: 
        print("Lütfen geçerli bir sayı giriniz!")
    anamenu()
anamenu()
        

# def run():
#     anamenu()
#     selection()

# if __name__ == "__main__":
#     run()

