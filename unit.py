import pygame
from civ import pressed_keys


class Unit(pygame.sprite.Sprite):
    def __init__(self, hp, unit_type, city_id):
        super(Unit, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        # mp, active, current_action, turn_over, location,
        self.hp = hp
        self.unit_type = unit_type
        # self.mp = mp
        # self.active = active
        # self.current_action = current_action
        # self.turn_over = turn_over
        # self.location = location
        self.city_id = city_id

    def get_hp(self):
        return self.hp

    def set_hp(self):
        self.hp = 100
        return self.hp

    def get_city(self):
        print(self.city_id)
        return self.city_id

    
class CombatUnit(Unit):
    def __init__(self, hp, unit_type, city_id, ap):
        super().__init__(hp, unit_type, city_id)
        self.ap = ap

    def get_ap(self):
        print(self.ap)
        return self.ap

    def attack(self, target):
        target.hp -= self.ap
        print(target.hp)
        print(self.ap)
        print("Hello?")
        return target.hp

class City:
    def __init__(self, name, population, id):
        self.name = name
        self.population = population
        self.id = id
    
    def get_name(self):
        print(self.name)
        return self.name

    def get_population(self):
        print(self.population)
        return self.population
    
    def add_to_population(self):
        self.population += 1
        print(self.population)
        return self.population

    def get_id(self):
        print(self.id)
        return self.id
    

# u = Unit("10", "Warrior", "Athens")
warrior = CombatUnit(10, "Warrior", "Sparta", 5)
barbarian = CombatUnit(8, "Warrior", "Barbarian", 4)
warrior.attack(barbarian)
print(f"Barbarian health after attack: {barbarian.hp}")

