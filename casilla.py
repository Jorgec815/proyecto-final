import pygame
import sys, pygame, util
from pygame import *
from pygame.sprite import Sprite
from pygame.locals import *
import util
from random import *

class Casilla (Sprite):
    def __init__ (self, coord, tipo):
        Sprite.__init__(self)
        self.imagenes = [util.cargar_imagen('imagenes/icono.png'),
                         util.cargar_imagen('imagenes/c++_imagen.png'),
                         util.cargar_imagen('imagenes/java_imagen.png')]
        self.image = self.imagenes[0]
        self.rect = self.image.get_rect()
	self.rect.move_ip(coord[0], coord[1])
	self.tipo = tipo
	self.rect.x = coord[0]
	self.rect.y = coord[1]

        
	
	
	
        
        
