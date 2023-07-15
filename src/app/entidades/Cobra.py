from typing import Dict, List

from src.app.entidades.Ponto import Ponto
from src.app.helpers.utils import Utils


class Cobra:
    """
    link: https://docs.battlesnake.com/api/objects/battlesnake
    """
    __health:int
    __body:List[Ponto]
    __head:Ponto
    __length:int
    
    def __init__(self, body:dict):
        """
        EX:

        body = {
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 0, "y": 0}, 
                {"x": 1, "y": 0}, 
                {"x": 2, "y": 0}
            ],
            "latency": "123",
            "head": {"x": 0, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                "color":"#26CF04",
                "head":"smile",
                "tail":"bolt"
            }
        }
        """

        self.__health = body["health"]
        self.__body = [Ponto(x=ponto['x'], y=ponto['y']) for ponto in body["body"]]
        self.__head = Ponto(x=body["head"]["x"], y=body["head"]["y"])
        self.__length = body["length"]
    

    def retorna_redondezas_da_cabeca(self, altura_max: int, largura_max: int) -> List[Ponto]:
        retorno = list()
        if self.__head.x-1 >= 0: retorno.append(Ponto(x=self.__head.x-1, y=self.__head.y)) 
        retorno.append(Ponto(x=self.__head.x+1, y=self.__head.y))
        if self.__head.y-1 >= 0: retorno.append(Ponto(x=self.__head.x, y=self.__head.y-1))
        retorno.append(Ponto(x=self.__head.x, y=self.__head.y+1))

        for ponto in retorno:
            if ponto.x >= largura_max or ponto.y >= altura_max:
                retorno.remove(ponto)

        return retorno

    def retorna_perigos(self, altura_max: int, largura_max: int) -> List[Ponto]:
        retorno = list()
        retorno.extend(self.retorna_redondezas_da_cabeca(altura_max=altura_max, largura_max=largura_max))
        retorno.extend(self.__body)

        return Utils.ponto_uniq(retorno)