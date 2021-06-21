from tkinter import messagebox

import pygame
from level1 import Game1
from level2 import Game2
from level3 import Game3
from level4 import Game4
from level5 import Game5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576


def main1():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PACMAN")
    done = False
    clock = pygame.time.Clock()
    level1 = Game1()
    while not done:
        done = level1.process_events()
        level1.run_logic()
        level1.display_frame(screen)
        clock.tick(30)


def main2():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PACMAN")
    done = False
    clock = pygame.time.Clock()
    level2 = Game2()
    while not done:
        done = level2.process_events()
        level2.run_logic()
        level2.display_frame(screen)
        clock.tick(30)


def main3():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PACMAN")
    done = False
    clock = pygame.time.Clock()

    level3 = Game3()
    while not done:
        done = level3.process_events()
        level3.run_logic()
        level3.display_frame(screen)
        clock.tick(30)


def main4():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PACMAN")
    done = False
    clock = pygame.time.Clock()
    level4 = Game4()
    while not done:
        done = level4.process_events()
        level4.run_logic()
        level4.display_frame(screen)
        clock.tick(30)


def main5():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PACMAN")
    done = False
    clock = pygame.time.Clock()
    level5 = Game5()
    while not done:
        done = level5.process_events()
        level5.run_logic()
        level5.display_frame(screen)
        clock.tick(30)

    pygame.quit()


if __name__ == '__main__':
    main1()
