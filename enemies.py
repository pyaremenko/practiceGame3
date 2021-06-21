import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class Ellipse(pygame.sprite.Sprite):
    def __init__(self, x, y, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class Slime4(pygame.sprite.Sprite):
    def __init__(self, x, y, change_x, change_y):
        pygame.sprite.Sprite.__init__(self)
        self.change_x = change_x
        self.change_y = change_y
        self.image = pygame.image.load("images/slime4.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, horizontal_blocks, vertical_blocks):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
        elif self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0

        if self.rect.topleft in self.get_intersection_position():
            direction = random.choice(("left", "right", "up", "down"))
            if direction == "left" and self.change_x == 0:
                self.change_x = -2
                self.change_y = 0
            elif direction == "right" and self.change_x == 0:
                self.change_x = 2
                self.change_y = 0
            elif direction == "up" and self.change_y == 0:
                self.change_x = 0
                self.change_y = -2
            elif direction == "down" and self.change_y == 0:
                self.change_x = 0
                self.change_y = 2

    def get_intersection_position(self):
        items = []
        for i, row in enumerate(enviroment()):
            for j, item in enumerate(row):
                if item == 3:
                    items.append((j * 32, i * 32))

        return items


class Slime3(pygame.sprite.Sprite):
    def __init__(self, x, y, change_x, change_y):
        pygame.sprite.Sprite.__init__(self)
        self.change_x = change_x
        self.change_y = change_y
        self.image = pygame.image.load("images/slime3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, horizontal_blocks, vertical_blocks):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
        elif self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0

        if self.rect.topleft in self.get_intersection_position():
            direction = random.choice(("left", "right", "up", "down"))
            if direction == "left" and self.change_x == 0:
                self.change_x = -2
                self.change_y = 0
            elif direction == "right" and self.change_x == 0:
                self.change_x = 2
                self.change_y = 0
            elif direction == "up" and self.change_y == 0:
                self.change_x = 0
                self.change_y = -2
            elif direction == "down" and self.change_y == 0:
                self.change_x = 0
                self.change_y = 2

    def get_intersection_position(self):
        items = []
        for i, row in enumerate(enviroment()):
            for j, item in enumerate(row):
                if item == 3:
                    items.append((j * 32, i * 32))

        return items


class Slime2(pygame.sprite.Sprite):
    def __init__(self, x, y, change_x, change_y):
        pygame.sprite.Sprite.__init__(self)
        self.change_x = change_x
        self.change_y = change_y
        self.image = pygame.image.load("images/slime2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, horizontal_blocks, vertical_blocks):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
        elif self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0

        if self.rect.topleft in self.get_intersection_position():
            direction = random.choice(("left", "right", "up", "down"))
            if direction == "left" and self.change_x == 0:
                self.change_x = -2
                self.change_y = 0
            elif direction == "right" and self.change_x == 0:
                self.change_x = 2
                self.change_y = 0
            elif direction == "up" and self.change_y == 0:
                self.change_x = 0
                self.change_y = -2
            elif direction == "down" and self.change_y == 0:
                self.change_x = 0
                self.change_y = 2

    def get_intersection_position(self):
        items = []
        for i, row in enumerate(enviroment()):
            for j, item in enumerate(row):
                if item == 3:
                    items.append((j * 32, i * 32))

        return items


class Slime1(pygame.sprite.Sprite):
    def __init__(self, x, y, change_x, change_y):
        pygame.sprite.Sprite.__init__(self)
        self.change_x = change_x
        self.change_y = change_y
        self.image = pygame.image.load("images/slime1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, horizontal_blocks, vertical_blocks):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
        elif self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0

        if self.rect.topleft in self.get_intersection_position():
            direction = random.choice(("left", "right", "up", "down"))
            if direction == "left" and self.change_x == 0:
                self.change_x = -2
                self.change_y = 0
            elif direction == "right" and self.change_x == 0:
                self.change_x = 2
                self.change_y = 0
            elif direction == "up" and self.change_y == 0:
                self.change_x = 0
                self.change_y = -2
            elif direction == "down" and self.change_y == 0:
                self.change_x = 0
                self.change_y = 2

    def get_intersection_position(self):
        items = []
        for i, row in enumerate(enviroment()):
            for j, item in enumerate(row):
                if item == 3:
                    items.append((j * 32, i * 32))

        return items


class Slime(pygame.sprite.Sprite):
    def __init__(self, x, y, change_x, change_y):
        pygame.sprite.Sprite.__init__(self)
        self.change_x = change_x
        self.change_y = change_y
        self.image = pygame.image.load("images/slime.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, horizontal_blocks, vertical_blocks):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
        elif self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0

        if self.rect.topleft in self.get_intersection_position():
            direction = random.choice(("left", "right", "up", "down"))
            if direction == "left" and self.change_x == 0:
                self.change_x = -2
                self.change_y = 0
            elif direction == "right" and self.change_x == 0:
                self.change_x = 2
                self.change_y = 0
            elif direction == "up" and self.change_y == 0:
                self.change_x = 0
                self.change_y = -2
            elif direction == "down" and self.change_y == 0:
                self.change_x = 0
                self.change_y = 2

    def get_intersection_position(self):
        items = []
        for i, row in enumerate(enviroment()):
            for j, item in enumerate(row):
                if item == 3:
                    items.append((j * 32, i * 32))

        return items


def enviroment():  # 23x18
    grid = ((10, 2, 11, 11, 2, 11, 11, 11, 11, 2, 11, 11, 11, 2, 11, 11, 11, 11, 11, 11, 11, 2, 11, 11, 9),
            (8, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 7),
            (1, 3, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1),
            (8, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 7),
            (1, 3, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1),
            (8, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 7),
            (8, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 7),
            (1, 3, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1),
            (8, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 4, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 7),
            (1, 3, 1, 1, 3, 1, 1, 1, 1, 3, 1, 3, 1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1),
            (8, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 7),
            (1, 3, 1, 1, 3, 1, 1, 1, 1, 3, 1, 3, 1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1),
            (8, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 7),
            (8, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 7),
            (1, 3, 1, 1, 3, 1, 1, 1, 1, 3, 1, 3, 1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1),
            (4, 2, 5, 5, 2, 5, 5, 5, 5, 2, 5, 4, 5, 2, 5, 5, 5, 5, 5, 5, 5, 2, 5, 5, 6))

    return grid


def draw_enviroment(screen):
    for i, row in enumerate(enviroment()):
        for j, item in enumerate(row):
            if item == 1:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32 + 32, i * 32], 3)  # гор-верх
                pygame.draw.line(screen, BLUE, [j * 32, i * 32 + 32], [j * 32 + 32, i * 32 + 32], 3)  # гор-низ
            elif item == 2:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32, i * 32 + 32], 3)  # ver-liv
                pygame.draw.line(screen, BLUE, [j * 32 + 32, i * 32], [j * 32 + 32, i * 32 + 32], 3)  # ver-prav
            elif item == 4:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32 + 32, i * 32], 3)  # гор-верх
                pygame.draw.line(screen, BLUE, [j * 32, i * 32 + 32], [j * 32 + 32, i * 32 + 32], 3)  # гор-низ
            elif item == 5:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32 + 32], [j * 32 + 32, i * 32 + 32], 3)  # гор-низ
            elif item == 6:
                pygame.draw.line(screen, BLUE, [j * 32 + 32, i * 32], [j * 32 + 32, i * 32 + 32], 3)  # ver-prav
                pygame.draw.line(screen, BLUE, [j * 32, i * 32 + 32], [j * 32 + 32, i * 32 + 32], 3)  # гор-низ

            elif item == 8:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32, i * 32 + 32], 3)  # ver-liv
            elif item == 9:
                pygame.draw.line(screen, BLUE, [j * 32 + 32, i * 32], [j * 32 + 32, i * 32 + 32], 3)  # ver-prav
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32 + 32, i * 32], 3)  # гор-верх
            elif item == 10:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32, i * 32 + 32], 3)  # ver-liv
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32 + 32, i * 32], 3)  # гор-верх
            elif item == 11:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32 + 32, i * 32], 3)  # гор-верх
            elif item == 12:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32 + 32, i * 32], 3)  # гор-верх
                pygame.draw.line(screen, BLUE, [j * 32, i * 32 + 32], [j * 32 + 32, i * 32 + 32], 3)  # гор-низ
            elif item == 13:
                pygame.draw.line(screen, BLUE, [j * 32 + 32, i * 32], [j * 32 + 32, i * 32 + 32], 3)  # ver-prav
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32 + 32, i * 32], 3)  # гор-верх
                pygame.draw.line(screen, BLUE, [j * 32, i * 32 + 32], [j * 32 + 32, i * 32 + 32], 3)  # гор-низ
            elif item == 20:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32, i * 32 + 32], 3)  # ver-liv
                pygame.draw.line(screen, BLUE, [j * 32 + 32, i * 32], [j * 32 + 32, i * 32 + 32], 3)  # ver-prav
