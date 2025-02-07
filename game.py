from abc import ABC, abstractmethod

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self) -> str:
        """Метод для выполнения атаки, возвращает описание атаки."""
        pass

# Конкретные классы оружия
class Sword(Weapon):
    def attack(self) -> str:
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self) -> str:
        return "Боец наносит удар из лука."

class Axe(Weapon):
    def attack(self) -> str:
        return "Боец наносит удар топором."

class Spear(Weapon):
    def attack(self) -> str:
        return "Боец наносит удар копьем."

# Класс для монстра
class Monster:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, damage: int):
        self.health -= damage
        print(f"{self.name} получает {damage} урона. Здоровье: {self.health}.")

# Класс для бойца
class Fighter:
    def __init__(self, name: str):
        self.name = name
        self.weapon: Weapon = None

    def choose_weapon(self, weapon: Weapon):
        if weapon is None:
            raise ValueError("Оружие не может быть None.")
        self.weapon = weapon
        print(f"{self.name} выбирает {self.weapon.__class__.__name__.lower()}.")

    def attack(self) -> str:
        if self.weapon is None:
            return "Боец без оружия."
        return self.weapon.attack()

    def change_weapon(self, new_weapon: Weapon):
        if new_weapon is None:
            raise ValueError("Новое оружие не может быть None.")
        old_weapon = self.weapon.__class__.__name__ if self.weapon else "без оружия"
        self.weapon = new_weapon
        print(f"{self.name} меняет оружие с {old_weapon} на {self.weapon.__class__.__name__.lower()}.")

# Функция для проведения боя
def battle(fighter: Fighter, monster: Monster):
    print("\nНачинается бой!")
    while monster.is_alive():
        action = fighter.attack()
        if action == "Боец без оружия.":
            print(action)
            break
        print(action)
        # Предположим, что каждая атака наносит 10 урона
        monster.take_damage(10)
    if monster.is_alive():
        print("Боец не смог победить монстра.")
    else:
        print(f"{monster.name} побежден!")

# Основная функция для демонстрации
def main():
    # Создание бойца и монстров
    fighter = Fighter("Артур")
    monsters = [
        Monster("Гоблин", 30),
        Monster("Орк", 50),
        Monster("Дракон", 100)
    ]

    # Выбор оружия и бой с каждым монстром
    for monster in monsters:
        # Выбор оружия
        if monster.name == "Гоблин":
            fighter.choose_weapon(Sword())
        elif monster.name == "Орк":
            fighter.change_weapon(Bow())
        elif monster.name == "Дракон":
            fighter.change_weapon(Axe())

        # Бой
        battle(fighter, monster)

if __name__ == "__main__":
    main()