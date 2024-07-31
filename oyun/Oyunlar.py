import oyun.yilan as oy
def oyunmenu():
    print("╔═════════════════════════════╗")
    print("║           OYUNLAR           ║")
    print("║ 1-Yılan                     ║")
    print("║ 2-Tetris                    ║")
    print("║                             ║")
    print("║                             ║")
    print("║                             ║")
    print("╚═════════════════════════════╝")
    secim = input()
    if secim == "1": oy.yilanoyna()