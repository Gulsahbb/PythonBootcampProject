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
