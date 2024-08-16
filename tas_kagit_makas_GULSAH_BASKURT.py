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
pygame.display.set_caption('Büyücüler Dünyası') # Ekran başlığı ayarlanıldı.

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
            test_line = f"{current_line} {word}".strip() # Mevcut satıra kelimeleri ekler ve metin objesini oluşturur.
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
    draw_text("•••Taş, Kağıt, Makas Galaksisine Hoş Geldiniz!•••\n",font, DARK_YELLOW, screen, screen_width // 2, screen_height // 2 - 170, screen_width - 40)
    draw_text("Uzayın derinliklerinde, destansı bir düello sizi bekliyor! Taşlar, Kağıtlar ve Makaslar, bu evrende sonsuz bir rekabet içinde.\n",font, GREY, screen, screen_width // 2, screen_height // 2 - 120, screen_width - 40)
    draw_text("Göreviniz rakibinizi galaktik zeka ile alt edin. İlk iki turda zafere ulaşan, galaksinin yeni kahramanı olacak!\n",font, GREY, screen, screen_width // 2, screen_height // 2 - 90, screen_width - 40)
    draw_text("Evrensel Kurallar:\n",font, DARK_YELLOW, screen, screen_width // 2, screen_height // 2 - 40, screen_width - 40)
    draw_text("   • Taş, Makas gezegenini paramparça eder.\n",font, GREY, screen, screen_width // 2, screen_height // 2 - 10, screen_width - 40)
    draw_text("   • Makas, Kağıt yıldızını ikiye böler.\n",font, GREY, screen, screen_width // 2, screen_height // 2 + 20, screen_width - 40)
    draw_text("   • Kağıt, Taş asteroidini sarar ve etkisiz hale getirir.\n",font, GREY, screen, screen_width // 2, screen_height // 2 + 50 , screen_width - 40)
    draw_text("Oyunun sonuna kadar galaktik becerilerinizi gösterin veya (q) basarak evinize geri dönün.\n",font, GREY, screen, screen_width // 2, screen_height // 2 + 100, screen_width - 40)
    draw_text("Yıldızlar sizinle olsun! Hazırsanız, epik savaş başlasın!",font, GREY, screen, screen_width // 2, screen_height // 2 + 130, screen_width - 40)
    draw_text("BAŞLIYOR...",font,DARK_YELLOW,screen,screen_width // 2,screen_height// 2 + 170,screen_width - 40)
    pygame.display.flip() # Ekrandaki değişiklikleri günceller.
    pygame.time.wait(5000)  # 5 saniye boyunca metni gösterir.

# Oyun Akışı
def tas_kagit_makas_GULSAH_BASKURT():
    # Oyuncu ve Bilgisayarın seçebileceği seçenekler bir liste halinde tutuluyor.
    seçenekler = ["taş", "kağıt", "makas"]
    # Her sonuç durumu için farklı mesajlar liste halinde tutuluyor.
    bilgisayar_galibiyet_mesaji = ["Karanlık lord kazandı!", "Güçlü değilsin..."]
    oyuncu_galibiyet_mesaji = ["Kehanet seni destekliyor!", "Harikasın!"]
    beraberlik_mesaji = ["Bu sadece bir denge!", "Birbirine denk güçler!"]

    show_intro()  # Tanıtım metnini gösterir.

    # Oyun bitene kadar bu döngü devam eder.
    while True:
        # Her yeni galibiyette bu sayılar sıfırlanır.
        oyuncu_galibiyeti = 0
        bilgisayar_galibiyeti = 0

    # Oyuncu ve bilgisayar 2 galibiyet alana kadar oyun devam eder. İlk 2 galibiyet alan oyunu kazanır.
        while oyuncu_galibiyeti < 2 and bilgisayar_galibiyeti < 2:
            screen.fill(DARK_BLUE) # Ekran belirlenen renk ile dolduruldu.
            # Oyuncuya seçim yapması için verilen metni ekrana çizer.
            draw_text('Gücünüzü seçin:\n1: Taş\n2: Kağıt\n3: Makas', font, GREY, screen, screen_width // 2, screen_height // 2 - 50, screen_width - 40)
            # Ekrandaki değişiklikleri günceller.
            pygame.display.flip()

            # Oyuncunun yapacağı seçim ilk başta none olarak ayarlanır.
            oyuncu_secimi = None
            while oyuncu_secimi not in seçenekler: # Oyuncu geçerli bir seçenek seçene kadar döngü çalışmaya devam eder.
                # Pygameden gelen olayları dinler.
                for event in pygame.event.get():
                    # Oyun kapatılmak istenirse oyun kapatılır.
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    # q'ya basarsa oyun kapanır.
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()
                        # taş, kağıt, makastan herhangi birini yazarsa oyuncu_seciminie o değer atanır.
                        if event.key == pygame.K_1:
                            oyuncu_secimi = "taş"
                        elif event.key == pygame.K_2:
                            oyuncu_secimi = "kağıt"
                        elif event.key == pygame.K_3:
                            oyuncu_secimi = "makas"

            bilgisayar_secimi = random.choice(seçenekler) # Bİlgisayardan rastgele bir seçim bilgisayar_secim'e atanır.
            mesaj = "" # verilecek mesaj başta boş olarak belirlenir.

            # eğer ki oyuncu ve bilgisayart seçimleri aynıysa beraberlik olur ve kimse sayı kazanmaz. Beraberlik mesajı ekrana çizilir.
            if oyuncu_secimi == bilgisayar_secimi: 
                mesaj = random.choice(beraberlik_mesaji)
            # Eğer ki oyuncu seçiminin bilgisayar seçimini yendiği koşullarda oyuncuya bir sayı yazılır ve ekrana oyuncu galibiyet mesajı çizilir.
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş"):
                mesaj = random.choice(oyuncu_galibiyet_mesaji)
                oyuncu_galibiyeti += 1
            # Eğer ki bilgisayar seçiminin oyuncu seçimini yendiği koşullarda ise bilgisayara bir sayı yazılır ve ekrana bilgisayar galibiyet mesajı çizdirilir.
            else:
                mesaj = random.choice(bilgisayar_galibiyet_mesaji)
                bilgisayar_galibiyeti += 1

            
            screen.fill(DARK_BLUE) # Ekran belirlenen renk ile doldurulur.
            # Oyuncu seçimi, bilgisayar seçimi, skor ve galibiyet mesajları ekrana çizilir.
            draw_text(f'Kahraman: {oyuncu_secimi.capitalize()}\nKaranlık Lord: {bilgisayar_secimi.capitalize()}\nSkor: Kahraman {oyuncu_galibiyeti} - {bilgisayar_galibiyeti} Karanlık Lord\n', font, GREY, screen, screen_width // 2, screen_height // 2 - 50, screen_width - 40)
            draw_text(f'{mesaj}', font, DARK_YELLOW, screen, screen_width // 2, screen_height // 2 + 50, screen_width - 40)
            pygame.display.flip() # Ekrandaki değişiklikleri günceller.
            pygame.time.wait(4000) # 2 saniye boyunca ekranı bu şekilde tutar.

        screen.fill(DARK_BLUE) # Ekran belirlenen renk ile doldurulur.
        # Eğer ki oyuncu galibiyeti 2 olursa oyuncu kazanır.Bilgisayarın galibiyeti 2 olursa bilgisayar kazanır.
        if oyuncu_galibiyeti == 2:
            draw_text("Tebrikler! Kehaneti gerçekleştirdiniz ve karanlık lordu yendiniz!", font, DARK_GREEN, screen, screen_width // 2, screen_height // 2 - 50, screen_width - 40)
        else:
            draw_text("Maalesef, karanlık lord sizi yendi.", font, DARK_RED, screen, screen_width // 2, screen_height // 2 - 50, screen_width - 40)
        # Oyunu devam ettirmeyi isteyip istemeidğini sorar.
        draw_text("Tekrar oynamak ister misiniz? (e/h)", font, GREY, screen, screen_width // 2, screen_height // 2, screen_width - 40)
        pygame.display.flip()
        pygame.time.wait(3000)
        
        # Oyuncu devam etmek istiyorsa e, devam etmek istmeiyorsa h tuşuna basar.
        devam_oyuncu = None
        while devam_oyuncu not in ['e', 'h']:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_e:
                        devam_oyuncu = 'e'
                    elif event.key == pygame.K_h:
                        devam_oyuncu = 'h'

        # Oyuncu h'ye bastığında ekranda belirlenen mesaj gösterilir. 2saniye bekledikten sonra program sona erer.
        screen.fill(DARK_BLUE)
        if devam_oyuncu == 'h':
            draw_text("Savaş sona erdi. Güle güle, kahraman!", font, GREY, screen, screen_width // 2, screen_height // 2 + 50, screen_width - 40)
            pygame.display.flip()
            pygame.time.wait(3000)
            break

# Dosya direkt olarak çalıştırıldıysa tas_kagit_makas_GULSAH_BASKURT() fonksiyonunun çağrılmasını sağlar.
if __name__ == "__main__":
    tas_kagit_makas_GULSAH_BASKURT()
