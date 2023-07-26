while True:
    
    #iki sayılı bir işlemli basit bir hesap makinesi
    
    s1 = float(input("birinci sayıyı giriniz      :"))
    i = input("işlemi giriniz (+,-,*,/)     :")
    s2 = float(input("ikinci sayıyı giriniz       :"))
    
    #işlemi gerçekleştirdiğimiz kısım
    
    if i == "+":
        sonuc = s1 + s2
    elif i == "-":
        sonuc = s1 - s2
    elif i == "*":
        sonuc = s1 * s2
    elif i == "/":
        sonuc = s1 / s2
    else:
        print("yanlış işlem tuşladınız (!)")
        continue
    
    #←sonuç kısımı
    print("Sonuç    :", sonuc)
    
    #devam etme kısmı olsun
    
    devam = input("Başka bir işlem yapmak ister misiniz? (Evet:E,e; Hayır:H,h) tuşlayınız   :")
    if devam.upper() !="E":
        break
    while True:
    
    #iki sayılı bir işlemli basit bir hesap makinesi
    
    s1 = float(input("birinci sayıyı giriniz      :"))
    i = input("işlemi giriniz (+,-,*,/)     :")
    s2 = float(input("ikinci sayıyı giriniz       :"))
    
    #işlemi gerçekleştirdiğimiz kısım
    
    if i == "+":
        sonuc = s1 + s2
    elif i == "-":
        sonuc = s1 - s2
    elif i == "*":
        sonuc = s1 * s2
    elif i == "/":
        sonuc = s1 / s2
    else:
        print("yanlış işlem tuşladınız (!)")
        continue
    
    #←sonuç kısımı
    print("Sonuç    :", sonuc)
    
    #devam etme kısmı olsun
    
    devam = input("Başka bir işlem yapmak ister misiniz? (Evet:E,e; Hayır:H,h) tuşlayınız   :")
    if devam.upper() !="E":
        break
    
