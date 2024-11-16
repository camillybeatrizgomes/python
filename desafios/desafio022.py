import pygame
pygame.init()
pygame.mixer.music.load('mp3-chaves.mp3')
print('Tocando: ')
print('Chaves - Se você é jovem ainda')
pygame.mixer.music.play()
input()
pygame.event.wait()

