import abc
import random


class change_damage:
    def change_damage_for_warrior(weapon) -> int:
        crit = random.choice([0, 0, 0, 0, 0, 0, 0, 0, 1, 1])
        if crit:
            if weapon == 'меч':
                return random.randint(75, 100)
            elif weapon == 'копьё':
                return random.randint(90, 120)
        else:
            if weapon == 'меч':
                return random.randint(60, 85)
            elif weapon == 'копьё':
                return random.randint(80, 100)


class Player(abc.ABC):
    def attack():
        pass


class Warrior(Player):
    health = 1250
    def __init__(self, weapon: str) -> None:
        super().__init__()
        self.weapon = weapon.lower()
    
