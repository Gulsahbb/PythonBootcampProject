import random

def tas_kagit_makas_GULSAH_BASKURT():
    # Oyunun açıklama ve kurallarını içeren mesaj
    mesaj = """
############# TAŞ KAĞIT MAKAS OYUNU ##############

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

    # Seçenekler ve mesajlar
    secenekler = ['taş','kağıt','makas']
    oyuncu_galibiyet_mesaji = ['Harikasın!!','Böyle Devam','Muhteşem!!']
    bilgisayar_galibiyet_mesaji = ['Hah! Ben Kazandım','Odaklan Dostum','Yaşasın!!']
    beraberlik_mesaji = ['Şanslısın','Tüh!!','Seni alt edeceğim...']

    while True:
        print(mesaj)  # Oyun kurallarını ve açıklamaları yazdır
        oyuncu_galibiyeti = 0  # Oyuncunun galibiyet sayısını başlat
        bilgisayar_galibiyeti = 0  # Bilgisayarın galibiyet sayısını başlat
        tur_sayisi = 0  # Tur sayısını başlat

        # Oyun döngüsü, oyuncu veya bilgisayar iki galibiyete ulaşana kadar devam eder
        while oyuncu_galibiyeti < 2 and bilgisayar_galibiyeti < 2:
            tur_sayisi += 1  # Tur sayısını artır
            print(f'################### {tur_sayisi}.TUR ########################\n')
            oyuncu_secimi = input('Taş, Kağıt, Makas veya çıkmak için exit.\nLütfen birini seçiniz : ').lower()

            if oyuncu_secimi == 'exit':
                # Oyuncu çıkmak isterse, oyunu sonlandır
                print('Oyundan Ayrılıyorsunuz. Görüşmek Üzere...')
                return
            elif oyuncu_secimi not in secenekler:
                # Geçersiz seçim yapıldıysa, oyunu sonlandır
                print('Geçersiz bir seçim yaptınız. Program kapanıyor...')
                return

            # Bilgisayarın rastgele seçim yapmasını sağla
            bilgisayar_secimi = random.choice(secenekler).lower()
            print(f'\n• Oyuncu Seçimi : {oyuncu_secimi}')
            print(f'• Bilgisayar Seçimi : {bilgisayar_secimi}\n')

            # Sonuçları değerlendir ve galibiyetleri güncelle
            if oyuncu_secimi == bilgisayar_secimi:
                print(f'Bu Tur Berabere! - {random.choice(beraberlik_mesaji)}\n')
            elif ((oyuncu_secimi == 'taş' and bilgisayar_secimi == 'makas') or
                  (oyuncu_secimi == 'makas' and bilgisayar_secimi == 'kağıt') or 
                  (oyuncu_secimi == 'kağıt' and bilgisayar_secimi == 'taş')):
                oyuncu_galibiyeti += 1  # Oyuncu bu turu kazandı
                print(f'Bu Turu Sen Kazandın!! - {random.choice(oyuncu_galibiyet_mesaji)}\n')
            else:
                bilgisayar_galibiyeti += 1  # Bilgisayar bu turu kazandı
                print(f'Bu Turu Bilgisayar Kazandı!! - {random.choice(bilgisayar_galibiyet_mesaji)}\n')
    
            # Oyuncu ve bilgisayarın galibiyetlerini göster
            print(f'############# Oyuncu {oyuncu_galibiyeti} - {bilgisayar_galibiyeti} Bilgisayar ############\n')
        
        # Oyunun sonucunu belirle
        if oyuncu_galibiyeti == 2:
            print('OYUNU KAZANAN : Oyuncu')
        else:
            print('OYUNU KAZANAN : Bilgisayar')


        # Oyuna devam etmek isteyip istemediğini sor
        devam_bilgisayar = random.choice(['e','h'])  # Bilgisayarın devam etme isteğini rastgele belirle
        devam_oyuncu = input('Oyuna Devam Etmek İstiyor Musun? (e/h) : ')

        if devam_oyuncu == 'e' and devam_bilgisayar == 'e':
            # Hem oyuncu hem de bilgisayar oynamaya devam etmek istiyorsa
            print('İki tarafta oynamaya devam etmek istiyor. Oyun Başlıyor...')
            continue
        elif devam_oyuncu == 'h' and devam_bilgisayar == 'e':
            # Oyuncu oynamak istemiyor ancak bilgisayar devam etmek istiyor
            print('Oyundan çıkmak istiyorsunuz. Görüşmek Üzere...')
            break
        else:
            # Bilgisayar oynamak istemiyor
            print('Bilgisayar Oyuna Devam Etmek İstemiyor. Görüşmek Üzere...')
            break

# Fonksiyonu çağırarak oyunu başlat
tas_kagit_makas_GULSAH_BASKURT()