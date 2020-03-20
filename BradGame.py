import pygame
import sys
from time import sleep

BLACK = (0,0,0)
padWidth = 480
padHeight = 600
rockImage = ['rock01.png', 'rock02.png', 'rock03.png', 'rock04.png', 'rock05.png', 'rock06.png', 'rock07.png', 'rock08.png', 'rock09.png', 'rock10.png', 'rock11.png', 'rock12.png', 'rock13.png', 'rock14.png', 'rock15.png', 'rock16.png', 'rock17.png', 'rock18.png', 'rock19.png', 'rock20.png', 'rock21.png', 'rock22.png', 'rock23.png', 'rock24.png', 'rock25.png', 'rock26.png', 'rock27.png', 'rock28.png', 'rock29.png', 'rock30.png']
explosionSound = ['explosion.wav', 'explosion.wav', 'explosion.wav', 'explosion.wav', ]


def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x,y))
    
def initGame():
    global gamePad, clock, background, fighter, missile, explosion, missileSound, gameoverSound

    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight) )
    pygame.display.set_caption('PyShooting')
    background = pygame.image.load('game_screen.png')
    fighter = pygame.image.load('spaceship.png')
    clock = pygame.time.Clock()

def runGame():
    global gamePad, clock, background, fighter

    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    x = padWidth * 0.45
    y = padHeight * 0.9
    fighterX = 0


    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    fighterX -= 5                

                elif event.key == pygame.K_RIGHT:
                    fighterX += 5

            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX = 0

        drawObject(background, 0, 0 )
        x += fighterX
        if x < 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth

        drawObject(fighter, x, y )
        # gamePad.fill(BALCK)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()

initGame()
runGame()
