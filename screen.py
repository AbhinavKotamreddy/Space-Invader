import pygame
from pygame.locals import *

clock = pygame.time.Clock()
fps = 180

screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space INvaders')

#load img
bg = pygame.image.load("img/bg.jpg")
def draw_bg():
    screen.blit(bg, (0, 0))
run = True

while run:
    clock.tick(fps)

    #draw background
    draw_bg()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = false
    pygame.display.update()
pygame.quit()