import button
from settings import *
from tetris import Tetris, Text
import sys
import pathlib
from App import *


class menu:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Xếp Hình')
        self.screen = pg.display.set_mode(WIN_RES)
        self.font = pg.font.SysFont("arialblack", 40)
        singleplayer_image = pg.image.load("button/singleplayer.png").convert_alpha()
        quit_image = pg.image.load("button/quit.png").convert_alpha()
        multiplayer_image = pg.image.load("button/multiplayer.png").convert_alpha()
        self.back_ground_image = pg.image.load("back ground/new_back_ground.png").convert_alpha()
        self.singleplayer_button = button.Button(37, 200, singleplayer_image, 1)
        self.multiplayer_button = button.Button(37, 300, multiplayer_image, 1)
        self.quit_button = button.Button(170, 400, quit_image, 1)

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def run(self):
        run = True
        while run:
            self.screen.fill((52, 78, 91))
            self.screen.blit(self.back_ground_image, (0, 0))
            if self.singleplayer_button.draw(self.screen):
                app = App(self)
                app.run()
            if self.quit_button.draw(self.screen):
                run = False
            if self.multiplayer_button.draw(self.screen):
                pass
            # self.draw_text("Day la GAME xep hinh", self.font, TEXT_COL, 160, 250)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    # pygame.quit()
                    # sys.exit()
                    run = False

            pg.display.update()
        pg.quit()


if __name__ == '__main__':
    game = menu()
    game.run()
    # app = App()
    # app.run()
