import pygame
from Source import constants as C

pygame.font.init()


class Info:
    def __init__(self, state):
        self.state = state
        self.create_state_labels()
        self.create_info_labels()

    def create_state_labels(self):
        self.state_labels = [self.create_label(state) for state in C.GAME_STATES]
        self.state_positions = [position for position in C.STATES_POSITIONS]

    def create_info_labels(self):
        self.info_labels = [self.create_label(state) for state in C.INFO_LABELS]
        self.info_positions = [position for position in C.INFO_POSITIONS]

    def create_label(self, label, size=(20, 20), width_scale=1.25, height_scale=1):
        size = int(size[0] * width_scale * height_scale)
        font = pygame.font.Font(C.FONT, size)
        label_image = font.render(label, 1, (255, 255, 255))
        return label_image

    def update(self): ...

    def draw(self, surface):
        for label, position in zip(self.state_labels, self.state_positions):
            surface.blit(label, position)
        for info_label, info_position in zip(self.info_labels, self.info_positions):
            surface.blit(info_label, info_position)
