import pygame
import util
from pygame.sprite import Sprite
from pygame import *
from dado import *


class Ficha(Sprite):
	def __init__(self, coord, puntos):
		Sprite.__init__(self)
		self.puntos = puntos
		self.image= util.cargar_imagen('imagenes/ficha1.png')
		self.rect = self.image.get_rect()
		self.rect.move_ip(coord[0], coord[1])
	def update(self, casilla):
		if self.rect.x < casilla.rect.x:
			self.rect.x = self.rect.x + 1
                if self.rect.x > casilla.rect.x:
			self.rect.x = self.rect.x - 1
		if self.rect.y < casilla.rect.y:
			self.rect.y = self.rect.y + 1
		if self.rect.y > casilla.rect.y:
			self.rect.y = self.rect.y - 1
