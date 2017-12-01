#importe de las librerías necesarias
import sys, pygame, util
from time import *
from pygame.locals import *
from dado import *
from casilla import *
from ficha import *

#Dimensiones de la pantalla
SCREEN_WITDTH = 1024
SCREEN_HEIGHT = 768
ICON_SIZE = 100

def game():
    #Inicialización de algunos métodos
    pygame.init()
    pygame.mixer.init()
    pygame.mouse.set_visible( True )
    screen = pygame.display.set_mode( (SCREEN_WITDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption ( "Preguntas" )
    background_image = util.cargar_imagen( "imagenes/tablero3.jpg" )

    #creación de los objetos del juego
    dado = Dado(0)
    casilla = [Casilla((100,50), 'inicio'),Casilla((300,50), 'orientada'),
               Casilla((500,50), 'algoritmia'),Casilla((700,50), 'basica'),
               Casilla((900,50), 'orientada'),Casilla((900,175), 'algoritmia'),
               Casilla((700,175), 'basica'),Casilla((500,175), 'orientada'),
               Casilla((300,175), 'algoritmia'),Casilla((100,175), 'basica'),
               Casilla((100,300), 'orientada'),Casilla((300,300), 'algoritmia'),
               Casilla((500,300), 'basica'),Casilla((700,300), 'orientada'),
               Casilla((900,300), 'algoritmia'),Casilla((900,425), 'basica'),
               Casilla((700,425), 'orientada'),Casilla((500,425), 'algoritmia'),
               Casilla((300,425), 'basica'),Casilla((100,425), 'orientada'),
               Casilla((100,550), 'algoritmia'),Casilla((300,550), 'basica'),
               Casilla((500,550), 'orientada'),Casilla((700,550), 'algoritmia'),
               Casilla((900,550), 'basica'),Casilla((900,675), 'orientada'),
               Casilla((700,675), 'algoritmia'),Casilla((500,675), 'basica'),
               Casilla((300,675), 'orientada'),Casilla((100,675), 'final')
               ]
    ficha = Ficha((10,10), 0)

    #Estados para llevar un tiempo de ejecución
    jugando = False
    mover = False
    pregunta = False

    pos_actual = 0
    pos_siguiente = 0

    #ejecución del juego
    while True:

        teclas = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Detecta si la tecla "d" fue pulsada para proceder a lanzar el dado
        if teclas[K_d]:
            print("La tecla del dado fue presionada")
            jugando = False
            mover = True

        #Espacio se usa para reiniciar el juego
        if teclas[K_SPACE]:
            ficha.puntos = 0
            pos_actual = 0
            pos_siguiente = 0
            
            jugando = True
            mover = False
            pregunta = False

        #Juego activo
        if jugando:
            

            #Declaración del los texto que se imprimiran en pantalla
            fuente = pygame.font.Font(None,25)
            puntos = fuente.render("Puntos" + str(ficha.puntos),1,(255,255,255))

            screen.blit(background_image, (0,0))
            screen.blit(dado.image, dado.rect)
            screen.blit(ficha.image, ficha.rect)
            screen.blit(puntos, (900,10))

            while(pos_siguiente >= 30):
                pos_siguiente -= 1


            ficha.update(casilla[pos_siguiente])
            

            if (pos_siguiente == 30):
                print("Game Over")

            #"blit" de los objetos creados
            for n in casilla:
                if (n.tipo == 'basica'):
                    n.image = n.imagenes[1]
                    screen.blit(n.image , n.rect)
                elif(n.tipo == 'orientada'):
                    n.image = n.imagenes[2]
                    screen.blit(n.image , n.rect)
                elif(n.tipo == 'algoritmia'):
                    n.image = n.imagenes[3]
                    screen.blit(n.image, n.rect)
                elif(n.tipo == 'final'):
                    n.image = n.imagenes[4]
                    screen.blit(n.image, n.rect)
                elif(n.tipo == 'inicio'):
                    n.image = n.imagenes[5]
                    screen.blit(n.image, n.rect)

            screen.blit(ficha.image, ficha.rect)

            #Actualiza la posición actual de la ficha
            pos_actual = pos_siguiente

        
        #Cuando se lanza el dado
        elif mover:

            #Se le da un valor aleatorio al dado y se actualiza su imagen

            dado.valor = randint(1,6)
            dado.image = dado.imagenes[dado.valor]
            screen.blit(dado.image, dado.rect)

            print("El valor del dado es", dado.valor)

            pos_siguiente = pos_actual + dado.valor

            mover = False
            pregunta = False
            jugando = True

        #Si ningun estado se encuentra activo se imprimirá la pantalla de inicio  
        else:

            inicio_image = util.cargar_imagen('imagenes/inicio.jpg')
            spacebar_image = util.cargar_imagen('imagenes/spacebar.png')
            c_image = util.cargar_imagen('imagenes/c++_grande.png')
            java_image = util.cargar_imagen('imagenes/java_grande.png')
            algoritmia_image = util.cargar_imagen('imagenes/algoritmia_grande.png')

            screen.blit(inicio_image, (0,0))
            screen.blit(spacebar_image, (250,250))
            screen.blit(c_image, (150,500))
            screen.blit(java_image, (450,500))
            screen.blit(algoritmia_image, (750,500))
            

            fuente = pygame.font.Font(None, 150)
            titulo_inicio = fuente.render("Preguntas",1,(0,0,0))
            screen.blit(titulo_inicio, (250,100))
            fuente = pygame.font.Font(None, 40)
            c_inicio = fuente.render("Programación",1,(0,0,0))
            c2_inicio = fuente.render("Básica",1,(0,0,0))
            java_inicio = fuente.render("Orientada a",1,(0,0,0))
            java2_inicio = fuente.render("Objetos",1,(0,0,0))
            algoritmia_inicio = fuente.render("Algoritmia",1,(0,0,0))
            screen.blit(c_inicio, (150,700))
            screen.blit(c2_inicio, (150,725))
            screen.blit(java_inicio, (450,700))
            screen.blit(java2_inicio, (450,725))
            screen.blit(algoritmia_inicio, (750,700))
            
        #Actualización de la pantalla
        pygame.display.update()
        pygame.time.delay(10)

if __name__ == '__main__':
    game()
            
        

            
            
            
    
