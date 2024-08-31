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

