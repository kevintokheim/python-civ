import pygame, sys
from pygame.locals import *
from grid import *
from unit import *
import random
import math

c = CombatUnit("10", "Warrior", "Sparta", "5")

GAME_OVER = False
#GAME LOOP
while not GAME_OVER:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    print(c.get_ap())

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
    pygame.display.update()
