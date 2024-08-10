import hesapMakinesi as hm
import sporTurleriHakkindaBilgi as st
import notOrtalamasi as noto
import yasHesabi as yh
import boyKiloEndeksi as byk
import sicaklikCevirme as sc
import oyun.Oyunlar as oo

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
    print("║ 7-ÇIKIŞ                             ║")
    print("║                                     ║")
    print("║             SEÇİMİNİ YAP            ║")
    print("╚═════════════════════════════════════╝")
    secim = input()

    if secim =="1": 
    if secim =="2": 
    if secim =="3": 
    if secim =="4": 
    if secim =="5": 
    if secim =="6": 
    if secim =="7": oo.oyunmenu()

anamenu()