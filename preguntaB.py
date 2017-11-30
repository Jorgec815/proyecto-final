from pregunta import *

class PreguntaB(Pregunta):
    def __init__(self):
        PreguntaB.open("PBasica.txt","r")
        t = True
        f = False
        PreguntaB.readline(4) = t
        PreguntaB.readline(6) = t
        PreguntaB.readline(11)= t 
        PreguntaB.readline(15)= t
        PreguntaB.readline(19)= t
        PreguntaB.readline(24)= t
        PreguntaB.readline(28)= t
        r = randit (0,28)
        if r % 4 == 0:
            PreguntaB.readline(r)
        else: r = r+1
