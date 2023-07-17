from typing import List
from src.app.entidades.Arena import Arena
from src.app.entidades.Cobra import Cobra
from src.app.entidades.Ponto import Ponto
from src.app.helpers.erro import Erro


class BattleSnake(Cobra):
    """
    link: https://docs.battlesnake.com/api/objects/battlesnake
    """
    __health:int
    __body:List[Ponto]
    __head:Ponto
    __length:int
    modo: int = None

    def __init__(self, body:dict, arena: Arena):
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
        self.arena = arena

    def seta_modo(self) -> None:
        if self.get_length() < 4:
            self.modo = 1
            return None
        
        centros = self.arena.retorna_centro()
        if str(self.get_head()) not in [str(centro) for centro in centros]:
            self.modo = 2
            return None
        
        else:
            self.modo = 3
            return None
        
    def movimenta(self) -> None:
        if self.modo == None:
            raise Erro("Modo não setado")
        
        movimentos = {
            "up": (0,1),
            "down": (0,-1),
            "left": (-1,0),
            "right": (1,0)
        }
        possiveis_movimentos = movimentos.copy()

        corpo = self.get_body()
        if len(corpo) < 2:
            raise Erro("Corpo inválido")
        
        cabeca = self.get_head()
        pescoco = corpo[1]
        if pescoco.x < cabeca.x and pescoco.y == cabeca.y: possiveis_movimentos.pop("left")
        elif pescoco.x > cabeca.x and pescoco.y == cabeca.y: possiveis_movimentos.pop("right")
        elif pescoco.x == cabeca.x and pescoco.y < cabeca.y: possiveis_movimentos.pop("down")
        elif pescoco.x == cabeca.x and pescoco.y > cabeca.y: possiveis_movimentos.pop("up")
        else:
            raise Erro("Pescoco inválido")



        if self.modo == 1: 
            comida = self.encontra_comida_mais_perto(lista_de_comidas=self.arena.retorna_comidas())
            cabeca = self.get_head()
            
            if cabeca.x > comida.x: possiveis_movimentos.pop("right", None)
            elif cabeca.x < comida.x: possiveis_movimentos.pop("left", None)
            else:
                possiveis_movimentos.pop("right", None)
                possiveis_movimentos.pop("left", None)
                
            if cabeca.y > comida.y: possiveis_movimentos.pop("up", None)
            elif cabeca.y < comida.y: possiveis_movimentos.pop("down", None)
            else:
                possiveis_movimentos.pop("up", None)
                possiveis_movimentos.pop("down", None)
                
            for movimento in movimentos:
                if cabeca.x + movimentos[movimento][0] < 0 or cabeca.y + movimentos[movimento][1] < 0: 
                    pass
                elif str(Ponto(
                    x=cabeca.x + movimentos[movimento][0],
                    y=cabeca.y + movimentos[movimento][1]
                )) in [str(perigo) for perigo in self.arena.retorna_perigos()]:
                    possiveis_movimentos.pop(movimento, None)
        
            if len(possiveis_movimentos) == 0:
                raise Erro("Não há movimentos possíveis, derrota da cobra")    
            
            return list(possiveis_movimentos.keys())[0]
        
                

        elif self.modo == 2: pass
        elif self.modo == 3: pass
        else:
            raise Erro("Modo inválido")