import pygame
import sys, pygame, util
from pygame import *
from pygame.locals import *
from random import *


class Pregunta():
    def __init__(self):
        self.open = open("archivo","r")
        self.readline();
        for line in self:
            print line
            print line+1
            print line+2
            print line+3
        self.close()
