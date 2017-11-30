from Pregunta import*

class PreguntaO(Pregunta):
    def __init__(self):
        t = True
        f = False
        PreguntaO.open("POrientada.txt","r")
        PreguntaO.readline(2) = t
        PreguntaO.readline(8) = t
        PreguntaO.readline(10) = t
        PreguntaO.readline(15) = t
        PreguntaO.readline(19) = t
        PreguntaO.readline(23) = t
        PreguntaO.readline(28) = t
        r = randit (0,28)
        if r % 4 == 0:
            PreguntaO.readline(r)
        else: r = r+1
