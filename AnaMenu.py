import hesapMakinesi 
import sporTurleriHakkindaBilgi 
import notOrtalamasi 
import yasHesabi 
import boyKiloEndeksi 
import sicaklikCevirme 
import oyun.Oyunlar 

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
    soru=int(input("Seçiminizi yapın."))
    print()
    if secim == "1": hesapMakinesi.hesapmenu()
    elif secim == "2": sporTurleriHakkindaBilgi.spormenu()
    elif secim == "3": notOrtalamasi.notmenu()
    elif secim == "4": yasHesabi.yasmenu()
    elif secim == "5": boyKiloEndeksi.boykilo()
    elif secim == "6": sicaklikCevirme.sicaklikmenu()
    elif secim == "7": oyun.oyunmenu()

    secim = input()
