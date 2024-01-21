#colocar audio
import pygame
pygame.init()
pygame.mixer.music.load('m.mp3')
pygame.mixer.music.play()
pygame.event.wait()
