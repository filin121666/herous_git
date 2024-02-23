import abc
import random


class Change_damage:
    def change_damage_for_warrior(weapon: str) -> int:
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
    
    def change_damage_for_archer(weapon: str) -> int:
        crit = random.choice([0, 0, 0, 0, 0, 0, 0, 0, 1, 1])
        if crit:
            if weapon == 'лук':
                return random.randint(60, 80)
            elif weapon == 'арбалет':
                return random.randint(75, 100)
        else:
            if weapon == 'лук':
                return random.randint(40, 65)
            elif weapon == 'арбалет':
                return random.randint(65, 80)


class Player(abc.ABC):
    def attack():
        pass


class Warrior(Player, Change_damage):
    health = 1250

    def __init__(self, weapon: str) -> None:
        super().__init__()
        self.weapon = weapon.lower()
    
    def attack(self) -> int:
        return Change_damage.change_damage_for_warrior(weapon=self.weapon)


class Archer(Player, Change_damage):
    health = 1000

    def __init__(self, weapon: str) -> None:
        super().__init__()
        self.weapon = weapon

    def attack(self) -> int:
        return Change_damage.change_damage_for_archer(weapon=self.weapon)
    

