# buildings.py
# 定义建筑的类
import pygame
from settings import GRID_SIZE


class Building:
    def __init__(self, grid_x, grid_y, grid_w, grid_h, color):
        """
        建筑类的构造函数

        Args:
            grid_x (int): 建筑左上角在网格中的x坐标
            grid_y (int): 建筑左上角在网格中的y坐标
            grid_w (int): 建筑在网格中的宽度
            grid_h (int): 建筑在网格中的高度
            color (tuple): 建筑的颜色，使用RGB元组表示

        Returns:
            None
        """
        self.rect = pygame.Rect(
            grid_x * GRID_SIZE,
            grid_y * GRID_SIZE,
            grid_w * GRID_SIZE,
            grid_h * GRID_SIZE,
        )
        self.color = color

    def draw(self, screen):
        """
        在屏幕上绘制建筑

        Args:
            screen (pygame.Surface): 要绘制建筑的屏幕表面

        Returns:
            None
        """
        pygame.draw.rect(
            screen,
            self.color,
            (
                self.x * GRID_SIZE,
                self.y * GRID_SIZE,
                self.width * GRID_SIZE,
                self.height * GRID_SIZE,
            ),
        )
