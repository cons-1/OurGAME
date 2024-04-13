import time


class Building:
    def __init__(self, name, size, build_time, level=1):
        self.name = name
        self.size = size
        self.build_time = build_time
        self.level = level

    def upgrade(self):
        self.level += 1
        self.build_time *= 1.5  # 假设每次升级建筑时间增加50%

    def __str__(self):
        return f"{self.name} (Level {self.level})"


# 示例
b = Building("Town Hall", (4, 4), 60)
print(b)
b.upgrade()
print(b)


class Game:
    def __init__(self):
        self.buildings = []
        self.current_time = 0

    def add_building(self, building):
        self.buildings.append(building)
        print(
            f"Started building {building.name}, will take {building.build_time} seconds to build."
        )

    def show_buildings(self):
        for b in self.buildings:
            print(b)

    def advance_time(self, seconds):
        self.current_time += seconds
        print(
            f"Advanced time by {seconds} seconds, current time is {self.current_time} seconds."
        )


# 示例
game = Game()
game.add_building(Building("Barracks", (3, 3), 30))
game.advance_time(30)
game.show_buildings()
