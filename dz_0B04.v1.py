from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом")

class Bow(Weapon):
    def attack(self):
        print("Боец делает выстрел из лука")

class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon
        self.choose_weapon(weapon)

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        self.choose_weapon(weapon)

    def choose_weapon(self, weapon: Weapon):
        if isinstance(weapon, Sword):
            print("Боец выбирает меч.")
        elif isinstance(weapon, Bow):
            print("Боец выбирает лук.")

    def hit(self):
        self.weapon.attack()
        print("Монстр побежден!")

class Monster:
    pass

sword1 = Sword()
bow1 = Bow()

fighter1 = Fighter(sword1)
fighter1.hit()
fighter1.change_weapon(bow1)
fighter1.hit()