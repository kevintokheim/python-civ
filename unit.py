import pygame
from pygame.locals import *
from constants import *

class Unit(pygame.sprite.Sprite):
    def __init__(self, hp, unit_type, city_id):
        super(Unit, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.rect = self.surf.get_rect(topleft=(100, 300))
        # mp, active, current_action, turn_over, location,
        self.hp = hp
        # self.sprite
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

    #movement update function
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        #keep the player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > (MAPWIDTH * TILESIZE):
            self.rect.right = (MAPWIDTH * TILESIZE)
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= (MAPHEIGHT * TILESIZE):
            self.rect.bottom = (MAPHEIGHT * TILESIZE)

class CombatUnit(Unit):
    def __init__(self, hp, cmbt_unit_type, city_id, ap, color):
        super().__init__(hp, cmbt_unit_type, city_id)
        self.ap = ap
        self.surf.fill(color)

    def get_ap(self):
        print(self.ap)
        return self.ap

    def attack(self, target):
        target.hp -= self.ap
        print(target.hp)
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
# barbarian = CombatUnit(8, "Warrior", "Barbarian", 4)
# warrior.attack(barbarian)
# print(f"Barbarian health after attack: {barbarian.hp}")

