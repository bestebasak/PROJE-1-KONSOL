import oyun.yilan 
import oyun.tetris
import oyun.yazitura
import oyun.satranc


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
    if secim == 1 : oyun.yilan.yilanoyna()
    elif secim == 2 : oyun.tetris.tetrisoyna()
    elif secim == 3 : oyun.yazitura()
    elif secim == 4 : oyun.satranc()