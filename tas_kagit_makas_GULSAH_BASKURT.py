# Rastgele seçimler yapmak için kullanıldı.
import random


def tas_kagit_makas_GULSAH_BASKURT():

    mesaj = """
            
    ############# TAŞ KAĞIT MAKAS OYUNU #############

    1 - Taş, makası yener.
    2 - Makas, kağıdı yener.
    3 - Kağıt, taşı yener.
    4 - İlk iki turu kazanan oyunu kazanır.
    Her oyun sonrası bilgisayar ve oyuncuya oynamak
    veya çıkmak isteği sorulur.
    Her iki tarafta oynamak isterse oyun devam eder.
    Oyundan çıkmak istiyorsanız 'exit' yazın.

    ################# İYİ EĞLENCELER #################
        """

    secenekler = ['taş','kağıt','makas']
    oyuncu_galibiyet_mesaji = ['Harikasın!!','Böyle Devam','Muhteşem!!']
    bilgisayar_galibiyet_mesaji = ['Hah! Ben Kazandım','Odaklan Dostum','Yaşasın!!']
    beraberlik_mesaji = ['Şanslısın','Tüh!!','Seni alt edeceğim...']

    while True:
        print(mesaj)
        oyuncu_galibiyeti = 0
        bilgisayar_galibiyeti = 0
        tur_sayisi = 0

        while oyuncu_galibiyeti < 2 and bilgisayar_galibiyeti < 2:
            tur_sayisi += 1
            print(f'################### {tur_sayisi}.TUR ########################\n')
            oyuncu_secimi = input('Taş, Kağıt, Makas veya çıkmak için exit.\nLütfen birini seçiniz : ').lower()

            if oyuncu_secimi == 'exit':
                print('Oyundan Ayrılıyorsunuz. Görüşmek Üzere...')
                return
            elif oyuncu_secimi not in secenekler:
                print('Geçersiz bir seçim yaptınız. Program kapanıyor...')
                return
tas_kagit_makas_GULSAH_BASKURT()