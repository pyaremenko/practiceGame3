from player import Player

from enemies import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

ES = 4
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


class Game1(object):
    def __init__(self):
        self.font = pygame.font.Font("font/Pokemon GB.ttf", 33)
        self.font2 = pygame.font.Font("font/Pokemon GB.ttf", 20)
        self.about = False
        self.game_over = True
        self.score = 0
        self.lives = 0
        self.font = pygame.font.Font("font/Pokemon GB.ttf", 25)
        self.menu = Menu(("Start", "Score Table", "Exit"), font_color=WHITE, font_size=40)
        self.player = Player(32, 128, "images/player.png")
        self.horizontal_blocks = pygame.sprite.Group()
        self.vertical_blocks = pygame.sprite.Group()
        self.vertical_blocks = pygame.sprite.Group()
        self.dots_group = pygame.sprite.Group()

        for i, row in enumerate(enviroment()):
            for j, item in enumerate(row):
                if item == 1:
                    self.horizontal_blocks.add(Block(j * 32 + 8, i * 32 + 8, BLACK, 16, 16))
                if item == 2:
                    self.vertical_blocks.add(Block(j * 32 + 8, i * 32 + 8, BLACK, 16, 16))

        self.enemies = pygame.sprite.Group()

        self.enemies.add(Slime(291, 99, 0, ES))
        self.enemies.add(Slime(291, 323, 0, -ES))
        self.enemies.add(Slime(675, 131, 0, ES))
        self.enemies.add(Slime(35, 227, 0, ES))
        self.enemies.add(Slime(163, 67, ES, 0))
        self.enemies.add(Slime(452, 67, -ES, 0))
        self.enemies.add(Slime(547, 451, ES, 0))
        self.enemies.add(Slime(451, 355, ES, 0))
        for i, row in enumerate(enviroment()):
            for j, item in enumerate(row):
                if item == 1:
                    self.dots_group.add(Ellipse(j * 32 + 12, i * 32 + 12, WHITE, 8, 8))
                elif item == 2:
                    self.dots_group.add(Ellipse(j * 32 + 12, i * 32 + 12, WHITE, 8, 8))
                elif item == 3:
                    self.dots_group.add(Ellipse(j * 32 + 12, i * 32 + 12, WHITE, 8, 8))

        print(len(self.dots_group))

        self.pacman_sound = pygame.mixer.Sound("sounds/pacman_sound.ogg")
        self.game_over_sound = pygame.mixer.Sound("sounds/game_over_sound.ogg")
        self.ouch_sound = pygame.mixer.Sound("sounds/ouch_sound.ogg")

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                return True
            self.menu.event_handler(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.game_over and not self.about:
                        if self.menu.state == 0:
                            self.__init__()
                            self.game_over = False
                        elif self.menu.state == 1:
                            self.about = True
                        elif self.menu.state == 2:
                            exit()
                            return True

                elif event.key == pygame.K_RIGHT:
                    self.player.move_right()

                elif event.key == pygame.K_LEFT:
                    self.player.move_left()

                elif event.key == pygame.K_UP:
                    self.player.move_up()

                elif event.key == pygame.K_DOWN:
                    self.player.move_down()

                elif event.key == pygame.K_ESCAPE:
                    self.game_over = True
                    self.about = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.stop_move_right()
                elif event.key == pygame.K_LEFT:
                    self.player.stop_move_left()
                elif event.key == pygame.K_UP:
                    self.player.stop_move_up()
                elif event.key == pygame.K_DOWN:
                    self.player.stop_move_down()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.player.explosion = True

        return False

    def run_logic(self):

        if not self.game_over:
            self.player.update(self.horizontal_blocks, self.vertical_blocks)
            block_hit_list = pygame.sprite.spritecollide(self.player, self.dots_group, True)
            if len(block_hit_list) > 0:
                self.pacman_sound.play()
                self.score += 1

                def func():
                    import main
                    main.main2()

                if self.score == 203:
                    func()

            block_hit_list = pygame.sprite.spritecollide(self.player, self.enemies, True)
            if len(block_hit_list) > 0:
                self.lives += 1
                self.ouch_sound.play()
                if self.lives == 3:
                    self.player.explosion = True

                    self.game_over_sound.play()

            self.game_over = self.player.game_over
            self.enemies.update(self.horizontal_blocks, self.vertical_blocks)
        file_1 = open("files/score.txt", "w")
        file_1.write(str(self.score))
        file_1.close()

    def display_frame(self, screen):

        screen.fill(BLACK)
        if self.game_over:
            if self.about:

                from pathlib import Path
                sc = Path('files/score.txt').read_text()
                hsc = Path('files/highscore.txt').read_text()
                if sc > hsc:
                    hsc = sc
                    file_1 = open("files/highscore.txt", "w")
                    file_1.write(str(hsc))
                    file_1.close()

                self.display_message(screen, 50, "Highest Score: " + str(hsc))

            else:
                self.menu.display_frame(screen)
        else:

            self.horizontal_blocks.draw(screen)
            self.vertical_blocks.draw(screen)
            draw_enviroment(screen)
            self.dots_group.draw(screen)
            self.enemies.draw(screen)
            screen.blit(self.player.image, self.player.rect)
            text = self.font.render("Score: " + str(self.score), True, GREEN)
            screen.blit(text, [20, 530])

            heart3 = pygame.image.load('images/heart.png')

            screen.blit(heart3, (572, 524))

            text = self.font.render(" left: " + str(3 - self.lives), True, WHITE)
            screen.blit(text, [580, 530])

            text2 = self.font.render("Level 1", True, RED)
            screen.blit(text2, [480, 180])

        pygame.display.flip()

    def display_message(self, screen, y, message, color=(255, 0, 0)):
        label = self.font.render(message, True, color)
        width = label.get_width()
        height = label.get_height()
        posX = (SCREEN_WIDTH / 2) - (width / 2)
        posY = (SCREEN_HEIGHT / 2) - (height / 2) - y
        screen.blit(label, (posX, posY))


class Menu(object):
    state = 0

    def __init__(self, items, font_color=(0, 0, 0), select_color=(255, 0, 0), ttf_font="font/Pokemon GB.ttf",
                 font_size=25):
        self.font_color = font_color
        self.select_color = select_color
        self.items = items
        self.font = pygame.font.Font(ttf_font, font_size)

    def display_frame(self, screen):
        for index, item in enumerate(self.items):
            if self.state == index:
                label = self.font.render(item, True, self.select_color)
            else:
                label = self.font.render(item, True, self.font_color)

            width = label.get_width()
            height = label.get_height()

            posX = (SCREEN_WIDTH / 2) - (width / 2)
            t_h = len(self.items) * height
            posY = (SCREEN_HEIGHT / 2) - (t_h / 2) + (index * height)

            screen.blit(label, (posX, posY))

    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.state > 0:
                    self.state -= 1
            elif event.key == pygame.K_DOWN:
                if self.state < len(self.items) - 1:
                    self.state += 1
