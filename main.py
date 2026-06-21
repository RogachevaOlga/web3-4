import random

from battle import Battle
from characters import Mage, Warrior


def main():
    random.seed(42)

    team_a = [Warrior("Артур"), Mage("Мерлин")]
    team_b = [Warrior("Гоблин-вождь"), Mage("Тёмный маг")]

    Battle(team_a, team_b).run()


if __name__ == "__main__":
    main()
