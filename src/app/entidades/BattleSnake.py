from typing import List
from src.app.entidades.Arena import Arena
from src.app.entidades.Cobra import Cobra
from src.app.entidades.Ponto import Ponto


class BattleSnake(Cobra):
    """
    link: https://docs.battlesnake.com/api/objects/battlesnake
    """
    __health:int
    __body:List[Ponto]
    __head:Ponto
    __length:int
    modo: int

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

        modo: 1, 2, 3
        1: pegar tamanho = 4
            - deve buscar uma comida até ter tamanho = 4
        2: encontrar o centro
            - após atingir o tamanho determinado, deve encontrar o centro de batalha a fim de realizar a estratégia
        3: se manter no centro
            - ficar girando em circulos até morrer/partida acabar

        """
        super().__init__(body=body)
        self.get_length()

    def seta_modo(self, arena: Arena) -> None:
        if self.get_length() < 4:
            self.modo = 1
            return None
        
        centros = arena.retorna_centro()
        if str(self.get_head()) not in [str(centro) for centro in centros]:
            self.modo = 2
            return None
        
        else:
            self.modo = 3
            return None