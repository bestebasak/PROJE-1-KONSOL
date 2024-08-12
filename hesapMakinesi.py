def hesapmenu():
    print("╔════════════════════════╗")
    print("║    HESAP MAKİNESİ      ║")
    print("║ 1-Toplama              ║")
    print("║ 2-Çıkarma              ║")
    print("║ 3-Çarpma               ║")
    print("║ 4-Bölme                ║")
    print("║                        ║")
    print("║       SEÇİNİZ          ║")
    print("╚════════════════════════╝")
    
secim=int(input("Seçiminizi yapın. "))
sayi1 = int(input("İlk sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

def toplama(sayi1,sayi2):
    return sayi1+sayi2
def cikarma(sayi1,sayi2):
    return sayi1-sayi2
def carpma(sayi1,sayi2):
    return sayi1*sayi2
def bolme(say1,sayi2):
    return sayi1/sayi2

if secim == "1" : print("Sonuç: ", toplama(sayi1,sayi2))
elif secim == "2" : print("Sonuç: ", cikarma(sayi1,sayi2))
elif secim == "3" : print("Sonuç: ", carpma(sayi1,sayi2))
elif secim == "4" : print("Sonuç: ", bolme(sayi1,sayi2))


input()