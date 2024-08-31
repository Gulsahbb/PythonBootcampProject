# Oyun geliştirmek için kullanılan bir kütüphane.
import pygame
# Rastgele seçimler yapmak için kullanıldı.
import random
# Sistemle ilgili işlevleri sağlayan kütüphane.
import sys


# Pygame kütüphanesin başlatıldı.
pygame.init()

# Ekran ayarları
screen_width, screen_height = 1000, 400 # Ekranın genişlik ve yükseklik değerlerini belirlendi.
screen = pygame.display.set_mode((screen_width, screen_height)) # Pygame ekran penceresi oluşturuldu.
pygame.display.set_caption('Kozmik Düello: Taş-Kâğıt-Makas') # Ekran başlığı ayarlanıldı.

# Renkler
DARK_BLUE = (20, 33, 61)
DARK_YELLOW = (252, 163, 17)
GREY = (229, 229, 229)
DARK_RED = (255,176,176)
DARK_GREEN = (252,103,54)

# Font
font = pygame.font.SysFont(None, 24) # Sistem fontunu kullanarak belirli bir font boyutu (24) ayarlamdı.

# Ekrana metin çizmek için kullanıldı.
def draw_text(text, font, color, surface, x, y, max_width):
    lines = text.split('\n')  # Metni satırlara böl
    y_offset = y
    for line in lines: # Her satır için: 
        words = line.split(' ') # satırı kelimelere böler. 
        current_line = ''
        for word in words:
            test_line = f'{current_line} {word}'.strip() # Mevcut satıra kelimeleri ekler ve metin objesini oluşturur.
            textobj = font.render(test_line, True, color)
            textrect = textobj.get_rect()
            if textrect.width > max_width:  # Metnin genişliği maksimum genişliği aşıyorsa yeni bir satıra geçer.
                surface.blit(font.render(current_line, True, color), (x - textrect.width // 2, y_offset)) # Metni belirtilen konumda ekrana çizer.
                current_line = word
                y_offset += font.get_height() + 5
            else:
                current_line = test_line
        surface.blit(font.render(current_line, True, color), (x - textrect.width // 2, y_offset))
        y_offset += (font.get_height())*2 + 5  # Satır yüksekliği ve biraz boşluk ekle


# Oyun başlangıcındaki metni gösterir.
def show_intro():
    # Tanıtım metni
    screen.fill(DARK_BLUE)
    draw_text('•••Taş, Kağıt, Makas Galaksisine Hoş Geldiniz!•••\n',font, DARK_YELLOW, screen, screen_width // 2, screen_height // 2 - 170, screen_width - 40)
    draw_text('Uzayın derinliklerinde, destansı bir düello sizi bekliyor! Taşlar, Kağıtlar ve Makaslar, bu evrende sonsuz bir rekabet içinde.\n',font, GREY, screen, screen_width // 2, screen_height // 2 - 120, screen_width - 40)
    draw_text('Göreviniz rakibinizi galaktik zeka ile alt edin. İlk iki turda zafere ulaşan, galaksinin yeni Kozmik Savaşçıı olacak!\n',font, GREY, screen, screen_width // 2, screen_height // 2 - 90, screen_width - 40)
    draw_text('Evrensel Kurallar:\n',font, DARK_YELLOW, screen, screen_width // 2, screen_height // 2 - 40, screen_width - 40)
    draw_text('   • Taş, Makas gezegenini paramparça eder.\n',font, GREY, screen, screen_width // 2, screen_height // 2 - 10, screen_width - 40)
    draw_text('   • Makas, Kağıt yıldızını ikiye böler.\n',font, GREY, screen, screen_width // 2, screen_height // 2 + 20, screen_width - 40)
    draw_text('   • Kağıt, Taş asteroidini sarar ve etkisiz hale getirir.\n',font, GREY, screen, screen_width // 2, screen_height // 2 + 50 , screen_width - 40)
    draw_text('Oyunun sonuna kadar galaktik becerilerinizi gösterin veya (q) basarak evinize geri dönün.\n',font, GREY, screen, screen_width // 2, screen_height // 2 + 100, screen_width - 40)
    draw_text('Yıldızlar sizinle olsun! Hazırsanız, epik savaş başlasın!',font, GREY, screen, screen_width // 2, screen_height // 2 + 130, screen_width - 40)
    draw_text('BAŞLIYOR...',font,DARK_YELLOW,screen,screen_width // 2,screen_height// 2 + 170,screen_width - 40)
    pygame.display.flip() # Ekrandaki değişiklikleri günceller.
    pygame.time.wait(5000)  # 5 saniye boyunca metni gösterir.

# Oyun Akışı
def tas_kagit_makas_GULSAH_BASKURT():
    # Oyuncu ve Bilgisayarın seçebileceği seçenekler bir liste halinde tutuluyor.
    seçenekler = ['taş', 'kağıt', 'makas']
    # Her sonuç durumu için farklı mesajlar liste halinde tutuluyor.
    bilgisayar_galibiyet_mesaji = ['Kozmik Rakip galip geldi! Yıldızlar bu sefer onun tarafında.', 'Güçlü değilsin... Evren bu mücadelede üstün geldi.']
    oyuncu_galibiyet_mesaji = ['Galaksi şampiyonu sensin!', 'Harikasın!']
    beraberlik_mesaji = ['Bu sadece bir denge! Kozmik güçler eşit dağıldı.', 'Birbirine denk güçler! Evrenin dengesini korudunuz.']

    show_intro()  # Tanıtım metnini gösterir.

    # Oyun bitene kadar bu döngü devam eder.
    while True:
        # Her yeni galibiyette bu sayılar sıfırlanır.
        oyuncu_galibiyeti = 0
        bilgisayar_galibiyeti = 0
        tur_sayisi = 0
    # Oyuncu ve bilgisayar 2 galibiyet alana kadar oyun devam eder. İlk 2 galibiyet alan oyunu kazanır.
        while oyuncu_galibiyeti < 2 and bilgisayar_galibiyeti < 2:
            screen.fill(DARK_BLUE) # Ekran belirlenen renk ile dolduruldu.
            # Oyuncuya seçim yapması için verilen metni ekrana çizer.
            tur_sayisi += 1
            draw_text(f'{tur_sayisi}.TUR', font, GREY, screen, screen_width // 2, screen_height // 2 - 110, screen_width - 40)
            draw_text('Gezegen güçlerinizi seçin:\n1: Taş Astroidi\n2: Kağıt Yıldızı\n3: Makas Meteor', font, GREY, screen, screen_width // 2, screen_height // 2 - 80, screen_width - 40)
            # Ekrandaki değişiklikleri günceller.
            pygame.display.flip()

            


# Dosya direkt olarak çalıştırıldıysa tas_kagit_makas_GULSAH_BASKURT() fonksiyonunun çağrılmasını sağlar.
if __name__ == '__main__':
    tas_kagit_makas_GULSAH_BASKURT()
