# utilities.py
# 通用函数，例如绘制网格
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE


def draw_grid(screen):
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (0, y), (SCREEN_WIDTH, y))
