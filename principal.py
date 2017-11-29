import sys, pygame, util
from time import *
from pygame.locals import *
from dado import *
from casilla import *
from ficha import *


SCREEN_WITDTH = 1024
SCREEN_HEIGHT = 768
ICON_SIZE = 100

def game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode( (SCREEN_WITDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption ( "Preguntas" )
    background_image = util.cargar_imagen( "imagenes/fondo.png" )
    pygame.mouse.set_visible( True )
    temporizador = pygame.time.Clock()
    dado = Dado()
    casilla = [Casilla((90,50), 'basica'),Casilla((290,50), 'orientada'),
               Casilla((90,250), 'orientada'),Casilla((290,250), 'basica')]
    fichas = [Ficha((10,240),1), Ficha((10,260),2)]

    while True:

        fuente = pygame.font.Font(None,25)
        texto_dado = fuente.render("Presione espacio para lanzar el dado",1,(0,0,0))
        screen.blit(background_image, (0,0))

        teclas = pygame.key.get_pressed()
        if teclas[K_SPACE]:
            for x in range (10):
                for y in range (6):
                    num = randint (0,5)
                    dado.update()
                    screen.blit(dado.image, dado.rect)


        for n in casilla:
            if (n.tipo == 'basica'):
                n.image = n.imagenes[1]
                screen.blit(n.image , n.rect)
                n.update()
            elif(n.tipo == 'orientada'):
                n.image = n.imagenes[2]
                screen.blit(n.image , n.rect)
                n.update()

        for n in fichas:
            if (n.jugador == 1):
                n.image = n.imagenes[0]
                screen.blit(n.image, n.rect)
                n.update(casilla[0])
            elif(n.jugador == 2):
                n.image = n.imagenes[1]
                screen.blit(n.image, n.rect)
                n.update(casilla[0])
                

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #screen.blit(background_image, (0,0))
        screen.blit(dado.image, dado.rect)
        screen.blit(texto_dado, (300,600))

        pygame.display.update()
        pygame.time.delay(10)

if __name__ == '__main__':
    game()
