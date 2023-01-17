import pygame
from pygame.locals import *

clock = pygame.time.Clock()
fps = 60

screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space INvaders')

#load img
bg = pygame.image.load("img/bg.jpg")
def draw_bg():
    screen.blit(bg, (0, 0))


# create spaceship class
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/ship1.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
# create sprite groups
spaceship_group =  pygame.sprite.Group()

#create player
spaceship = Spaceship(int(screen_width / 2), screen_height - 100)
spaceship_group.add(spaceship)
run = True
while run:
    clock.tick(fps)

    #draw background
    draw_bg()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update sprite groups
    spaceship_group.draw(screen)

    pygame.display.update()
pygame.quit()
