# shop.py
import pygame
from buildings import Building
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE


class ShopItem:
    def __init__(self, building_prototype, position, size):
        """
        Initialize a ShopItem object.

        Args:
            building_prototype (Building): The prototype of the building.
            position (tuple): The position of the item's top-left corner.
            size (tuple): The size of the item.

        Attributes:
            building_prototype (Building): The prototype of the building.
            rect (pygame.Rect): The rectangular area occupied by the item.
        """
        self.building_prototype = building_prototype
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])

    def draw(self, screen):
        """
        Draw the item on the screen.

        Args:
            screen (pygame.Surface): The surface to draw on.
        """
        pygame.draw.rect(screen, self.building_prototype.color, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 1)  # 白色边框


class Shop:
    def __init__(self, items, position=(0, 0), item_size=(60, 60)):
        """
        Initialize a Shop object.

        Args:
            items (list): A list of ShopItem objects.
            position (tuple, optional): The position of the shop's top-left corner. Defaults to (0, 0).
            item_size (tuple, optional): The size of each item. Defaults to (60, 60).

        Attributes:
            items (list): A list of ShopItem objects.
            item_size (tuple): The size of each item.
            position (tuple): The position of the shop's top-left corner.
        """
        self.items = items
        self.item_size = item_size
        self.position = position
        # Update the position of each item
        for index, item in enumerate(self.items):
            new_x = self.position[0] + (index % 2) * self.item_size[0]
            new_y = self.position[1] + (index // 2) * self.item_size[1]
            item.rect = pygame.Rect(new_x, new_y, self.item_size[0], self.item_size[1])

    def draw(self, screen):
        """
        Draw the shop on the screen.

        Args:
            screen (pygame.Surface): The surface to draw on.
        """
        for item in self.items:
            item.draw(screen)

    def get_item_under_mouse(self, mouse_pos):
        """
        Get the item under the mouse cursor.

        Args:
            mouse_pos (tuple): The position of the mouse cursor.

        Returns:
            ShopItem or None: The item under the mouse cursor, or None if no item is found.
        """
        for item in self.items:
            if item.rect.collidepoint(mouse_pos):
                return item
        return None
