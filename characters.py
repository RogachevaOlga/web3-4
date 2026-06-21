import random


class Hero:
    """Общая основа для всех героев: имя, здоровье, защита, базовый урон."""

    def __init__(self, name, hp, attack_power, defense):
        self.name = name
        self._max_hp = hp
        self._hp = hp
        self._attack_power = attack_power
        self._defense = defense

    @property
    def hp(self):
        return self._hp

    @property
    def is_alive(self):
        return self._hp > 0

    def take_damage(self, amount):
        damage = max(0, amount - self._defense)
        self._hp = max(0, self._hp - damage)
        return damage

    def attack(self, target):
        raise NotImplementedError(
            f"{type(self).__name__} должен реализовать свой метод attack()"
        )


class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name, hp=120, attack_power=15, defense=10)

    def attack(self, target):
        damage = self._attack_power + random.randint(0, 5)
        dealt = target.take_damage(damage)
        print(f"  {self.name} рубит мечом {target.name} на {dealt} урона")


class Mage(Hero):
    SPELL_COST = 20

    def __init__(self, name):
        super().__init__(name, hp=70, attack_power=8, defense=3)
        self._mana = 100

    def attack(self, target):
        if self._mana >= self.SPELL_COST:
            self._mana -= self.SPELL_COST
            damage = self._attack_power * 2 + random.randint(0, 10)
            dealt = target.take_damage(damage)
            print(f"  {self.name} запускает огненный шар в {target.name} на {dealt} урона")
        else:
            damage = self._attack_power
            dealt = target.take_damage(damage)
            print(f"  {self.name} бьёт посохом {target.name} (без маны), {dealt} урона")
