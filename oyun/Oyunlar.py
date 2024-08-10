import Oyunlar.yilan 
def oyunmenu():
    print("╔═════════════════════════════╗")
    print("║           OYUNLAR           ║")
    print("║ 1-Yılan                     ║")
    print("║ 2-Tetris                    ║")
    print("║ 3-Yazı-Tura                 ║")
    print("║ 4-Satranç                   ║")
    print("║                             ║")
    print("╚═════════════════════════════╝")
    secim = input()
    if secim == "1": Oyunlar.yilanoyna()