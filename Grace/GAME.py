import pygame
import sys

# 初始化pygame
pygame.init()

# 设置窗口大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置窗口标题
pygame.display.set_caption("部落冲突风格游戏")

# 网格大小
grid_size = 20
grid_width = screen_width // grid_size
grid_height = screen_height // grid_size


class Building:
    def __init__(self, grid_x, grid_y, grid_w, grid_h, color):
        self.rect = pygame.Rect(
            grid_x * grid_size,
            grid_y * grid_size,
            grid_w * grid_size,
            grid_h * grid_size,
        )
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


def draw_grid():
    for x in range(0, screen_width, grid_size):
        pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, screen_height))
    for y in range(0, screen_height, grid_size):
        pygame.draw.line(screen, (50, 50, 50), (0, y), (screen_width, y))


# 创建一些建筑
buildings = [
    Building(5, 5, 3, 3, (180, 140, 100)),  # 3x3 建筑
    Building(10, 10, 2, 3, (140, 180, 100)),  # 2x3 建筑
]

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")  # 深绿色背景

    # 绘制网格
    draw_grid()

    # 绘制建筑
    for building in buildings:
        building.draw(screen)

    pygame.display.flip()

# 退出pygame
pygame.quit()
sys.exit()
