import pygame
from pygame.locals import *
from pygame.math import Vector2
from constants import *
from queue import PriorityQueue
import math

class Unit(pygame.sprite.Sprite):
    def __init__(self, hp, unit_type, city_id, pos):
        super(Unit, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.rect = self.surf.get_rect(topleft=(100, 300))
        self.hp = hp
        self.unit_type = unit_type
        self.color = WHITE
        self.city_id = city_id
        self.pos = pygame.Vector2(0, 0)
        self.set_target((0, 0))

    def get_hp(self):
        return self.hp

    def set_hp(self):
        self.hp = 100
        return self.hp

    def get_city(self):
        return self.city_id

    #set target for mouse click
    def set_target(self, pos):
        self.target = pygame.Vector2(pos)
    
    #movement update function
    #moves character to a target position. 
    #I plan on updating this with an A* pathfinding algorithm for NPCs
    def update(self):
        move = self.target - self.pos
        move_length = move.length()

        if move_length != 0:
            move.normalize_ip()
            self.pos += move

        self.rect.topleft = list(int(v) for v in self.pos)

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
    def __init__(self, hp, cmbt_unit_type, city_id, ap, color, pos):
        super().__init__(hp, cmbt_unit_type, city_id, pos)
        self.ap = ap
        self.surf.fill(color)

    def get_ap(self):
        return self.ap

    def attack(self, target):
        target.hp -= self.ap
        return target.hp

# u = Unit("10", "Warrior", "Athens")
# barbarian = CombatUnit(8, "Warrior", "Barbarian", 4)
# warrior.attack(barbarian)
# print(f"Barbarian health after attack: {barbarian.hp}")

