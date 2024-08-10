import Oyunlar.yilan 
import Oyunlar.tetris
import Oyunlar.yazitura
import Oyunlar.satranc


def oyunmenu():
    print("╔═════════════════════════════╗")
    print("║           OYUNLAR           ║")
    print("║ 1-Yılan                     ║")
    print("║ 2-Tetris                    ║")
    print("║ 3-Yazı-Tura                 ║")
    print("║ 4-Satranç                   ║")
    print("║     Seçiminizi Yapın        ║")
    print("╚═════════════════════════════╝")
    secim = int(input("Seçiminizi yapın: "))
    if secim == "1": Oyunlar.yilanoyna()
    elif secim == "2": Oyunlar.tetrisoyna()
    elif secim == "3" : Oyunlar.yazitura()
    else secim == "4": Oyunlar.satranc()