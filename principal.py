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
    pygame.mouse.set_visible( True )
    screen = pygame.display.set_mode( (SCREEN_WITDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption ( "Preguntas" )
    background_image = util.cargar_imagen( "imagenes/fondo.png" )
    dado = Dado(0)
    casilla = [Casilla((70,50), 'basica'),Casilla((140,50), 'orientada'),
               Casilla((210,50), 'basica'),Casilla((280,50), 'orientada'),
               Casilla((350,50), 'basica'),Casilla((420,50), 'orientada'),
               Casilla((490,50), 'basica'),Casilla((560,50), 'orientada'),
               Casilla((630,50), 'basica'),Casilla((700,50), 'orientada'),
               Casilla((70,200), 'basica'),Casilla((140,200), 'orientada'),
               Casilla((210,200), 'basica'),Casilla((280,200), 'orientada'),
               Casilla((350,200), 'basica'),Casilla((420,200), 'orientada'),
               Casilla((490,200), 'basica'),Casilla((560,200), 'orientada'),
               Casilla((630,200), 'basica'),Casilla((700,200), 'orientada'),
               Casilla((70,350), 'basica'),Casilla((140,350), 'orientada'),
               Casilla((210,350), 'basica'),Casilla((280,350), 'orientada'),
               Casilla((350,350), 'basica'),Casilla((420,350), 'orientada'),
               Casilla((490,350), 'basica'),Casilla((560,350), 'orientada'),
               Casilla((630,350), 'basica'),Casilla((700,350), 'orientada')
               ]
    ficha = Ficha((10,10), 0)

    jugando = False
    mover = False
    pregunta = False

    pos_actual = 0
    pos_siguiente = 0

    while True:

        teclas = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if teclas[K_d]:
            print("La tecla del dado fue presionada")
            jugando = False
            mover = True

        if teclas[K_SPACE]:
            ficha.puntos = 0
            pos_actual = 0
            pos_siguiente = 0
            
            jugando = True
            mover = False
            pregunta = False

        if jugando:
            
            
            fuente = pygame.font.Font(None,25)
            puntos = fuente.render("Puntos" + str(ficha.puntos),1,(0,0,0))

            screen.blit(background_image, (0,0))
            screen.blit(dado.image, dado.rect)
            screen.blit(ficha.image, ficha.rect)
            screen.blit(puntos, (900,10))

            while(pos_siguiente >= 30):
                pos_siguiente -= 1

            ficha.update(casilla[pos_siguiente])

            if (pos_siguiente == 30):
                print("Game Over")

            pos_actual = pos_siguiente

            for n in casilla:
                if (n.tipo == 'basica'):
                    n.image = n.imagenes[1]
                    screen.blit(n.image , n.rect)
                    n.update()
                elif(n.tipo == 'orientada'):
                    n.image = n.imagenes[2]
                    screen.blit(n.image , n.rect)
                    n.update()

        elif mover:

            dado.valor = randint(1,6)
            dado.image = dado.imagenes[dado.valor]
            screen.blit(dado.image, dado.rect)

            print("El valor del dado es", dado.valor)

            pos_siguiente = pos_actual + dado.valor

            mover = False
            pregunta = True

            jugando = True

        else:

            inicio_image = util.cargar_imagen('imagenes/inicio.jpg')
            spacebar_image = util.cargar_imagen('imagenes/spacebar.png')

            screen.blit(inicio_image, (0,0))
            screen.blit(spacebar_image, (250,400))

            fuente = pygame.font.Font(None, 150)
            titulo_inicio = fuente.render("Preguntas",1,(0,0,0))
            screen.blit(titulo_inicio, (250,250))

        pygame.display.update()
        pygame.time.delay(10)

if __name__ == '__main__':
    game()
            
        

            
            
            
    
