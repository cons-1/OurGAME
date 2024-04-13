# 游戏主要入口

from Source import tools

from Source.states import main_menu


def main():
    game = tools.Game()
    state = main_menu.MainMenu()
    game.run(state)


if __name__ == "__main__":
    main()
