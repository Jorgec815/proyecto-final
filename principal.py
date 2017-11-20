import sys, pygame, util
from time import *
from pygame.locals import *
from dado import *


SCREEN_WITDTH = 1024
SCREEN_HEIGHT = 768
ICON_SIZE = 32

def game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode( (SCREEN_WITDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption ( "Preguntas" )
    background_image = util.cargar_imagen( "imagenes/tablero.jpg" )
    pygame.mouse.set_visible( True )
    temporizador = pygame.time.Clock()
    
    dado = Dado()

    while True:

        fuente = pygame.font.Font(None,25)
        texto_dado = fuente.render("Presione espacio para lanzar el dado",1,(0,0,0))

        teclas = pygame.key.get_pressed()
        if teclas[K_SPACE]:
            for x in range (10):
                for y in range (6):
                    dado.update()
                    screen.blit(dado.image, dado.rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, (0,0))
        screen.blit(dado.image, dado.rect)
        screen.blit(texto_dado, (300,600))

        pygame.display.update()
        pygame.time.delay(10)

if __name__ == '__main__':
    game()
