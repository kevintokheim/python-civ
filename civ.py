import pygame, sys
from pygame.locals import *
from grid import *
from unit import *
from city import *
from constants import *
import random
import math


warrior = CombatUnit(10, "Warrior", "Sparta", 5, WHITE, (400, 500))
barbarian = CombatUnit(10, "Warrior", "Barbarian", 5, RED, (200, 300))
# worker = Unit(5, "Worker", "Sparta")
enemies = pygame.sprite.Group()
enemies.add(barbarian)
all_sprites = pygame.sprite.Group()
all_sprites.add(warrior, barbarian)


pygame.init()
pygame.display.set_caption('CITY STATE')

GAME_OVER = False
#GAME LOOP
while not GAME_OVER:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                GAME_OVER = True
                sys.exit()
        elif event.type == QUIT:
            GAME_OVER = True
            sys.exit()

        if pygame.sprite.spritecollideany(warrior, enemies):
            print('hello')
            warrior.attack(barbarian)

        #Gets position of clicked location and moves the character to that position
        if event.type == pygame.MOUSEBUTTONDOWN:
            warrior.set_target(pygame.mouse.get_pos())

    #updates warrior movement
    warrior.update()

    """
    RENDERING GRID, SPRITES, AND VIEWS
    """
    #RENDER GAME GRID
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURFACE.blit(TEXTURES[GRID[row][column]], (column*TILESIZE, row*TILESIZE))

    # RENDER TREES
    for tree in sorted(trees, key=lambda t: t.Y_POS):
        DISPLAYSURFACE.blit(tree.SPRITE, (tree.X_POS, tree.Y_POS))

    DISPLAYSURFACE.blit(warrior.surf, warrior.rect)
    DISPLAYSURFACE.blit(barbarian.surf, barbarian.rect)

    pygame.display.update()
    
# warrior.attack(barbarian)
