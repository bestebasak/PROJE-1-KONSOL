def boykilo():
    kilo=float(input("Kilonuzu Giriniz (kg): "))
    boy=float(input("Boyunuzu Giriniz (cm): "))
    boy/100
    boykiloendeksi= kilo / boy**2
    if boykiloendeksi<= 20: print("İdeal kilonuzun altındasınız.")
    elif 20< boykiloendeksi <= 25: print("Kilonuz ideal.")
    elif 25< boykiloendeksi <= 30: print("İdeal kilonuzun üstündesiniz.")
    else: print("İdeal kilonuzun çok üstündesiniz.")

