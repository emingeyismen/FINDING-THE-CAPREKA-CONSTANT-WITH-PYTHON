def numberSort1(number,reverse):
    rakamlar = list(str(number))
    if reverse:
        for i in range(len(rakamlar)):
            for j in range(i+1, len(rakamlar)):
                if rakamlar[i] > rakamlar[j]:
                    rakamlar[i],rakamlar[j] = rakamlar[j],rakamlar[i]
    
    else:
         for i in range(len(rakamlar)):
            for j in range(i+1, len(rakamlar)):
                if rakamlar[i] < rakamlar[j]:
                    rakamlar[i],rakamlar[j] = rakamlar[j],rakamlar[i]
    sıralama = int("".join(rakamlar))
    return sıralama

def kapreka(number1):
    while True:

        küçük = numberSort1(number1,reverse=True)
        büyük = numberSort1(number1,reverse=False)

    
        sonuc = büyük - küçük

        print(büyük,"-",küçük,"=",sonuc)

        if sonuc == 6174:
            break

        number1 = sonuc
    return sonuc    
    



print(kapreka(1234))
