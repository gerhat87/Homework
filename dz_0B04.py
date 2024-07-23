#Задача: Разработать простую игру, где игрок может использовать различные
#типы оружия для борьбы с монстрами. Программа должна быть спроектирована таким образом,
# чтобы легко можно было добавлять новые типы оружия, не изменяя существующий код бойцов или механизм боя.
#Исходные данные:
#- Есть класс `Fighter`, представляющий бойца.
#- Есть класс `Monster`, представляющий монстра.
#- Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
#Шаг 1:Создайте абстрактный класс для оружия
#- Создайте абстрактный класс `Weapon`, который будет содержать абстрактный метод `attack()`.
#Шаг 2: Реализуйте конкретные типы оружия
#- Создайте несколько классов, унаследованных от `Weapon`, например,
# `Sword` и `Bow`. Каждый из этих классов реализует метод `attack()` своим уникальным способом.


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
        print("Боец делает высрел из лука")

class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon
    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
    def hit(self):
       print(self.weapon.attack())
class Monstr():
    pass

sword1 = Sword()
bow1 = Bow()

fighter1=Fighter(sword1)
fighter1.hit()
fighter1.change_weapon(bow1)
fighter1.hit()







