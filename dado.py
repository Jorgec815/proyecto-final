import pygame
import sys, pygame, util
from pygame import *
from pygame.locals import *
import util
from random import *

class Dado():
    def __init__(self):
        self.imagenes = [util.cargar_imagen('imagenes/dado1.png'),
                         util.cargar_imagen('imagenes/dado2.png'),
                         util.cargar_imagen('imagenes/dado3.png'),
                         util.cargar_imagen('imagenes/dado4.png'),
                         util.cargar_imagen('imagenes/dado5.png'),
                         util.cargar_imagen('imagenes/dado6.png')]
        
        self.image = self.imagenes[0]
        self.rect = (975, 10)

    def update(self):
        
        num = randint(0,5)
        self.image = self.imagenes[num]
        self.numero = num
