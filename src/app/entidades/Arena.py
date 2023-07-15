from ast import Dict
import math
from typing import List
from src.app.entidades.Cobra import Cobra

from src.app.entidades.Ponto import Ponto


class Arena:
    """
    link: https://docs.battlesnake.com/api/objects/board
    """
    __height:int
    __width:int
    __food:List[Ponto]
    __hazards:List[Ponto]
    __snakes:List[Cobra]

    def __init__(self, body:dict):
        """
        EX: 

        body = {
            "height": 11,
            "width": 11,
            "food": [
                {"x": 5, "y": 5}, 
                {"x": 9, "y": 0}, 
                {"x": 2, "y": 6}
            ],
            "hazards": [
                {"x": 0, "y": 0}, 
                {"x": 0, "y": 1}, 
                {"x": 0, "y": 2}
            ],
            "snakes": [
                {"id": "snake-one", ... },
                {"id": "snake-two", ... },
                {"id": "snake-three", ... }
            ]
        }
        """ 
        self.__height = body["height"]
        self.__width = body["width"]
        self.__food = [Ponto(x=ponto['x'], y=ponto['y']) for ponto in body["food"]]
        self.__hazards = [Ponto(x=ponto['x'], y=ponto['y']) for ponto in body["hazards"]]
        self.__snakes = [Cobra(body=body_cobra) for body_cobra in body["snakes"]]
    
    def retorna_centro(self) -> List[Ponto]:
        retorno = list()
        x = self.__width - 1
        y = self.__height - 1
        baixo_esquerda = Ponto(x=math.ceil((x)/2)-1, y=math.ceil((y)/2)-1)
        
        retorno.append(baixo_esquerda)
        retorno.append(Ponto(x=baixo_esquerda.x+1, y=baixo_esquerda.y))        
        retorno.append(Ponto(x=baixo_esquerda.x, y=baixo_esquerda.y+1))        
        retorno.append(Ponto(x=baixo_esquerda.x+1, y=baixo_esquerda.y+1))        
        
        return retorno
    
    def retorna_comidas(self) -> List[Ponto]:
        return self.__food

    def retorna_perigos(self) -> List[Ponto]:
        """
        perigos: hazard, cobras, redondezas da cabeça
        """
        retorno = list()
        retorno.extend(self.__hazards)
        retorno.extend(self.__snakes)
        for cobra in self.__snakes:
            retorno.extend(cobra.retorna_redondezas_da_cabeca(altura_max=self.__height, largura_max=self.__width))
        return list(set(retorno))

