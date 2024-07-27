import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        print(f"{self.name} атаковал {other.name} на {damage} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Игра началась!")
        print(f"{self.player.name} vs {self.computer.name}")

        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            if self.computer.is_alive():
                self.computer.attack(self.player)

            print(f"{self.player.name} здоровье: {self.player.health}")
            print(f"{self.computer.name} здоровье: {self.computer.health}")
            print("-" * 20)

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


# Пример использования
player = Hero(name="Игрок")
computer = Hero(name="Компьютер")
game = Game(player, computer)
game.start()