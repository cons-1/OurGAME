import pygame
from Source import tools
from Source import setup
from Source import constants as C
from Source.components import info


class MainMenu:
    def __init__(self):
        self.setup_background()
        self.setup_player()
        self.setup_cursor()
        self.info = info.Info("main_menu")

    def setup_background(self):
        self.background = setup.GRAPHICS["bg"]
        self.background_rect = self.background.get_rect()
        self.background = pygame.transform.scale(
            self.background,
            (
                int(self.background_rect.width * C.BG_MULTI),
                int(self.background_rect.height * C.BG_MULTI),
            ),
        )
        self.viewport = setup.SCREEN.get_rect()
        self.caption = tools.get_image(
            setup.GRAPHICS["pic"], 400, 400, 45, 45, "white", C.BG_MULTI
        )

    def setup_player(self):
        self.player = tools.get_image(
            setup.GRAPHICS["pic"], 120, 120, 45, 45, "white", C.BG_MULTI
        )

    def setup_cursor(self):
        self.cursor = tools.get_image(
            setup.GRAPHICS["pic"], 80, 80, 30, 30, "white", C.BG_MULTI
        )

    def update(self, surface):
        surface.blit(self.background, self.viewport)
        surface.blit(self.caption, (C.SCREEN_WIDTH // 2 - 22, 50))
        surface.blit(self.player, (C.SCREEN_WIDTH // 2 - 22, 200))
        surface.blit(self.cursor, (C.SCREEN_WIDTH // 2 - 60, 300))

        self.info.update()
        self.info.draw(surface)
