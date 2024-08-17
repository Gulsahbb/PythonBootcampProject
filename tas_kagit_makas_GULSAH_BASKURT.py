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
    
    print(mesaj)

tas_kagit_makas_GULSAH_BASKURT()