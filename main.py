import pygame

width=300
height=300

screen=pygame.display.set_mode((width, height))

tower=pygame.image.load("tower.png")
towerRect=tower.get_rect()

smallEnemy=pygame.image.load("small enemy.png")
smallEnemyRect=smallEnemy.get_rect()

soldier=pygame.image.load("soldier.png")
soldierRect=soldier.get_rect()

while True:
    screen.fill((255,255,255))
    screen.blit(tower, towerRect)
    screen.blit(smallEnemy, smallEnemyRect)
    screen.blit(soldier, soldierRect)
    pygame.display.flip()