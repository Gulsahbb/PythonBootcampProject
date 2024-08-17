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

            bilgisayar_secimi = random.choice(secenekler).lower()
            print(f'\n• Oyuncu Seçimi : {oyuncu_secimi}')
            print(f'• Bilgisayar Seçimi : {bilgisayar_secimi}\n')

            if oyuncu_secimi == bilgisayar_secimi:
                print(f'Bu Tur Berabere! - {random.choice(beraberlik_mesaji)}\n')
            elif ((oyuncu_secimi == 'taş' and bilgisayar_secimi == 'makas') or
                  (oyuncu_secimi == 'makas' and bilgisayar_secimi == 'kağıt') or 
                  (oyuncu_secimi == 'kağıt' and bilgisayar_secimi == 'taş')):
                    oyuncu_galibiyeti += 1
                    print(f'Bu Turu Sen Kazandın!! - {random.choice(oyuncu_galibiyet_mesaji)}\n')
            else:
                bilgisayar_galibiyeti += 1
                print(f'Bu Turu Bilgisayar Kazandı!! - {random.choice(bilgisayar_galibiyet_mesaji)}\n')
    
            print(f'############# Oyuncu {oyuncu_galibiyeti} - {bilgisayar_galibiyeti} Bilgisayar ############\n')
        
        if oyuncu_galibiyeti == 2:
            print('OYUNU KAZANAN : Oyuncu')
        else:
            print('OYUNU KAZANAN : Bilgisayar')

        devam_bilgisayar = random.choice(['e','h'])
        devam_oyuncu = input('Oyuna Devam Etmek İstiyor Musun? (e/h) : ')

        if devam_oyuncu == 'e' and devam_bilgisayar == 'e':
            print('İki tarafta oynamaya devam etmek istiyor. Oyun Başlıyor...')
            continue
        elif devam_oyuncu == 'h' and devam_bilgisayar == 'e':
            print('Oyundan çıkmak istiyorsunuz. Görüşmek Üzere...')
            break
        else:
            print('Bilgisayar Oyuna Devam Etmek İstemiyor. Görüşmek Üzere...')
            break

tas_kagit_makas_GULSAH_BASKURT()