import random
import time
import traceback

import pygame
from pygame.locals import *
from algo_test import bubble_sort, selection_sort, insertion_sort

SIZE = 600, 800
pygame.init()
pygame.font.init()
pygame.display.set_caption('Sorting Visusalizer')
screen = pygame.display.set_mode(SIZE)
FPS = 10

RED = (255, 0, 0)
GRAY = (150, 150, 150)

font = pygame.font.SysFont('Aerial', 30)
clock = pygame.time.Clock()
running = True
sorting_algo = bubble_sort
stages = []


def draw():
    global current_animation

    if current_animation < len(stages) - 1:
        current_animation += 1
    screen.fill((0, 0, 0))
    for index, x in enumerate(stages[current_animation]):
        bar = Bar(x, index)
        bar.draw()

    pygame.draw.rect(screen, (255, 255, 255),
                     Rect(50, 50, 500, 500), width=3)
    for x in buttons:
        x.draw()
        if x.rect.collidepoint(pygame.mouse.get_pos()):
            x.draw_border()
    slider.draw()
    pygame.display.update()


class Bar:
    def __init__(self, length=random.randint(1, 600), index=random.randint(0, 24)):
        self.length = length
        self.index = index

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0),
                         Rect(50 + (20 * self.index), 50, 20, self.length))
        pygame.draw.rect(screen, (255, 255, 255),
                         Rect(50 + (20 * self.index), 50, 20, self.length), width=2)


class Slider:
    def __init__(self):
        self.x = 60
        self.clicked = False
        self.rect = Rect(self.x, 694, 15, 25)

    def draw(self):
        global FPS
        pygame.draw.rect(screen, (255, 255, 255),
                         Rect(50, 700, 500, 10))
        pygame.draw.rect(screen, (0, 0, 0),
                         Rect(50, 704, 500, 2))
        pygame.draw.rect(screen, (192, 192, 192),
                         Rect(self.x, 694, 15, 25))
        self.rect = Rect(self.x, 694, 15, 25)
        FPS = int(self.x/6)


class Button:
    def __init__(self, x, y, width, height, text, algo):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.textsurface = font.render(text, False, (255, 255, 255))
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.algo = algo

    def draw(self):
        pygame.draw.rect(screen, (10, 10, 10),
                         Rect(self.x, self.y, self.width, self.height))
        screen.blit(self.textsurface, (self.x, self.y + 10))

    def action(self):
        global stages, current_animation
        test_list = [random.randint(1, 500) for x in range(0, 25)]
        stages = self.algo(test_list.copy())
        current_animation = 0

    def draw_border(self):
        pygame.draw.rect(screen, (255, 255, 255),
                         Rect(self.x, self.y, self.width, self.height), width=2)


button1 = Button(50, 600, 150, 40, '     BUBBLE  ', bubble_sort)
button2 = Button(225, 600, 150, 40, '   SELECTION  ', selection_sort)
button3 = Button(400, 600, 150, 40, '   INSERTION  ', insertion_sort)
buttons = [button1, button2, button3]
slider = Slider()
current_animation = 0
button1.action()
while running:
    draw()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for x in buttons:
                if x.rect.collidepoint(pygame.mouse.get_pos()):
                    x.action()
            if slider.rect.collidepoint(pygame.mouse.get_pos()):
                slider.clicked = True
        if slider.clicked:
            x, _ = pygame.mouse.get_pos()
            if x > 550:
                x = 550
            elif x < 50:
                x = 50
            slider.x = x
        if event.type == pygame.MOUSEBUTTONUP and slider.clicked:
            slider.clicked = False

pygame.quit()
