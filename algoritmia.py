from pregunta import*

class Algoritmia(Pregunta):
    def __init__(self):
        Algoritmia.open("Algoritmia","r")
        t = True
        f = False
        Algoritmia.readline(2) = t
        Algoritmia.readline(7) = t
        Algoritmia.readline(12) = t
        Algoritmia.readline(16) = t
        Algoritmia.readline(18) = t
        Algoritmia.readline(23) = t
        Algoritmia.readline(28) = t
        r = randit (0,28)
        if r % 4 == 0:
            Algoritmia.readline(r)
        else: r = r+1
