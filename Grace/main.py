# main.py
import pygame
import sys
from buildings import Building
from utilities import draw_grid
from shop import Shop, ShopItem
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE
import pygame
import sys
from buildings import Building
from utilities import draw_grid
from shop import Shop, ShopItem
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE


# Define the main function
def main():
    """
    The main function of the game.

    Initializes the game, sets up the screen, creates the shop items,
    handles user input, updates the game state, and renders the game.

    Returns:
        None
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Grace and Liam")

    # Define the shop items
    shop_items = [
        ShopItem(Building(0, 0, 3, 3, (180, 140, 100)), (0, 0), (60, 60)),
        ShopItem(Building(0, 0, 2, 3, (140, 180, 100)), (0, 60), (60, 60)),
    ]
    # Set the position of the shop in the bottom right corner
    shop_x = SCREEN_WIDTH - 2 * 60  # Assuming the shop width is 2 grid cells
    shop_y = (
        SCREEN_HEIGHT - (len(shop_items) // 2) * 60
    )  # Height calculated based on the number of items
    shop = Shop(shop_items, position=(shop_x, shop_y), item_size=(60, 60))
    buildings = []
    selected_item = None

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if selected_item is None:  # 尝试选择一个物品
                    selected_item = shop.get_item_under_mouse(mouse_pos)
                else:
                    # 放置建筑
                    grid_x, grid_y = (
                        mouse_pos[0] // GRID_SIZE,
                        mouse_pos[1] // GRID_SIZE,
                    )
                    new_building = Building(
                        grid_x,
                        grid_y,
                        selected_item.building_prototype.width,
                        selected_item.building_prototype.height,
                        selected_item.building_prototype.color,
                    )
                    buildings.append(new_building)
                    selected_item = None

        screen.fill((0, 100, 0))

        # Draw the grid
        draw_grid(screen)

        # Draw the shop and buildings
        shop.draw(screen)
        for building in buildings:
            building.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
