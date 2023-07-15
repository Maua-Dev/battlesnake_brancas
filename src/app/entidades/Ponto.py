import math

from src.app.helpers.erro import Erro


class Ponto:
    def __init__(self, x:int, y:int):
        if(type(x) != int or type(y) != int):
            raise Erro("Ponto deve ser instanciado com inteiros")
        if(x < 0 or y < 0):
            raise Erro("Ponto não pode ter coordenadas negativas")
        else:
            self.x = x
            self.y = y
    
    def distancia(self, other):
        return round(math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2), 6)

    def __str__(self):
        return f'({self.x},{self.y})'
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y