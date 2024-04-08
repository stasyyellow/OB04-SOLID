import random
from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self, fighter_name):
        pass

class Sword(Weapon):
    def __init__(self):
        self.damage = 3

    def attack(self, fighter_name):
        return f"{fighter_name} наносит удар мечом"

class Bow(Weapon):
    def __init__(self):
        self.damage = 1

    def attack(self, fighter_name):
        return f"{fighter_name} стреляет из лука"

class Axe(Weapon):
    def __init__(self):
        self.damage = 4

    def attack(self, fighter_name):
        return f"{fighter_name} атакует топором"

class Dagger(Weapon):
    def __init__(self):
        self.damage = 1

    def attack(self, fighter_name):
        return f"{fighter_name} атакует кинжалом"

class Fighter:
    def __init__(self, name, weapon=None, lives=None):
        self.name = name
        self.weapon = weapon
        self.lives = lives if lives is not None else random.randint(5, 8)

    def changeWeapon(self, weapon):
        self.weapon = weapon

    def takeDamage(self, damage):
        self.lives -= damage
        print(f"{self.name} получает урон в размере {damage}!")
        if self.lives <= 0:
            print(f"{self.name} осталось {self.lives} жизней.")
            print(f"{self.name} погиб!")
        else:
            print(f"{self.name} осталось {self.lives} жизней.")

    def fight(self, opponent):
        if self.weapon:
            print(f"{self.name} выбирает {type(self.weapon).__name__}.") #__name__
            print(f"{self.weapon.attack(self.name)}.") #
            opponent.takeDamage(self.weapon.damage) #opponent
        # else:
        #     print(f"{self.name} не выбрал оружие, нечем сражаться!")

class Monster:
    def __init__(self, name, lives=None):
        self.name = name
        self.lives = lives if lives is not None else random.randint(5, 8)

    def takeDamage(self, damage):
        self.lives -= damage
        print(f"{self.name} получает урон в размере {damage}!")
        if self.lives <= 0:
            print(f"{self.name} осталось {self.lives} жизней.")
            print(f"{self.name} погиб!")
        else:
            print(f"{self.name} осталось {self.lives} жизней.")

sword = Sword()
bow = Bow()
axe = Axe()
dagger = Dagger()

fighter = Fighter("Боец", sword) #fighter = Fighter("Боец", sword)
monster = Monster("Монстр")

# Рандомно определим, кто ходит первым
current_player = random.choice([fighter, monster])
next_player = fighter if current_player == monster else monster

turns = [fighter, monster]

while fighter.lives > 0 and monster.lives > 0:
    if isinstance(current_player, Fighter):
        current_player.fight(next_player)
    else:
        next_player.takeDamage(random.randint(1, 5))
    print()

    # Обновляем оружие для следующего игрока перед его ходом
    next_player.weapon = random.choice([sword, bow, axe, dagger])

    # Поменяем игроков местами для следующего хода
    current_player, next_player = next_player, current_player

print("Бой завершен.")
