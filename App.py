from settings import *
from tetris import Tetris, Text
import sys
import pathlib
import button
from main import *


class App:
    def __init__(self, menu):
        self.menu = menu
        # pg.init()
        pg.display.set_caption('Xếp Hình')
        self.screen = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.set_timer()
        self.images = self.load_images()
        self.tetris = Tetris(self)
        self.text = Text(self)
        self.font = pg.font.SysFont("arialblack", 40)
        self.back_ground_image = pg.image.load("back ground/new_back_ground2.jpg").convert_alpha()
        restart_button = pg.image.load("back ground/restart2.png").convert_alpha()
        self.restart_button = button.Button(240, 500, restart_button, 0.7)
        self.game_over = False
        main_menu_button = pg.image.load("back ground/menu.png").convert_alpha()
        self.main_menu_button = button.Button(170, 350, main_menu_button, 0.8)
        # self.game_over_pressed = False

    def load_images(self):
        files = [item for item in pathlib.Path(SPRITE_DIR_PATH).rglob('*.png') if item.is_file()]
        images = [pg.image.load(file).convert_alpha() for file in files]
        images = [pg.transform.scale(image, (TILE_SIZE, TILE_SIZE)) for image in images]
        return images

    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.fast_user_event = pg.USEREVENT + 1
        self.anim_trigger = False
        self.fast_anim_trigger = False
        pg.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)
        pg.time.set_timer(self.fast_user_event, FAST_ANIM_TIME_INTERVAL)

    def update(self):
        if self.game_over:
            pass
        else:
            self.tetris.update()
            self.clock.tick(FPS)

    def draw(self):
        # self.screen.fill(color=BG_COLOR)
        # self.screen.fill(color=FIELD_COLOR, rect=(0, 0, *FIELD_RES))
        self.screen.blit(self.back_ground_image, (0, 0))
        self.text.draw()
        if self.game_over:
            # self.screen.fill(color=FIELD_COLOR)
            # self.screen.blit(self.back_ground_image, (0, 0))
            self.draw_text("Game Over", self.font, TEXT_COL, 175, 100)
            if self.restart_button.draw(self.screen):
                self.__init__(self.menu)
            if self.main_menu_button.draw(self.screen):
                self.menu.run()
        self.tetris.draw()
        pg.display.flip()

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def check_events(self):
        self.anim_trigger = False
        self.fast_anim_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.tetris.control(pressed_key=event.key)
            elif event.type == self.user_event:
                self.anim_trigger = True
            elif event.type == self.fast_user_event:
                self.fast_anim_trigger = True

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
