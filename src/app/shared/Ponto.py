import math

from .erro import Erro



class Ponto:
    def __init__(self, x:int = None, y:int = None, ponto_string: str = None):
        if ponto_string == None:
            if(type(x) != int or type(y) != int):
                raise Erro("Ponto deve ser instanciado com inteiros")
            if(x < 0 or y < 0):
                raise Erro("Ponto não pode ter coordenadas negativas")
            else:
                self.x = x
                self.y = y
        else:
            try:
                ponto_string = ponto_string.replace('(', '').replace(')', '')
                lista_das_coordenadas = ponto_string.split(',')
                self.x = int(lista_das_coordenadas[0])
                self.y = int(lista_das_coordenadas[1])
            except:
                raise Erro("Erro na conversão de string para Ponto")

    def distancia(self, other) -> float:
        return round(math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2), 6)

    def __str__(self):
        return f'({self.x},{self.y})'
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y